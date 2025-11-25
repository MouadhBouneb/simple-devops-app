# Sample DevOps Project

A sample DevOps project demonstrating CI/CD pipelines with GitHub Actions, Docker, and automated testing.

## 🚀 Features





- **Flask REST API** - Simple Python web application
- **GitHub Actions CI/CD** - Automated testing, building, and deployment
- **Docker Support** - Containerized application
- **Automated Testing** - Unit tests with pytest
- **Code Quality** - Linting with flake8
- **Health Checks** - Built-in health monitoring endpoints

## 📋 Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)
- Git

## 🛠️ Installation

### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd simple-devops-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Docker

1. Build the Docker image:
```bash
docker build -t sample-devops-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 sample-devops-app
```

## 🧪 Testing

Run tests with pytest:
```bash
pytest tests/ -v
```

Run tests with coverage:
```bash
pytest tests/ -v --cov=app --cov-report=html
```

## 📡 API Endpoints

- `GET /` - Home endpoint with app information
- `GET /health` - Health check endpoint
- `GET /api/users` - Get all users
- `POST /api/users` - Create a new user
- `GET /api/users/<id>` - Get user by ID

### Example Requests

```bash
# Get all users
curl http://localhost:5000/api/users

# Create a user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Health check
curl http://localhost:5000/health
```

## 🔄 CI/CD Pipeline

### CI Pipeline (`.github/workflows/ci.yml`)

The CI pipeline runs on every push and pull request:

1. **Test Job**
   - Checks out code
   - Sets up Python environment
   - Installs dependencies
   - Runs linter (flake8)
   - Runs unit tests with coverage
   - Uploads coverage to Codecov

2. **Build Job**
   - Builds Docker image
   - Tests the Docker image

### CD Pipeline (`.github/workflows/cd.yml`)

The CD pipeline runs on pushes to main branch:

1. **Build and Push**
   - Builds Docker image
   - Pushes to GitHub Container Registry (ghcr.io)
   - Tags images with version, branch, and SHA

2. **Deploy**
   - Deploys to staging environment
   - Runs smoke tests

## 📁 Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── .gitignore           # Git ignore file
├── tests/               # Test files
│   └── test_app.py      # Unit tests
├── .github/
│   └── workflows/       # GitHub Actions workflows
│       ├── ci.yml       # CI pipeline
│       └── cd.yml       # CD pipeline
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

- `APP_VERSION` - Application version (default: 1.0.0)
- `ENVIRONMENT` - Environment name (default: development)
- `PORT` - Server port (default: 5000)

### GitHub Actions Secrets

For the CD pipeline to work, ensure you have:
- `GITHUB_TOKEN` - Automatically provided by GitHub Actions

## 🚢 Deployment

The CD pipeline automatically:
1. Builds and pushes Docker images to GitHub Container Registry
2. Deploys to staging on pushes to main branch

To deploy manually:
```bash
# Pull the image
docker pull ghcr.io/<username>/<repo-name>:latest

# Run the container
docker run -p 5000:5000 ghcr.io/<username>/<repo-name>:latest
```

## 📝 Contributing

1. Create a feature branch
2. Make your changes
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This is a sample project for educational purposes.

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Documentation](https://docs.pytest.org/)

