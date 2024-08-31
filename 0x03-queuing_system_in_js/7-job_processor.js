import kue from 'kue';

// Define blacklisted phone numbers
const blacklist = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track initial progress
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklist.includes(phoneNumber)) {
    // Fail the job with an error
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    done(error);
  } else {
    // Update progress
    job.progress(50, 100);

    // Simulate sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Finish the job
    done();
  }
}

// Create a Kue queue with concurrency of 2 (two jobs at a time)
const queue = kue.createQueue({ concurrency: 2, redis: { port: 6379, host: '127.0.0.1' } });

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Retrieve phone number and message from job data
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
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
    console.log('Kue shutdown:', err || '');
    process.exit(0);
  });
});
