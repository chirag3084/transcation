# Transaction Management System

A comprehensive web application built with Django for managing financial transactions with data visualization, REST API support, and user authentication.

## 📋 Features

- **User Authentication**
  - User registration and login
  - Password reset functionality
  - Secure authentication with Django's built-in auth system

- **Transaction Management**
  - Add new transactions with date, amount, category, and description
  - View all transactions in a dashboard
  - Filter transactions by date range
  - Export transaction data as JSON

- **Data Visualization**
  - Interactive transaction graphs using Plotly
  - Line charts for transaction analysis
  - Visual representation of spending patterns

- **REST API**
  - RESTful API endpoints using Django REST Framework
  - FastAPI integration for additional endpoints
  - JSON export capabilities

- **Data Export**
  - Export transactions as JSON
  - CSV file generation support
  - Programmatic data access

## 🛠️ Tech Stack

### Backend
- **Django 5.1** - Main web framework
- **Django REST Framework 3.16.0** - REST API
- **FastAPI 0.115.6** - Alternative API framework
- **PostgreSQL** - Primary database (MySQL and SQLite support available)

### Data Processing & Visualization
- **Pandas 2.2.3** - Data manipulation
- **Matplotlib 3.10.3** - Data visualization
- **Plotly** - Interactive charts
- **NumPy 2.2.4** - Numerical computing

### Deployment & Static Files
- **Gunicorn 23.0.0** - WSGI HTTP Server
- **WhiteNoise 6.9.0** - Static file serving
- **Uvicorn 0.33.0** - ASGI server

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL (or MySQL/SQLite)
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/chirag3084/transcation.git
   cd transcation
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your-secret-key-here
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432
   
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-email-password
   ```

5. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

## 🚀 Usage

### Running the Development Server

**Django Development Server:**
```bash
python manage.py runserver
```
Access the application at `http://localhost:8000`

**FastAPI Server:**
```bash
uvicorn home.api_fastapi:app --reload
```
Access FastAPI at `http://localhost:8000`

### Accessing the Application

- **Home Page:** `http://localhost:8000/`
- **Dashboard:** `http://localhost:8000/dashboard.html/`
- **Login:** `http://localhost:8000/login.html/`
- **Register:** `http://localhost:8000/register.html/`
- **Admin Panel:** `http://localhost:8000/admin/`

## 📡 API Endpoints

### Django REST Framework Endpoints

- **List all transactions:** `GET /api/transactions/`
- **Create transaction:** `POST /api/transactions/`
- **Get transaction by ID:** `GET /api/transactions/{id}/`
- **Update transaction:** `PUT /api/transactions/{id}/`
- **Delete transaction:** `DELETE /api/transactions/{id}/`

### Custom JSON Endpoints

- **Export all data as JSON:** `GET /export-json/`
- **Export data by ID:** `GET /export-json/{id}/`

### FastAPI Endpoints

- **Root endpoint:** `GET /`

## 💾 Database Configuration

The application supports multiple database backends. Configure in `core/settings.py`:

**PostgreSQL (Default):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

**SQLite (Alternative):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 📊 Data Model

### Transaction Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Auto-generated primary key |
| date_t | DateField | Transaction date |
| amount_t | IntegerField | Transaction amount |
| category_t | CharField | Transaction category (max 100 chars) |
| description_t | CharField | Transaction description (max 80 chars) |

## 🔧 Development

### Project Structure

```
transcation/
├── core/               # Project settings and configuration
│   ├── settings.py    # Django settings
│   ├── urls.py        # Main URL configuration
│   └── wsgi.py        # WSGI configuration
├── home/              # Main application
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── urls.py        # App URL patterns
│   ├── serializers.py # DRF serializers
│   └── api_fastapi.py # FastAPI endpoints
├── templates/         # HTML templates
├── staticfiles_build/ # Static files for production
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

### Running Tests

```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Chirag**
- GitHub: [@chirag3084](https://github.com/chirag3084)

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- FastAPI Documentation
- Plotly for visualization capabilities
