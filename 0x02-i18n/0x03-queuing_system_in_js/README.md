# Project README.md

## Queuing System in JS

### Project Overview

This project focuses on building a queuing system in JavaScript using Redis, NodeJS, and the Kue library. The system involves creating a Redis server, implementing a Redis client for basic and advanced operations, and building a basic Express app that interacts with Redis and utilizes a queue system.

### Project Details

#### Curriculum Information

- **Short Specializations:** 0x03. Queuing System in JS
- **Back-end Technologies:** JavaScript (ES6), Redis, NodeJS, ExpressJS, Kue
- **Author:** Johann Kerbrat, Engineering Manager at Uber Works
- **Weight:** 1
- **Project Duration:** March 4, 2024, 6:00 AM - March 7, 2024, 6:00 AM
- **QA Review:** Manual QA review required

#### Learning Objectives

By the end of this project, you should be able to explain the following concepts without using external resources:

1. Running a Redis server on your machine
2. Performing simple operations with the Redis client
3. Using a Redis client with NodeJS for basic operations
4. Storing hash values in Redis
5. Handling asynchronous operations with Redis
6. Implementing Kue as a queue system
7. Building a basic Express app interacting with a Redis server
8. Extending the Express app to interact with both a Redis server and a queue

#### Project Requirements

- All code to be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A `README.md` file is mandatory
- Code should use the `.js` extension

#### Required Files for the Project

1. `package.json`
2. `.babelrc`

**Note:** Don't forget to run `$ npm install` when you have the `package.json`

### Project Tasks

#### 0. Install a Redis Instance

- **Description:** Download, extract, compile the latest stable Redis version (higher than 5.0.7) and set up a Redis server.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `README.md`, `dump.rdb`

#### 1. Node Redis Client

- **Description:** Install `node_redis` using npm and create a script that connects to the Redis server.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `0-redis_client.js`

#### 2. Node Redis Client and Basic Operations

- **Description:** Extend the previous script to include functions for setting and displaying values in Redis.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `1-redis_op.js`

#### 3. Node Redis Client and Async Operations

- **Description:** Modify the previous script to use ES6 async/await with promisify.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `2-redis_op_async.js`

#### 4. Node Redis Client and Advanced Operations

- **Description:** Use the Redis client to store a hash value and display it.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `4-redis_advanced_op.js`

#### 5. Node Redis Client Publisher and Subscriber

- **Description:** Implement a basic Redis-based queuing system with a publisher and subscriber.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **Files:** `5-subscriber.js`, `5-publisher.js`

#### 6. Create the Job Creator

- **Description:** Create a script that generates job data and pushes it to a Redis-based queue.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `6-job_creator.js`

#### 7. Create the Job Processor

- **Description:** Create a script that processes jobs from a Redis-based queue.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `6-job_processor.js`

#### 8. Track Progress and Errors with Kue: Create the Job Creator

- **Description:** Create a script that generates job data and tracks their progress and errors.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `7-job_creator.js`

#### 9. Track

 Progress and Errors with Kue: Create the Job Processor

- **Description:** Modify the previous job processor script to track progress and handle errors using Kue.
- **Repo:** [GitHub repository: alx-backend](#)
- **Directory:** `0x03-queuing_system_in_js`
- **File:** `7-job_processor.js`

### Evaluation

Your project will be manually reviewed based on the following criteria:

- Correctness
- Readability
- Maintainability
- Code efficiency
- Adherence to the project requirements
- Proper error handling and testing
- Compliance with the learning objectives

### Resources

- [Redis Downloads](https://redis.io/download)
- [Node Redis GitHub Repository](https://github.com/NodeRedis/node-redis)
- [Kue GitHub Repository](https://github.com/Automattic/kue)
- [Express.js](https://expressjs.com/)