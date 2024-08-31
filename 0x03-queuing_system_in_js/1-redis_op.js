import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Function to handle Redis connection events
function redisConnect() {
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
}

// Function to set a new school name and value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a given school name from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err}`);
      return;
    }
    console.log(`Value for ${schoolName}: ${reply}`);
  });
}

// Calling the functions as per your requirements
redisConnect();

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
