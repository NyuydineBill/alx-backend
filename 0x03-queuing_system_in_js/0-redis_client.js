import redis from 'redis';

function redisConnect() {
  const client = redis.createClient();

  client.on('connect', () => {
    console.log('Redis client connected to the server');
    // Optional: Test connection with a Redis command
    client.set('key', 'value', (err, reply) => {
      if (err) {
        console.error(`Error setting key: ${err}`);
        return;
      }
      console.log(`Set key: ${reply}`);
      // Close the client after the test command
      client.quit();
    });
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
}

redisConnect();
