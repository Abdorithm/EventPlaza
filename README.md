# Welcome to EventPlaza

EventPlaza is a project brought to you by Abdorithm & HazemUsama. 

This project was born out of our own experiences as event organizers and our desire to support local events more efficiently. We recognized the need for a simple-to-use platform that could streamline event organization and management, leading us to develop EventPlaza.

## About the Project

EventPlaza is still a work-in-progress. While the current version represents the backbone, or minimum viable product (MVP), of our vision for the platform, there are many planned features yet to be implemented. We are committed to continuously improving and expanding EventPlaza to better meet the needs of event organizers and attendees alike.

## Contributing

Your input is valuable to us. Please feel free to contribute or report any issues through our project's GitHub repository.

Thank you for your interest in EventPlaza!

## Installation

To run EventPlaza in a development environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/EventPlaza.git
   ```
   Replace `your_username` with your GitHub username.

2. Navigate to the project directory:
   ```bash
   cd EventPlaza
   ```

3. Build the Docker image:
   ```bash
   docker build -t plaza .
   ```

4. You will need to setup mysql server & run the setup script.
    ```bash
    mysql < setup_mysql_dev.sql
    ```

5. You will need to have a google OAuth2 api credentials for the email verification and password reset functionalities to work. For more info, check [Setting Up OAuth 2.0 from Google Cloud](https://support.google.com/cloud/answer/6158849). You might need to independently run the `send_email.py` script on an environment with GUI (your local machine) to generate the `gmail-python-email-send.json` file. Afterwards, transfer both files `client_secret.json` and `gmail-python-email-send.json` to the docker container. `client_secret.json` should be in `event_plaza/`, the app package directory. Modify the `event_plaza/send_email.py` script to make it find the `gmail-python-email-send.json` wherever you put it in your system. By default, `~/.credentials/gmail-python-email-send.json` is the path where it looks for that file. Contact us if you need help setting up this mess.

Now you can start exploring and testing EventPlaza in your development environment. Happy coding!

The project is currently (temporarily) deployed [here](http://web-02.abdorithm.tech/eventplaza/)

## Technologies

1. SQLalchemy (ORM with python)
2. MySQL (Relational Database Management System)
3. Python (Back-end)
4. JavaScript (Front-end)
5. Flask (Web Microframework)
6. TailwindCSS (CSS Framework)
