# README.md

## Curriculum - 0x02 i18n

### Overview
This project focuses on internationalization (i18n) in a Flask web application. The goal is to create a basic Flask app, set up Babel for localization, and implement features such as parametrizing templates, forcing locale with URL parameters, emulating user login, and handling time zones.

### Project Structure
The project is organized into multiple tasks, each building upon the previous one. The tasks are outlined below:

1. **Basic Flask App**
   - Create a simple Flask app with a single route and template.

2. **Basic Babel Setup**
   - Install Flask-Babel extension and configure it with language support.

3. **Get Locale from Request**
   - Implement a function to determine the best match for the user's preferred language.

4. **Parametrize Templates**
   - Use the `_` or `gettext` function to parametrize templates and set up translation dictionaries.

5. **Force Locale with URL Parameter**
   - Implement a way to force a specific locale by passing a parameter in the app's URLs.

6. **Mock Logging In**
   - Emulate user login behavior by creating a mock user table and displaying personalized messages.

7. **Use User Locale**
   - Update the app to use a user's preferred locale, giving priority to URL parameters, user settings, and request headers.

8. **Infer Appropriate Time Zone**
   - Implement a function to infer the appropriate time zone based on URL parameters, user settings, or default to UTC.

### Requirements
Ensure the following requirements are met for the successful execution of the project:

- Python version: 3.7
- Operating System: Ubuntu 18.04 LTS
- Code Style: Pycodestyle (version 2.5)
- Execution: All Python files should have the shebang `#!/usr/bin/env python3`
- Documentation: All modules, classes, functions, and methods should have appropriate documentation.
- Type Annotations: All functions and coroutines must be type-annotated.

### How to Run
1. Clone the GitHub repository:
   ```
   git clone https://github.com/username/alx-backend.git
   cd alx-backend/0x02-i18n
   ```

2. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```

3. Execute the desired task (e.g., Task 1):
   ```
   python3 1-app.py
   ```

### Testing
To run the automated tests, execute the following command:
   ```
   python3 -m unittest discover tests
   ```

### Manual QA Review
Upon completing each task, initiate a manual QA review and address any feedback provided.

### Additional Notes
- The project is an ongoing second chance project with a deadline.
- Automatic QA reviews will be launched at the specified deadlines.
- Copyright © 2024 ALX, All rights reserved.