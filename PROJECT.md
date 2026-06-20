# CarbonTracker AI - Project Documentation

## Project Overview

**CarbonTracker AI** is an AI-powered web application focused on sustainability and climate action. It helps users calculate, track, predict, and reduce their personal carbon footprint through AI-generated recommendations, sustainability education, carbon analytics, and goal tracking.

## UN Sustainable Development Goals (SDGs) Alignment

- **SDG 11**: Sustainable Cities and Communities
- **SDG 12**: Responsible Consumption and Production
- **SDG 13**: Climate Action

## Technology Stack

### Frontend
- **Framework**: Next.js 14 (React 18)
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **HTTP Client**: Axios
- **State Management**: React Context API / Zustand

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: bcrypt

### AI/ML Stack
- **LLM**: IBM Granite (via watsonx.ai) - Primary
- **Alternative**: Llama 3 (via Ollama) - Fallback
- **AI Framework**: LangChain
- **Vector Database**: ChromaDB
- **RAG Architecture**: LangChain + ChromaDB
- **Agentic AI**: LangChain Agents
- **ML Libraries**: Pandas, NumPy, Scikit-Learn
- **OCR**: Tesseract / pytesseract

### IBM Tools Integration
- **IBM watsonx.ai**: For Granite LLM access
- **IBM Watson Discovery**: Optional for enhanced document search
- **IBM Cloud Object Storage**: Optional for document storage

### DevOps
- **Containerization**: Docker & Docker Compose
- **Version Control**: Git
- **Environment Management**: 
  - Python: venv (virtual environment)
  - Node.js: npm (local node_modules)

## Project Structure

```
carbontracker-ai/
├── backend/                          # FastAPI Backend
│   ├── venv/                        # Python virtual environment (isolated)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI application entry
│   │   ├── api/                     # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py             # Authentication endpoints
│   │   │   ├── users.py            # User management
│   │   │   ├── carbon.py           # Carbon calculator
│   │   │   ├── analytics.py        # Analytics endpoints
│   │   │   ├── chat.py             # AI chatbot
│   │   │   ├── recommendations.py  # Recommendations
│   │   │   ├── predictions.py      # ML predictions
│   │   │   ├── documents.py        # Document upload/OCR
│   │   │   └── admin.py            # Admin panel
│   │   ├── models/                  # Database models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── carbon_entry.py
│   │   │   ├── recommendation.py
│   │   │   └── goal.py
│   │   ├── schemas/                 # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── carbon.py
│   │   │   └── auth.py
│   │   ├── services/                # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── carbon_calculator.py
│   │   │   ├── analytics_service.py
│   │   │   └── ocr_service.py
│   │   ├── ai/                      # AI components
│   │   │   ├── __init__.py
│   │   │   ├── llm_config.py       # IBM Granite/Llama config
│   │   │   ├── rag_engine.py       # RAG implementation
│   │   │   ├── agents/             # AI Agents
│   │   │   │   ├── __init__.py
│   │   │   │   ├── carbon_agent.py
│   │   │   │   ├── recommendation_agent.py
│   │   │   │   ├── education_agent.py
│   │   │   │   └── goal_tracking_agent.py
│   │   │   ├── chatbot.py          # Chatbot logic
│   │   │   └── vector_store.py     # ChromaDB integration
│   │   ├── ml/                      # Machine Learning
│   │   │   ├── __init__.py
│   │   │   ├── prediction_model.py
│   │   │   ├── train.py
│   │   │   └── models/             # Saved ML models
│   │   ├── core/                    # Core configuration
│   │   │   ├── __init__.py
│   │   │   ├── config.py           # Settings
│   │   │   ├── security.py         # JWT & auth
│   │   │   └── database.py         # DB connection
│   │   └── utils/                   # Utilities
│   │       ├── __init__.py
│   │       └── emission_factors.py
│   ├── alembic/                     # Database migrations
│   ├── tests/                       # Backend tests
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment template
│   └── README.md
│
├── frontend/                         # Next.js Frontend
│   ├── node_modules/                # NPM packages (isolated)
│   ├── public/                      # Static assets
│   ├── src/
│   │   ├── app/                     # Next.js 14 App Router
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx            # Home page
│   │   │   ├── login/
│   │   │   ├── register/
│   │   │   ├── dashboard/
│   │   │   ├── calculator/
│   │   │   ├── analytics/
│   │   │   ├── chat/
│   │   │   ├── recommendations/
│   │   │   ├── profile/
│   │   │   └── admin/
│   │   ├── components/              # React components
│   │   │   ├── ui/                 # Reusable UI components
│   │   │   ├── charts/             # Chart components
│   │   │   ├── forms/              # Form components
│   │   │   └── layout/             # Layout components
│   │   ├── services/                # API services
│   │   │   ├── api.ts              # Axios config
│   │   │   ├── auth.service.ts
│   │   │   ├── carbon.service.ts
│   │   │   └── chat.service.ts
│   │   ├── hooks/                   # Custom React hooks
│   │   ├── context/                 # React Context
│   │   ├── utils/                   # Utility functions
│   │   └── types/                   # TypeScript types
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── next.config.js
│   ├── .env.local.example
│   └── README.md
│
├── data/                             # Data files
│   ├── sustainability_docs/         # RAG knowledge base
│   ├── sample_datasets/             # Sample data
│   └── emission_factors.json        # Carbon emission factors
│
├── docs/                             # Documentation
│   ├── API.md                       # API documentation
│   ├── INSTALLATION.md              # Setup guide
│   ├── DEPLOYMENT.md                # Deployment guide
│   ├── DATABASE_SCHEMA.md           # Database design
│   ├── AI_ARCHITECTURE.md           # AI system design
│   └── MOM.md                       # Minutes of Meeting
│
├── docker-compose.yml               # Docker services
├── .gitignore
├── README.md                        # Main README
└── PROJECT.md                       # This file
```

## Core Features

### 1. User Profile Management
- User registration and authentication
- Profile information (name, age, location, household size)
- Sustainability goals setting
- Profile editing

### 2. Carbon Footprint Calculator
**Input Parameters:**
- Monthly electricity usage (kWh)
- Transportation data (car, bike, public transport, flights)
- Food preferences (vegetarian, non-vegetarian, vegan)
- Water consumption

**Output:**
- Monthly CO₂ emissions
- Annual CO₂ emissions
- Sustainability score (0-100)
- Category-wise breakdown

### 3. Carbon Analytics Dashboard
**Visualizations:**
- Total carbon footprint (current month/year)
- Monthly trend charts
- Emission breakdown by category (pie/bar charts)
- Sustainability score gauge
- Reduction progress over time
- Comparison with average user

### 4. AI Sustainability Coach (Chatbot)
**Powered by:** IBM Granite (via watsonx.ai) or Llama 3
**Capabilities:**
- Answer sustainability questions
- Explain climate concepts
- Suggest eco-friendly alternatives
- Generate personalized reduction plans
- Provide educational content

### 5. RAG Knowledge Base
**Vector Database:** ChromaDB
**Data Sources:**
- UN SDG resources
- Climate change reports (IPCC)
- Renewable energy articles
- Government environmental guidelines
- EPA sustainability data

**Functionality:**
- Semantic search over sustainability documents
- Context-aware responses
- Citation of sources

### 6. Agentic AI System
**Four Specialized Agents:**

**A. Carbon Calculation Agent**
- Calculates emissions from user input
- Validates data
- Provides breakdown analysis

**B. Recommendation Agent**
- Generates personalized recommendations
- Estimates CO₂ savings
- Prioritizes high-impact actions

**C. Education Agent**
- Explains climate concepts
- Provides learning resources
- Answers "why" questions

**D. Goal Tracking Agent**
- Monitors user goals
- Tracks progress
- Sends reminders and encouragement

### 7. AI Recommendation Engine
**Recommendation Types:**
- Transportation alternatives
- Energy efficiency tips
- Dietary changes
- Waste reduction strategies
- Renewable energy adoption

**Features:**
- Personalized based on user profile
- Estimated CO₂ savings per recommendation
- Difficulty level (easy, medium, hard)
- Implementation timeline

### 8. Carbon Footprint Prediction
**ML Model:** Time series forecasting (ARIMA/Prophet/LSTM)
**Predictions:**
- Next 6 months carbon emissions
- Trend analysis
- Goal achievement probability
- Impact of recommendations

### 9. Document Upload & OCR
**Supported Documents:**
- Electricity bills
- Fuel receipts
- Travel tickets

**Process:**
- Upload document (PDF/Image)
- OCR extraction (Tesseract)
- Data parsing
- Automatic entry creation

### 10. Admin Panel
**Admin Capabilities:**
- User management (view, edit, delete)
- System analytics (total users, emissions)
- Knowledge base management
- Content moderation
- System configuration

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    location VARCHAR(255),
    household_size INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE
);
```

### User Profiles Table
```sql
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    food_preference VARCHAR(50),
    transportation_mode VARCHAR(50),
    sustainability_goal TEXT,
    target_reduction_percentage DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Carbon Entries Table
```sql
CREATE TABLE carbon_entries (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    entry_date DATE NOT NULL,
    electricity_kwh DECIMAL(10,2),
    car_km DECIMAL(10,2),
    bike_km DECIMAL(10,2),
    public_transport_km DECIMAL(10,2),
    flight_km DECIMAL(10,2),
    water_liters DECIMAL(10,2),
    food_type VARCHAR(50),
    total_co2_kg DECIMAL(10,2),
    sustainability_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Recommendations Table
```sql
CREATE TABLE recommendations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    recommendation_text TEXT NOT NULL,
    category VARCHAR(100),
    estimated_co2_savings DECIMAL(10,2),
    difficulty_level VARCHAR(20),
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
```

### Goals Table
```sql
CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    goal_description TEXT NOT NULL,
    target_date DATE,
    target_reduction_kg DECIMAL(10,2),
    current_progress DECIMAL(5,2) DEFAULT 0,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Chat History Table
```sql
CREATE TABLE chat_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    response TEXT NOT NULL,
    agent_used VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh JWT token
- `POST /api/auth/logout` - User logout

### User Management
- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update user profile
- `DELETE /api/users/me` - Delete user account

### Carbon Calculator
- `POST /api/carbon/calculate` - Calculate carbon footprint
- `GET /api/carbon/entries` - Get user's carbon entries
- `GET /api/carbon/entries/{id}` - Get specific entry
- `DELETE /api/carbon/entries/{id}` - Delete entry

### Analytics
- `GET /api/analytics/summary` - Get carbon summary
- `GET /api/analytics/trends` - Get monthly trends
- `GET /api/analytics/breakdown` - Get category breakdown
- `GET /api/analytics/score` - Get sustainability score

### AI Chat
- `POST /api/chat/message` - Send message to AI
- `GET /api/chat/history` - Get chat history
- `DELETE /api/chat/history` - Clear chat history

### Recommendations
- `GET /api/recommendations` - Get personalized recommendations
- `POST /api/recommendations/{id}/complete` - Mark as completed
- `GET /api/recommendations/impact` - Get total impact

### Predictions
- `GET /api/predictions/forecast` - Get 6-month forecast
- `GET /api/predictions/goal-probability` - Goal achievement probability

### Documents
- `POST /api/documents/upload` - Upload document
- `GET /api/documents` - List uploaded documents
- `DELETE /api/documents/{id}` - Delete document

### Admin
- `GET /api/admin/users` - List all users
- `GET /api/admin/analytics` - System-wide analytics
- `PUT /api/admin/users/{id}` - Update user
- `DELETE /api/admin/users/{id}` - Delete user

## Environment Variables

### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/carbontracker

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# IBM watsonx.ai
IBM_WATSONX_API_KEY=your-api-key
IBM_WATSONX_PROJECT_ID=your-project-id
IBM_WATSONX_URL=https://us-south.ml.cloud.ibm.com

# ChromaDB
CHROMA_HOST=localhost
CHROMA_PORT=8000

# OCR
TESSERACT_PATH=/usr/bin/tesseract

# CORS
CORS_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=CarbonTracker AI
```

## Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15
- Docker & Docker Compose
- Git

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

### Database Setup
```bash
docker-compose up -d postgres chromadb
```

### Running the Application
```bash
# Backend
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload

# Frontend
cd frontend
npm run dev
```

## Deployment

### Docker Deployment
```bash
docker-compose up -d
```

### Cloud Deployment Options
- **Frontend**: Vercel, Netlify
- **Backend**: Heroku, Railway, AWS EC2
- **Database**: AWS RDS, Azure Database, Heroku Postgres

## Testing Strategy

### Backend Tests
- Unit tests for services
- Integration tests for APIs
- AI agent tests

### Frontend Tests
- Component tests (Jest + React Testing Library)
- E2E tests (Playwright)

## Security Considerations

- JWT-based authentication
- Password hashing (bcrypt)
- CORS configuration
- Input validation
- SQL injection prevention (SQLAlchemy ORM)
- Rate limiting
- HTTPS in production

## Performance Optimization

- Database indexing
- API response caching
- Lazy loading in frontend
- Image optimization
- Code splitting
- CDN for static assets

## Future Enhancements

- Mobile app (React Native)
- Social features (community challenges)
- Gamification (badges, leaderboards)
- Integration with smart home devices
- Carbon offset marketplace
- Multi-language support

## License

MIT License

## Contributors

- Project Lead: [Your Name]
- Development Team: [Team Members]

## Contact

For questions or support, contact: [email@example.com]

---

**Last Updated**: June 20, 2026
**Version**: 1.0.0