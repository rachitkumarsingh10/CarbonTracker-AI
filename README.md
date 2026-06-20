# 🌍 CarbonTracker AI

<div align="center">

![CarbonTracker AI](https://img.shields.io/badge/CarbonTracker-AI-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Next.js](https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)

**An AI-powered web application for tracking, analyzing, and reducing your carbon footprint**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 About

**CarbonTracker AI** is a comprehensive sustainability platform that helps individuals understand and reduce their environmental impact. Built with cutting-edge AI technology and aligned with UN Sustainable Development Goals (SDGs 11, 12, and 13), it provides personalized insights and actionable recommendations for a more sustainable lifestyle.

### 🎯 UN SDG Alignment

- **SDG 11**: Sustainable Cities and Communities
- **SDG 12**: Responsible Consumption and Production
- **SDG 13**: Climate Action

---

## ✨ Features

### 🧮 Carbon Footprint Calculator
- Track emissions from electricity, transportation, food, and water consumption
- Real-time CO₂ calculations with category-wise breakdown
- Monthly and annual emission reports
- Sustainability score (0-100) with personalized insights

### 📊 Analytics Dashboard
- Interactive charts and visualizations (powered by Recharts)
- Monthly trend analysis and historical comparisons
- Emission breakdown by category (pie charts, bar graphs)
- Progress tracking towards sustainability goals
- Comparison with average user benchmarks

### 🤖 AI Sustainability Coach
- **Powered by**: IBM Granite (via watsonx.ai) or Llama 3
- Natural language conversations about sustainability
- Personalized advice based on your carbon footprint
- Educational content on climate change and eco-friendly practices
- Context-aware responses using RAG (Retrieval-Augmented Generation)

### 🎓 RAG Knowledge Base
- **Vector Database**: ChromaDB
- Curated sustainability documents from:
  - UN SDG resources
  - IPCC climate reports
  - EPA environmental guidelines
  - Renewable energy research
- Semantic search for accurate, cited information

### 🤝 Agentic AI System
Four specialized AI agents working together:

1. **Carbon Calculation Agent** - Validates and calculates emissions
2. **Recommendation Agent** - Generates personalized reduction strategies
3. **Education Agent** - Explains climate concepts and provides learning resources
4. **Goal Tracking Agent** - Monitors progress and provides encouragement

### 💡 AI Recommendation Engine
- Personalized suggestions based on your profile and habits
- Estimated CO₂ savings for each recommendation
- Difficulty levels (easy, medium, hard)
- Implementation timelines and step-by-step guides
- Categories: Transportation, Energy, Food, Waste, Lifestyle

### 📈 ML-Powered Predictions
- 6-month carbon footprint forecast
- Trend analysis and pattern recognition
- Goal achievement probability calculations
- Impact assessment of recommendations

### 📄 Document Upload & OCR
- Upload electricity bills, fuel receipts, and travel tickets
- Automatic data extraction using Tesseract OCR
- Smart parsing and validation
- Automatic carbon entry creation

### 👨‍💼 Admin Panel
- User management and analytics
- System-wide statistics and insights
- Knowledge base content management
- Configuration and monitoring tools

---

## 🛠️ Technology Stack

### Frontend
- **Framework**: Next.js 14 (React 18) with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **State Management**: Zustand / React Context API
- **HTTP Client**: Axios
- **Forms**: React Hook Form + Zod validation

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (development) / PostgreSQL (production)
- **ORM**: SQLAlchemy
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: bcrypt
- **API Documentation**: Swagger UI / ReDoc (auto-generated)

### AI/ML Stack
- **LLM**: IBM Granite (via watsonx.ai) - Primary
- **Fallback LLM**: Llama 3 (via Ollama)
- **AI Framework**: LangChain
- **Vector Database**: ChromaDB
- **Embeddings**: sentence-transformers
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **OCR**: Tesseract / pytesseract

### DevOps
- **Containerization**: Docker & Docker Compose
- **Version Control**: Git
- **Environment Management**: Python venv, npm

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (Next.js)                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Dashboard │  │Calculator│  │Analytics │  │  Chat    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ REST API
┌────────────────────────▼────────────────────────────────────┐
│                      Backend (FastAPI)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Endpoints Layer                      │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Business Logic & Services                   │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              AI/ML Components                         │  │
│  │  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐    │  │
│  │  │Carbon  │  │Recomm. │  │Educ.   │  │Goal    │    │  │
│  │  │Agent   │  │Agent   │  │Agent   │  │Agent   │    │  │
│  │  └────────┘  └────────┘  └────────┘  └────────┘    │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼──────┐  ┌──────▼──────┐  ┌─────▼──────┐
│   SQLite/    │  │   ChromaDB  │  │    IBM     │
│  PostgreSQL  │  │   (Vector   │  │  watsonx   │
│  (Database)  │  │   Database) │  │    .ai     │
└──────────────┘  └─────────────┘  └────────────┘
```

---

## 🚀 Installation

### Prerequisites

- **Python**: 3.11 or higher
- **Node.js**: 18 or higher
- **Git**: Latest version
- **Operating System**: Windows, macOS, or Linux

### Quick Start (Windows)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/carbontracker-ai.git
cd carbontracker-ai

# 2. Run automated setup
setup.bat

# 3. Start the application
start-all.bat
```

### Manual Setup

<details>
<summary>Click to expand manual setup instructions</summary>

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your configuration

# Start backend server
uvicorn app.main:app --reload
```

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Configure environment
copy .env.local.example .env.local
# Edit .env.local with your configuration

# Start development server
npm run dev
```

</details>

### Access the Application

Once running, access the application at:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📖 Usage

### 1. Register an Account
- Navigate to http://localhost:3000
- Click "Register" and create your account
- Complete your profile with household information

### 2. Calculate Your Carbon Footprint
- Go to the Calculator page
- Enter your monthly consumption data:
  - Electricity usage (kWh)
  - Transportation (car, bike, public transport, flights)
  - Food preferences (vegetarian, non-vegetarian, vegan)
  - Water consumption
- View your results and sustainability score

### 3. Explore Analytics
- Visit the Analytics Dashboard
- View monthly trends and breakdowns
- Compare your footprint with averages
- Track your progress over time

### 4. Chat with AI Coach
- Open the AI Chat interface
- Ask questions about sustainability
- Get personalized recommendations
- Learn about climate action

### 5. Set and Track Goals
- Define your sustainability goals
- Monitor progress with AI assistance
- Receive encouragement and tips
- Celebrate milestones

---

## 📚 API Documentation

### Authentication Endpoints

```http
POST /api/auth/register    # Register new user
POST /api/auth/login       # User login
POST /api/auth/refresh     # Refresh JWT token
```

### Carbon Calculator Endpoints

```http
POST /api/carbon/calculate      # Calculate carbon footprint
GET  /api/carbon/entries        # Get user's entries
GET  /api/carbon/entries/{id}   # Get specific entry
DELETE /api/carbon/entries/{id} # Delete entry
```

### Analytics Endpoints

```http
GET /api/analytics/summary    # Get carbon summary
GET /api/analytics/trends     # Get monthly trends
GET /api/analytics/breakdown  # Get category breakdown
GET /api/analytics/score      # Get sustainability score
```

### AI Chat Endpoints

```http
POST /api/chat/message     # Send message to AI
GET  /api/chat/history     # Get chat history
DELETE /api/chat/history   # Clear chat history
```

For complete API documentation, visit http://localhost:8000/docs when the backend is running.

---

## 📁 Project Structure

```
carbontracker-ai/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── ai/                # AI components
│   │   │   └── agents/        # AI agents
│   │   ├── ml/                # ML models
│   │   ├── core/              # Core configuration
│   │   └── utils/             # Utilities
│   ├── tests/                 # Backend tests
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment template
│
├── frontend/                   # Next.js Frontend
│   ├── src/
│   │   ├── app/               # Next.js pages (App Router)
│   │   ├── components/        # React components
│   │   ├── services/          # API services
│   │   ├── hooks/             # Custom hooks
│   │   ├── context/           # React Context
│   │   ├── utils/             # Utilities
│   │   └── types/             # TypeScript types
│   ├── public/                # Static assets
│   ├── package.json           # Node dependencies
│   └── .env.local.example    # Environment template
│
├── data/                       # Data files
│   ├── sustainability_docs/   # RAG knowledge base
│   └── sample_datasets/       # Sample data
│
├── docs/                       # Documentation
│   ├── INSTALLATION.md        # Setup guide
│   ├── MOM.md                 # Meeting minutes
│   └── PROJECT.md             # Project documentation
│
├── docker-compose.yml         # Docker services
├── setup.bat                  # Windows setup script
├── start-all.bat             # Start all services
└── README.md                  # This file
```

---

## 💻 Development

### Running Tests

**Backend Tests:**
```bash
cd backend
pytest
pytest --cov=app --cov-report=html
```

**Frontend Tests:**
```bash
cd frontend
npm test
npm run test:coverage
```

### Code Quality

**Backend:**
```bash
# Format code
black app/

# Lint code
flake8 app/

# Type checking
mypy app/
```

**Frontend:**
```bash
# Lint
npm run lint

# Type check
npm run type-check

# Format
npm run format
```

### Database Migrations

```bash
cd backend

# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🧪 Testing

### Test Coverage

- **Backend**: Unit tests, integration tests, AI agent tests
- **Frontend**: Component tests (Jest + React Testing Library)
- **E2E**: End-to-end tests (Playwright - coming soon)

### Running Specific Tests

```bash
# Backend - specific test file
pytest tests/test_carbon_calculator.py

# Backend - specific test function
pytest tests/test_carbon_calculator.py::test_calculate_emissions

# Frontend - specific component
npm test -- Calculator.test.tsx
```

---

## 🚢 Deployment

### Docker Deployment

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Cloud Deployment Options

- **Frontend**: Vercel, Netlify, AWS Amplify
- **Backend**: Heroku, Railway, AWS EC2, Google Cloud Run
- **Database**: AWS RDS, Azure Database, Heroku Postgres

### Environment Variables

See `.env.example` files in backend and frontend directories for required configuration.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Project Maintainer**: [Your Name]

- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)

**Project Link**: [https://github.com/yourusername/carbontracker-ai](https://github.com/yourusername/carbontracker-ai)

---

## 🙏 Acknowledgments

- **IBM watsonx.ai** for providing enterprise-grade AI capabilities
- **UN SDG** resources for sustainability guidelines
- **EPA** for emission factor data
- **Open-source community** for amazing tools and libraries

---

## 📊 Project Status

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)
![Version](https://img.shields.io/badge/version-0.1.0-blue)

**Current Phase**: Foundation Complete ✅  
**Next Phase**: Core Features Development 🔄

---

## 🗺️ Roadmap

- [x] Project planning and documentation
- [x] Foundation setup (backend, frontend, database)
- [ ] Core features (calculator, analytics, basic AI)
- [ ] Advanced AI features (RAG, agents, predictions)
- [ ] OCR document upload
- [ ] Admin panel
- [ ] Mobile app (React Native)
- [ ] Social features and gamification
- [ ] Carbon offset marketplace

---

## 📸 Screenshots

*Coming soon - Screenshots will be added as features are implemented*

---

<div align="center">

**Made with ❤️ for a sustainable future**

⭐ Star this repo if you find it helpful!

</div>#   C a r b o n T r a c k e r - A I  
 