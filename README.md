# Welcome to EventPlaza

EventPlaza is a project brought to you by Abdorithm & HazemUsama. 

This project was born out of our own experiences as event organizers and our desire to support local events more efficiently. We recognized the need for a simple-to-use platform that could streamline event organization and management, leading us to develop EventPlaza.

## About the Project

EventPlaza is still a work-in-progress. While the current version represents the backbone, or minimum viable product (MVP), of our vision for the platform, there are many planned features yet to be implemented. We are committed to continuously improving and expanding EventPlaza to better meet the needs of event organizers and attendees alike.

## Contributing

We welcome contributions from the community to help us enhance and grow EventPlaza. Whether it's adding new features, fixing bugs, or providing feedback, your input is valuable to us. Please feel free to contribute or report any issues through our project's GitHub repository.

Thank you for your interest in EventPlaza!

# Installation

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

4. You will need to setup mysql server & put your google api (OAuth2) credentials in the container manually. Then run the setup script. OAuth credentials are needed for the email verification & password reset functionalities to work.
    ```bash
    mysql < setup_mysql_dev.sql
    ```

Now you can start exploring and testing EventPlaza in your development environment. Happy coding!