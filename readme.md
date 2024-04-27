![Example Image](images/blockchain.png)

# Django Voting System

This Django project implements an online voting system where users can register as voters, cast votes for presidential candidates, and view the election results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/django-voting-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd django-voting-system
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # Activate the virtual environment (Unix/Linux)
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Rename `.env.example` to `.env` and configure environment variables:
    ```bash
    mv .env.example .env
    ```

2. Update database settings in `voting_system/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

## Usage

1. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

2. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

4. Access the application in your web browser at `http://127.0.0.1:8000/`

## Features

- User registration and authentication
- Voting system for presidential candidates
- Admin dashboard to manage voters and election results

## Directory Structure

django-voting-system/
│
├── voting/ # Main Django app
│ ├── migrations/ # Database migrations
│ ├── static/ # Static files (CSS, JavaScript)
│ ├── templates/ # HTML templates
│ ├── init.py
│ ├── admin.py
│ ├── models.py # Database models (e.g., Voter, Vote)
│ ├── urls.py # URL patterns
│ └── views.py # View functions
│
├── voting_system/ # Django project settings
│ ├── init.py
│ ├── settings.py # Project settings
│ ├── urls.py # Project-level URL configurations
│ └── wsgi.py # WSGI configuration for deployment
│
├── .gitignore # Git ignore file
├── manage.py # Django project management script
├── README.md # Project README (this file)
└── requirements.txt # Python dependencies


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
