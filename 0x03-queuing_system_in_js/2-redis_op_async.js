import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to handle Redis connection events
function redisConnect() {
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
}

// Function to set a new school name and value in Redis
async function setNewSchool(schoolName, value) {
  try {
    await setAsync(schoolName, value);
    console.log(`Set ${schoolName} = ${value}`);
  } catch (error) {
    console.error(`Error setting ${schoolName}: ${error}`);
  }
}

// Function to display the value for a given school name from Redis using async/await
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`Value for ${schoolName}: ${reply}`);
  } catch (error) {
    console.error(`Error getting value for ${schoolName}: ${error}`);
  }
}

// Calling the functions as per your requirements
redisConnect();

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  // Optionally quit the Redis client after operations
  client.quit();
})();
