# CarbonTracker AI - Backend

FastAPI backend with AI/ML capabilities for carbon footprint tracking and analysis.

## 🛠️ Technology Stack

- **Framework**: FastAPI 0.109.0
- **Database**: PostgreSQL 15 + SQLAlchemy
- **AI/ML**: 
  - IBM watsonx.ai (Granite model)
  - LangChain + ChromaDB (RAG)
  - Scikit-learn (ML predictions)
- **Authentication**: JWT
- **OCR**: Tesseract

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/              # API endpoints
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── ai/              # AI components
│   │   └── agents/      # AI agents
│   ├── ml/              # ML models
│   ├── core/            # Core config
│   └── utils/           # Utilities
├── alembic/             # Database migrations
├── tests/               # Tests
├── requirements.txt     # Dependencies
└── .env.example        # Environment template
```

## 🚀 Setup Instructions

### 1. Create Virtual Environment

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# - Database credentials
# - IBM watsonx.ai API key
# - Secret keys
```

### 4. Start Database Services

```bash
# From project root
docker-compose up -d postgres chromadb
```

### 5. Run Database Migrations

```bash
# Initialize Alembic (first time only)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

### 6. Start Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔑 Environment Variables

See `.env.example` for all available configuration options.

### Required Variables:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `IBM_WATSONX_API_KEY`: IBM watsonx.ai API key (or use Ollama)

### Optional Variables:
- `OLLAMA_BASE_URL`: Ollama server URL (fallback LLM)
- `CHROMA_HOST`: ChromaDB host
- `TESSERACT_PATH`: Tesseract OCR path

## 📊 Database Schema

### Tables:
- `users` - User accounts
- `user_profiles` - User profile details
- `carbon_entries` - Carbon footprint records
- `recommendations` - AI recommendations
- `goals` - User sustainability goals
- `chat_history` - AI chat conversations

## 🤖 AI Components

### LLM Configuration
1. **Primary**: IBM Granite (via watsonx.ai)
2. **Fallback**: Llama 3 (via Ollama)

### AI Agents
1. **Carbon Calculation Agent** - Calculates emissions
2. **Recommendation Agent** - Generates suggestions
3. **Education Agent** - Explains concepts
4. **Goal Tracking Agent** - Monitors progress

### RAG System
- **Vector DB**: ChromaDB
- **Embeddings**: sentence-transformers
- **Documents**: Sustainability knowledge base

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_carbon_calculator.py
```

## 📝 API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Main Endpoints:

**Authentication**
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login

**Carbon Calculator**
- `POST /api/carbon/calculate` - Calculate footprint
- `GET /api/carbon/entries` - Get entries

**Analytics**
- `GET /api/analytics/summary` - Get summary
- `GET /api/analytics/trends` - Get trends

**AI Chat**
- `POST /api/chat/message` - Chat with AI
- `GET /api/chat/history` - Get history

**Recommendations**
- `GET /api/recommendations` - Get recommendations

**Predictions**
- `GET /api/predictions/forecast` - Get forecast

## 🔧 Development

### Code Quality

```bash
# Format code
black app/

# Lint code
flake8 app/

# Type checking
mypy app/
```

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Check connection
psql -h localhost -U carbontracker -d carbontracker_db
```

### ChromaDB Issues
```bash
# Check if ChromaDB is running
curl http://localhost:8000/api/v1/heartbeat

# Restart ChromaDB
docker-compose restart chromadb
```

### Import Errors
```bash
# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📦 Dependencies

See `requirements.txt` for complete list.

### Key Dependencies:
- FastAPI - Web framework
- SQLAlchemy - ORM
- LangChain - AI framework
- ChromaDB - Vector database
- Scikit-learn - ML library
- Pytesseract - OCR

## 🚀 Deployment

### Production Checklist:
- [ ] Set `DEBUG=false` in .env
- [ ] Use strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Set up HTTPS
- [ ] Configure CORS properly
- [ ] Set up logging
- [ ] Configure rate limiting
- [ ] Set up monitoring

### Docker Deployment:
```bash
# Build image
docker build -t carbontracker-backend .

# Run container
docker run -p 8000:8000 carbontracker-backend
```

## 📄 License

MIT License

## 🤝 Contributing

1. Create feature branch
2. Make changes
3. Run tests
4. Submit pull request

## 📧 Support

For issues or questions, please open an issue on GitHub.