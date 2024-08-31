import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
  let queue;

  // Before each test, set up the queue and enter test mode
  beforeEach(function (done) {
    queue = kue.createQueue();
    queue.testMode.enter();
    done();
  });

  // After each test, clear the queue and exit test mode
  afterEach(function (done) {
    queue.testMode.clear();
    queue.testMode.exit();
    done();
  });

  it('display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Verify job creation and properties
    const job1 = queue.testMode.jobs[0];
    const job2 = queue.testMode.jobs[1];

    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data).to.deep.equal(jobs[0]);

    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.deep.equal(jobs[1]);
  });

  // Add more tests as needed for job completion, failure handling, etc.
});
