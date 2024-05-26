# ToDo App

This is a Django-based ToDo application that allows users to manage their tasks efficiently. The application supports adding, deleting, updating tasks with priority levels and due dates. Users can also sort tasks by priority, search tasks by keyword, and receive warnings if a task's due date is today or tomorrow. The app includes user authentication features such as login, logout, registration, and a profile page. Task management features are only accessible to authenticated users.

## Features

- **Add Tasks**: Users can add new tasks with a priority level (Low, Medium, High) and a due date.
- **Delete Tasks**: Users can delete tasks. If a task is marked as completed, it will be automatically deleted.
- **Update Tasks**: Users can update tasks. The update button is disabled for tasks that are marked as completed.
- **Sort by Priority**: Users can sort tasks by priority (Low, Medium, High).
- **Search Tasks**: Users can search for tasks by keyword.
- **Due Date Warnings**: Users receive warnings if a task is due today or tomorrow.
- **Authentication**: Includes login, logout, registration, and profile pages. Users must be logged in to view tasks or their profile.

## Tech Stack

- **Backend**: Django
- **Database**: MySQL
- **Frontend**: Bootstrap
- **IDE**: VS Code

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Virtualenv

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/VarunK715/todo_app.git
    cd todo_app
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Create a MySQL database.
    - Update the `DATABASES` setting in `todo_app/settings.py` with your MySQL database credentials.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
