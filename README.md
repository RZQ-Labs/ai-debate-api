# AI Debate Trainer Backend

This is the backend service for the AI Debate Trainer project. It is built with FastAPI, SQLAlchemy, Alembic, and Docker, and is designed to manage users, debate sessions, arguments, and integrate with LLMs (such as OpenAI and OpenRouter) and IndoBERT.

## Features
- User registration and authentication
- Debate session and argument management
- Integration with PostgreSQL and Redis
- Support for LLM providers (OpenAI, OpenRouter)
- IndoBERT model integration
- Admin interface (Adminer)
- Full Docker support with multi-architecture images
- Database migrations with Alembic

## Project Structure
```
backend/
├── alembic/                  # Database migrations
├── app/
│   ├── models/               # SQLAlchemy models
│   ├── schemas/              # Pydantic schemas
│   ├── routes/               # API routes
│   ├── deps.py               # Dependency utilities
│   └── ...
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # Docker Compose setup
├── Dockerfile                # Backend Dockerfile
├── .env                      # Environment variables
└── README.md                 # This file
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.9+

### Configuration
1. Copy `.env.example` to `.env` and fill in your secrets and configuration.
2. (Optional) Adjust `docker-compose.yml` for your architecture (see `platform:` directives).

### Build and Run (Docker)
```bash
# Build and start all services
COMPOSE_BAKE=true docker compose up --build
```

### Database Migrations
```bash
# Generate a new migration after model changes
alembic revision --autogenerate -m "Your migration message"
# Apply migrations
alembic upgrade head
```

### Running Locally (without Docker)
You'll need to install and setup the following yourself:

1. PostgreSQL
2. Redis
3. OpenAI API key
4. OpenRouter API key
5. IndoBERT model path

After setting up the above, you can run the application:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables
See `.env.example` for all configuration options, including:
- PostgreSQL and Redis settings
- OpenAI and OpenRouter API keys
- IndoBERT model path
- n8n credentials
- Logging level

## License
MIT

---

For more information, see the source code and comments in each module.
