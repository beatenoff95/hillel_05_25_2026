# Homework 31.1 Jenkins Pipeline

This homework adds a Jenkins Pipeline for the Python tests from `lesson_30`.

## What the pipeline does

- Checks out the repository code.
- Creates a Python virtual environment.
- Installs dependencies from `lesson_30/requirements.txt`.
- Starts a temporary PostgreSQL container for the tests.
- Runs pytest and writes JUnit results to `test-results/pytest-results.xml`.
- Archives Allure result files from `lesson_30/allure-results`.
- Publishes test results in Jenkins with the `junit` step.
- Sends a build result email to `InsertYour@Mail.Here` with the Jenkins `mail` step.

## Local Jenkins requirements

- Jenkins Pipeline support.
- Jenkins Mailer plugin and configured SMTP server.
- Docker available to the Jenkins agent.
- Python 3 available as `py -3` on Windows or `python3` on Linux/macOS.

## Jenkins setup

1. Create a new Pipeline or Multibranch Pipeline job.
2. Point it to this Git repository.
3. Use `Jenkinsfile` from the repository root.
4. Configure SMTP in Jenkins: `Manage Jenkins` -> `System` -> `E-mail Notification`.
5. Run the job and check `Test Result`, archived artifacts, and the email notification.

The `pollSCM('H/2 * * * *')` trigger checks the repository regularly so the pipeline can run after new commits. If the repository is hosted remotely, a webhook can be added in addition to polling.
