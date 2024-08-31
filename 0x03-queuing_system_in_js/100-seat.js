import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const client = redis.createClient();
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const queue = kue.createQueue();

const app = express();
const port = 1245;

// Initialize available seats and reservation status
(async () => {
  await setAsync('available_seats', '50');
})();
let reservationEnabled = true;

// Function to reserve a seat
async function reserveSeat(number) {
  await setAsync('available_seats', number.toString());
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats) || 0;
}

// Route to get number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save(err => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', err => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route to process the queue and reserve seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats === 0) {
    reservationEnabled = false;
  }

  if (currentAvailableSeats >= 1) {
    const job = queue.create('reserve_seat').save();
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', err => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });

    // Reduce available seats by 1
    await reserveSeat(currentAvailableSeats - 1);
  } else {
    const errorMessage = 'Not enough seats available';
    const job = queue.create('reserve_seat').failed().error(new Error(errorMessage));
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
