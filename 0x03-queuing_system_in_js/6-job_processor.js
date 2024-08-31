import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from queue
queue.process('push_notification_code', (job, done) => {
  // Extract job data
  const { phoneNumber, message } = job.data;

  // Call function to send notification
  sendNotification(phoneNumber, message);

  // Mark job as completed
  done();
});

// Log when the queue is ready
queue.on('ready', () => {
  console.log('Queue is ready to process jobs');
});

// Log when there's an error in the queue
queue.on('error', (err) => {
  console.error('Queue error:', err);
});

// Graceful shutdown of the queue process
process.once('SIGTERM', () => {
  queue.shutdown(5000, (err) => {
    console.log('Kue shutdown: ', err || '');
    process.exit(0);
  });
});
