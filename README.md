---
# Project Title: Python-Django Mock Management Tool


## Introduction
This project is a comprehensive mock management tool developed using Python programming language and the Django web framework. It streamlines the process of managing mock API endpoints by leveraging the power of Django's built-in Admin interface. The tool allows you to effortlessly create, update, and maintain simulated APIs with various configurations including URLs, request methods, response parameters, latency, and activation status.

### Key Features
- **User-friendly Interface**: Utilizes Django's Admin Dashboard and enhances it with the SimpleUI plugin for an intuitive and visually appealing user experience.
- **Mock Endpoint Management**: Directly edit and configure mock endpoints including:
    - URL paths
    - HTTP Request Methods (GET, POST, PUT, DELETE, etc.)
    - Response Parameters
    - Delay settings to simulate server latency
    - Enable or disable mock endpoints as needed
- **Django Integration**: Seamless integration with existing Django projects, making it easy to incorporate into your development workflow.

## Getting Started
### Installation
1. Clone the repository:
    ```
    git clone [https://github.com/YourUsername/PythonDjangoMockManager.git](https://github.com/treatortrick/network-mock-server.git)
    cd PythonDjangoMockManager
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set up the database and apply migrations:
    ```
     python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser to access the Admin panel:
    ```
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

6. Visit `http://localhost:8000/admin` to access the Mock Manager and start configuring your endpoints.

## Usage
Login to the Django Admin interface with your created superuser credentials, navigate to the Mock Endpoints section, and begin adding/editing mock API configurations.

## Contributing
We welcome contributions from the community. If you'd like to contribute, please fork this repository, make changes, and submit a pull request. Or send me an E-mail: renkmail@163.com.

## Contact & Support
If you have any questions, issues, or suggestions, feel free to open an issue in this repository. Your feedback is valuable!

Thank you for considering using our Python-Django Mock Management Tool. Happy coding!
