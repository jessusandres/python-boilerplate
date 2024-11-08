# Python Boilerplate

A modern Python boilerplate project with Flask, SQLAlchemy, and Google Cloud Functions Framework integration. This project provides a solid foundation for building scalable web applications and microservices.

## Features

- **Flask Integration**: Built on Flask for HTTP request handling
- **Google Cloud Functions Framework**: Ready for serverless deployment
- **SQLAlchemy ORM**: Database abstraction with support for multiple database engines
- **Comprehensive Logging**: Custom logging with timing decorators
- **Environment Configuration**: Environment variable management with dotenv
- **Testing Setup**: Pytest configuration with coverage reporting
- **Code Quality Tools**: Flake8 and pydocstyle configuration

## Project Structure

```
python-boilerplate/
├── src/                    # Source code
│   ├── common/             # Common utilities
│   │   ├── helpers/        # Helper functions
│   │   ├── cus_logging.py  # Custom logging setup
│   │   └── timed_logger.py # Performance timing decorator
│   ├── config/             # Configuration
│   │   └── database.py     # Database connection setup
│   ├── models/             # Data models
│   │   ├── Base.py         # SQLAlchemy base model
│   │   └── EventTypeModel.py # Example model
│   └── services/           # Business logic
│       └── app_service.py  # Core application services
├── tests/                  # Test files
│   ├── helpers/            # Test helpers
│   └── test_main.py        # Main tests
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
├── setup.cfg               # Tool configurations
├── .coveragerc             # Coverage configuration
├── log_conf.yaml           # Logging configuration
├── execute.sh              # Execution script
└── runDeploy.sh            # Deployment script
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-boilerplate.git
   cd python-boilerplate
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your configuration:
   ```
   SERVICE_NAME=your-service-name
   PROJECT_ID=your-project-id
   DB_HOST=localhost
   DB_PORT=5432
   DB_USERNAME=postgres
   DB_PASSWORD=your-password
   DB_DATABASE=your-database
   DB_DIALECT=postgresql
   DB_DRIVER=pg8000
   DB_LOGGER=FALSE
   ```

## Usage

### Local Development

Run the application locally using the Functions Framework:

```bash
functions-framework --target=main
```

Or use the provided execution script:

```bash
./execute.sh
```

### Testing

Run tests with pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src
```

### Deployment

Deploy to Google Cloud Functions using the provided script:

```bash
./runDeploy.sh
```

## Database Configuration

The project supports multiple database engines:

- **SQLite** (default for development)
- **PostgreSQL** (using pg8000 driver)
- Other SQL databases supported by SQLAlchemy

Configure the database connection in your `.env` file or environment variables.

## Logging

Logging is configured in `log_conf.yaml`. The default configuration logs to the console at INFO level.

You can use the `@timed` decorator to measure and log function execution time:

```python
from src.common import timed

@timed
def my_function():
    # Your code here
    pass
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using commitizen (`cz commit`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.