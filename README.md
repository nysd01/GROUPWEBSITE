
# Group Website Project

Welcome to the **Group Website Project**, a full-stack web application built with Django for the backend. This project provides various features like user authentication, product management, and testimonial submissions, with a clean and functional interface.

## Key Features

- **User Authentication**: Secure user login, registration, and management.
- **Testimonials**: Users can leave feedback and view testimonials.
- **Product Management**: Manage products, cart functionality, and payments.
- **Real-time Chat**: Chat feature integrated for user interaction.

## Quick Start

This guide will help you set up and run the project on your local machine. It's easy to follow, even if you're not familiar with Django.

### Prerequisites

Before starting, ensure you have the following installed on your machine:

- Python 3.9+
- Pip (Python package installer)
- Git (to clone the repository)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd GROUPWEBSITE/backend
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 6. Run the Server

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` in your browser to see the application running locally.

## Project Structure

```
GROUPWEBSITE/
├── backend/
│   ├── myfirst/              # Django core settings and configuration
│   ├── nysdapp/              # Main application handling views, models, and static files
│   ├── staticfiles/          # Collected static files
│   ├── manage.py             # Django management script
│   ├── requirements.txt      # Python dependencies
│   └── build_files.sh        # Shell script for setting up the environment
├── .gitignore
└── .vercel/
```

## Build and Deploy

This project is ready for deployment on **Vercel**. Make sure you have:

1. A `vercel.json` file for configuration.
2. Use `build_files.sh` to set up the environment for deployment.

For deployment:
```bash
bash build_files.sh
```

## Contributing

We welcome contributions! Please feel free to fork the project, create a new branch, and submit a pull request. Contributions should be well-documented and accompanied by tests.

## License

This project is licensed under the MIT License.
