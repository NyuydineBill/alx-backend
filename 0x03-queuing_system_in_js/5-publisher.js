import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Function to handle Redis connection events
function redisConnect() {
  publisher.on('connect', () => {
    console.log('Redis client connected to the server');
    // Publish messages after a certain delay
    setTimeout(() => {
      publishMessage("Holberton Student #1 starts course", 100);
      publishMessage("Holberton Student #2 starts course", 200);
      publishMessage("KILL_SERVER", 300);
      publishMessage("Holberton Student #3 starts course", 400);
    }, 50); // Delay to ensure the subscriber is ready
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
}

// Function to publish a message to a Redis channel after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Start the Redis connection
redisConnect();
