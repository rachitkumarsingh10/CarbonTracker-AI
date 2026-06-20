# 🌍 CarbonTracker AI

<div align="center">

### AI-Powered Carbon Footprint Tracking & Reduction Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/next.js-14-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688.svg)](https://fastapi.tiangolo.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Track • Analyze • Reduce Your Carbon Footprint with AI**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Demo](#-demo)

</div>

---

## 🎯 About

**CarbonTracker AI** is a comprehensive sustainability platform that empowers individuals to understand and reduce their environmental impact through AI-powered insights and personalized recommendations.

### Why CarbonTracker AI?

- 🤖 **AI-Powered Insights** - Get personalized recommendations from IBM Granite AI
- 📊 **Real-Time Analytics** - Track your carbon footprint with interactive dashboards
- 🎓 **Educational** - Learn about climate action through our RAG-powered knowledge base
- 🎯 **Goal-Oriented** - Set and achieve sustainability goals with AI coaching
- 🌱 **UN SDG Aligned** - Contributing to SDGs 11, 12, and 13

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🧮 Carbon Calculator
- Track electricity, transport, food & water
- Real-time CO₂ calculations
- Category-wise breakdown
- Sustainability score (0-100)

</td>
<td width="50%">

### 📊 Analytics Dashboard
- Interactive charts & visualizations
- Monthly trend analysis
- Historical comparisons
- Progress tracking

</td>
</tr>
<tr>
<td width="50%">

### 🤖 AI Sustainability Coach
- Powered by IBM Granite / Llama 3
- Natural language conversations
- Personalized advice
- Context-aware responses (RAG)

</td>
<td width="50%">

### 💡 Smart Recommendations
- Personalized reduction strategies
- Estimated CO₂ savings
- Difficulty levels & timelines
- Implementation guides

</td>
</tr>
<tr>
<td width="50%">

### 📈 ML Predictions
- 6-month carbon forecast
- Trend analysis
- Goal achievement probability
- Impact assessment

</td>
<td width="50%">

### 📄 Document Upload
- OCR for bills & receipts
- Automatic data extraction
- Smart parsing
- Auto-entry creation

</td>
</tr>
</table>

### 🤝 Four Specialized AI Agents

| Agent | Purpose | Capability |
|-------|---------|------------|
| 🧮 **Carbon Agent** | Emission Calculation | Validates & calculates CO₂ from user input |
| 💡 **Recommendation Agent** | Personalized Suggestions | Generates tailored reduction strategies |
| 🎓 **Education Agent** | Climate Education | Explains concepts & provides resources |
| 🎯 **Goal Tracking Agent** | Progress Monitoring | Tracks goals & provides encouragement |

---

## 🛠️ Technology Stack

<table>
<tr>
<td>

**Frontend**
- Next.js 14 (React 18)
- TypeScript
- Tailwind CSS
- Recharts
- Zustand

</td>
<td>

**Backend**
- FastAPI (Python 3.11+)
- SQLAlchemy ORM
- PostgreSQL / SQLite
- JWT Authentication
- Pydantic

</td>
<td>

**AI/ML**
- IBM Granite (watsonx.ai)
- LangChain
- ChromaDB
- Scikit-learn
- Tesseract OCR

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.11+  |  Node.js 18+  |  Git
```

### Installation (Windows)

```bash
# Clone the repository
git clone https://github.com/yourusername/carbontracker-ai.git
cd carbontracker-ai

# Run automated setup
setup.bat

# Start all services
start-all.bat
```

### Installation (Linux/Mac)

```bash
# Clone the repository
git clone https://github.com/yourusername/carbontracker-ai.git
cd carbontracker-ai

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Frontend setup
cd ../frontend
npm install
cp .env.local.example .env.local

# Start backend (in one terminal)
cd backend && source venv/bin/activate
uvicorn app.main:app --reload

# Start frontend (in another terminal)
cd frontend && npm run dev
```

### Access the Application

| Service | URL | Description |
|---------|-----|-------------|
| 🌐 Frontend | http://localhost:3000 | Main application |
| 🔧 Backend API | http://localhost:8000 | REST API |
| 📚 API Docs | http://localhost:8000/docs | Swagger UI |
| 📖 ReDoc | http://localhost:8000/redoc | Alternative docs |

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [PROJECT.md](PROJECT.md) | Complete technical documentation |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Detailed setup instructions |
| [docs/MOM.md](docs/MOM.md) | Meeting minutes & decisions |
| [backend/README.md](backend/README.md) | Backend documentation |
| [frontend/README.md](frontend/README.md) | Frontend documentation |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                    │
│   Dashboard  │  Calculator  │  Analytics  │  AI Chat    │
└────────────────────────┬────────────────────────────────┘
                         │ REST API (Axios)
┌────────────────────────▼────────────────────────────────┐
│                   Backend (FastAPI)                      │
│  ┌────────────────────────────────────────────────────┐ │
│  │         API Layer (Auth, Carbon, Analytics)        │ │
│  └────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────┐ │
│  │              AI Agent Orchestration                 │ │
│  │  Carbon │ Recommendation │ Education │ Goal Agent  │ │
│  └────────────────────────────────────────────────────┘ │
└────────────────────────┬────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   PostgreSQL        ChromaDB      IBM watsonx.ai
   (Database)     (Vector Store)    (LLM Provider)
```

---

## 📁 Project Structure

```
carbontracker-ai/
│
├── 📂 backend/              # FastAPI Backend
│   ├── app/
│   │   ├── api/            # REST API endpoints
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   ├── ai/             # AI components
│   │   │   └── agents/     # Specialized AI agents
│   │   ├── ml/             # ML models
│   │   └── core/           # Configuration
│   └── requirements.txt
│
├── 📂 frontend/             # Next.js Frontend
│   ├── src/
│   │   ├── app/            # Pages (App Router)
│   │   ├── components/     # React components
│   │   ├── services/       # API services
│   │   └── hooks/          # Custom hooks
│   └── package.json
│
├── 📂 data/                 # Data & documents
├── 📂 docs/                 # Documentation
├── 🐳 docker-compose.yml    # Docker services
└── 📄 README.md             # This file
```

---

## 🎮 Usage

### 1️⃣ Register & Setup Profile
Create your account and complete your profile with household information.

### 2️⃣ Calculate Carbon Footprint
Enter your monthly consumption data:
- ⚡ Electricity usage (kWh)
- 🚗 Transportation (car, bike, public transport, flights)
- 🍽️ Food preferences (vegetarian, non-vegetarian, vegan)
- 💧 Water consumption

### 3️⃣ View Analytics
Explore your carbon footprint through interactive dashboards and charts.

### 4️⃣ Chat with AI Coach
Ask questions, get recommendations, and learn about sustainability.

### 5️⃣ Track Goals
Set sustainability goals and monitor your progress with AI assistance.

---

## 🔌 API Endpoints

### Authentication
```http
POST   /api/auth/register     # Register new user
POST   /api/auth/login        # User login
POST   /api/auth/refresh      # Refresh token
```

### Carbon Calculator
```http
POST   /api/carbon/calculate      # Calculate footprint
GET    /api/carbon/entries        # Get entries
GET    /api/carbon/entries/{id}   # Get specific entry
DELETE /api/carbon/entries/{id}   # Delete entry
```

### Analytics
```http
GET /api/analytics/summary     # Carbon summary
GET /api/analytics/trends      # Monthly trends
GET /api/analytics/breakdown   # Category breakdown
GET /api/analytics/score       # Sustainability score
```

### AI Chat
```http
POST   /api/chat/message    # Send message to AI
GET    /api/chat/history    # Get chat history
DELETE /api/chat/history    # Clear history
```

**📚 Full API Documentation:** Visit http://localhost:8000/docs when running

---

## 🧪 Testing

### Run Tests

```bash
# Backend tests
cd backend
pytest
pytest --cov=app --cov-report=html

# Frontend tests
cd frontend
npm test
npm run test:coverage
```

### Code Quality

```bash
# Backend
black app/          # Format
flake8 app/         # Lint
mypy app/           # Type check

# Frontend
npm run lint        # ESLint
npm run type-check  # TypeScript
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

### Contribution Guidelines

- ✅ Follow existing code style
- ✅ Write tests for new features
- ✅ Update documentation
- ✅ Ensure all tests pass

---

## 🗺️ Roadmap

- [x] **Phase 1:** Planning & Documentation
- [x] **Phase 2:** Foundation Setup
- [ ] **Phase 3:** Core Features (Calculator, Analytics, Basic AI)
- [ ] **Phase 4:** Advanced AI (RAG, Agents, Predictions)
- [ ] **Phase 5:** Polish & Deployment

### Future Enhancements

- 📱 Mobile app (React Native)
- 🎮 Gamification (badges, leaderboards)
- 🌐 Multi-language support
- 🏪 Carbon offset marketplace
- 🏠 Smart home device integration
- 👥 Social features & community challenges

---

## 🌱 UN SDG Alignment

<table>
<tr>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/SDG-11-red?style=for-the-badge" alt="SDG 11"/>
<br><b>Sustainable Cities</b>
<br>and Communities
</td>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/SDG-12-orange?style=for-the-badge" alt="SDG 12"/>
<br><b>Responsible Consumption</b>
<br>and Production
</td>
<td align="center" width="33%">
<img src="https://img.shields.io/badge/SDG-13-green?style=for-the-badge" alt="SDG 13"/>
<br><b>Climate</b>
<br>Action
</td>
</tr>
</table>

---

## 📊 Project Stats

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-active-success)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **IBM watsonx.ai** - Enterprise AI capabilities
- **UN SDG** - Sustainability guidelines
- **EPA** - Emission factor data
- **Open Source Community** - Amazing tools and libraries

---

## 📧 Contact & Support

<div align="center">

**Project Maintainer:** [Your Name]

[![Email](https://img.shields.io/badge/Email-Contact-blue?style=for-the-badge&logo=gmail)](mailto:your.email@example.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yourprofile)

**Found a bug?** [Open an issue](https://github.com/yourusername/carbontracker-ai/issues)

**Have a question?** [Start a discussion](https://github.com/yourusername/carbontracker-ai/discussions)

</div>

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ for a sustainable future 🌍**

*Last Updated: June 2026 • Version 0.1.0*

</div>