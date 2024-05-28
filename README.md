# Restaurant App in Django

## Overview
This is a Django-based web application for managing a restaurant. It includes features for handling menus, orders, and customer information, making it easier to manage a restaurant's daily operations.


**Note:** This project is currently in development. Features and functionality are subject to change.

## Features
- **Menu Management:** Create, update, and delete menu items.
- **Order Management:** Place and track customer orders.
- **Customer Management:** Manage customer information and order history.
- **User Authentication:** Secure login and registration system.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Virtualenv

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Sottie1/Restaurant-App-in-Django.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Restaurant-App-in-Django
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv myvenv
    ```
4. Activate the virtual environment:
    ```bash
    # On Windows
    myvenv\Scripts\activate

    # On Mac/Linux
    source myvenv/bin/activate
    ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Run database migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Navigate to `http://127.0.0.1:8000/` in your web browser.
2. Register a new user or log in with an existing account.
3. Start managing your restaurant's menu, orders, and customers.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- Django Documentation
- Bootstrap for front-end components
