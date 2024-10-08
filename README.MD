# Django and React Authentication with JWT and HTTP-Only Cookies

This project implements a user authentication system using Django and React. It includes user registration, login, logout, and fetching user data. Authentication is handled using JWT (JSON Web Tokens) and HTTP-only cookies for improved security. The application's frontend is styled using Bootstrap.

The project consists of two directories: 

- `client`: Contains the React application
- `server`: Contains the Django backend

## Installation

To run this project on your local machine, follow the steps below:

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8 or higher
- Node.js v14.15.0 or higher
- npm 6.14.9 or higher

### Setup

1. Clone the repository:
    ```
    git clone https://github.com/iwantcustomgift-lab/test.git
    ```
2. Change into the directory:
    ```
    cd test
    ```

### Server

1. Navigate to the `server` directory:
    ```
    cd server
    ```
2. Install Django and other dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the server:
    ```
    python manage.py runserver
    ```

### Client

1. Navigate to the `client` directory:
    ```
    cd ../client
    ```
2. Install all the dependencies:
    ```
    npm install
    ```
3. Run the client:
    ```
    npm start
    ```

Now, your application should be running at `localhost:3000`.

Note:
- The Django server should be running at the same time as the React application for the system to function properly.
- The application uses the email field instead of the username field for user identification.


## Task
1. Add an input field for the user's Ethereum wallet address to the registration page. When a user registers an account, this wallet address must be saved to the database.
2. After login, the homepage must show the balance of the user's Ethereum wallet address.

Commit your code to your personal git and share the link.

## Test work is done
- I added Dockerfiles and docker-compose.yml files for easy and quick dev environment setup. You can now just run following command to run & up both the client and server applications at the same time and do development work. Any changes in any files will be updated live.
```
$ docker compose up --build -d
```
- I just did the minimum work to complete the task. There might be many other places where we can do optimizations and implement scripts for automation.
- For ethereum balance check i used EthereumTesterProvider for quick response to your task.
