import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Function to handle Redis connection events
function redisConnect() {
  subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
    subscriber.subscribe('holberton school channel');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
}

// Function to handle messages received from subscribed channels
subscriber.on('message', (channel, message) => {
  console.log(`Message received on channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});

// Start the Redis connection
redisConnect();
