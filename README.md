# Expense Sharing Application

## Overview

This is a Django-based expense-sharing application that allows users to manage shared expenses. Users can create accounts, add expenses, and track how much they owe or are owed by others.

## Features

- User registration and management
- Adding and tracking expenses
- Viewing expenses by user
- Viewing overall expenses

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Suresh-Kanth/Expense-Sharing.git
    cd expense_sharing
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python3 manage.py createsuperuser
    ```

6. **Run the server:**

    ```bash
    python3 manage.py runserver
    ```

## API Endpoints

### Create a User

- **URL:** `/api/users/`
- **Method:** POST
- **Request Body:**

    ```json
    {
      "email": "user@example.com",
      "name": "John Doe",
      "mobile_number": "1234567890"
    }
    ```

### Get User Details

- **URL:** `/api/users/<user_id>/`
- **Method:** GET

### Add an Expense

- **URL:** `/api/expenses/`
- **Method:** POST
- **Request Body:**

    ```json
    {
      "user": 1,
      "description": "Dinner",
      "amount": 50.00,
      "split_type": "equal",
      "split_details": {
        "user_ids": [1, 2, 3],
        "amounts": [16.67, 16.67, 16.66]
      }
    }
    ```

### Get All Expenses for a User

- **URL:** `/api/users/<user_id>/expenses/`
- **Method:** GET

### Get All Expenses

- **URL:** `/api/expenses/overall/`
- **Method:** GET

## Example Usage with curl

1. **Create a User:**

    ```bash
    curl -X POST http://127.0.0.1:8000/api/users/ \
    -H "Content-Type: application/json" \
    -d '{"email": "user@example.com", "name": "John Doe", "mobile_number": "1234567890"}'
    ```

2. **Get User Details:**

    ```bash
    curl http://127.0.0.1:8000/api/users/1/
    ```

3. **Add an Expense:**

    ```bash
    curl -X POST http://127.0.0.1:8000/api/expenses/ \
    -H "Content-Type: application/json" \
    -d '{
        "user": 1,
        "description": "Dinner",
        "amount": 50.00,
        "split_type": "equal",
        "split_details": {
            "user_ids": [1, 2, 3],
            "amounts": [16.67, 16.67, 16.66]
        }
    }'
    ```

4. **Get All Expenses for a User:**

    ```bash
    curl http://127.0.0.1:8000/api/users/1/expenses/
    ```

5. **Get All Expenses:**

    ```bash
    curl http://127.0.0.1:8000/api/expenses/overall/
    ```

## Running Tests

To run the tests, use the following command:

```bash
python3 manage.py test
