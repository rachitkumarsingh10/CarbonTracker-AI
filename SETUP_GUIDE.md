# CarbonTracker AI - Local Setup Guide (No Docker)

This guide will help you set up and run CarbonTracker AI on your local machine without Docker.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)

## Quick Start (Windows)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd carbontracker-ai
```

### 2. Run Setup Script
```bash
setup.bat
```

This will:
- Create Python virtual environment
- Install all Python dependencies
- Install all Node.js dependencies
- Create environment files
- Create necessary directories

### 3. Start the Application

**Option A: Start Both Servers Together**
```bash
start-all.bat
```

**Option B: Start Servers Separately**

Terminal 1 (Backend):
```bash
start-backend.bat
```

Terminal 2 (Frontend):
```bash
start-frontend.bat
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Manual Setup (Step by Step)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

5. Environment file is already created at `backend/.env`

6. Start the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
# Windows
copy .env.local.example .env.local

# Linux/Mac
cp .env.local.example .env.local
```

4. Start the frontend server:
```bash
npm run dev
```

## Database

The project uses **SQLite** for local development (no PostgreSQL installation needed).

- Database file: `backend/carbontracker.db`
- Automatically created on first run
- No manual database setup required

## Configuration

### Backend Configuration (`backend/.env`)

Key settings already configured:
- `DATABASE_URL=sqlite:///./carbontracker.db` - SQLite database
- `SECRET_KEY` - JWT secret (change in production)
- `CORS_ORIGINS` - Allowed frontend origins
- Carbon emission factors

### Frontend Configuration (`frontend/.env.local`)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=CarbonTracker AI
```

## Project Structure

```
carbontracker-ai/
├── backend/              # FastAPI backend
│   ├── venv/            # Python virtual environment
│   ├── app/             # Application code
│   ├── .env             # Environment variables
│   └── carbontracker.db # SQLite database (created on first run)
├── frontend/            # Next.js frontend
│   ├── node_modules/    # NPM packages
│   ├── src/             # Source code
│   └── .env.local       # Environment variables
├── setup.bat            # Setup script
├── start-backend.bat    # Start backend
├── start-frontend.bat   # Start frontend
└── start-all.bat        # Start both servers
```

## Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError`
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

**Problem**: Port 8000 already in use
**Solution**: Kill the process or change port in `start-backend.bat`

### Frontend Issues

**Problem**: `Module not found` errors
**Solution**: Reinstall dependencies
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Problem**: Port 3000 already in use
**Solution**: Next.js will automatically use port 3001

### TypeScript Errors

The TypeScript errors you see are normal before running `npm install`. They will be resolved after:
```bash
cd frontend
npm install
```

## Development Workflow

1. **Make changes** to backend or frontend code
2. **Servers auto-reload** (hot reload enabled)
3. **Test changes** in browser
4. **Check API docs** at http://localhost:8000/docs

## Next Steps

After setup, you can:

1. **Test the API** - Visit http://localhost:8000/docs
2. **View the Frontend** - Visit http://localhost:3000
3. **Start Development** - Begin implementing features
4. **Add AI Features** - Configure IBM watsonx.ai or Ollama

## Optional: AI Configuration

### IBM watsonx.ai (Recommended)

1. Get API key from [IBM Cloud](https://cloud.ibm.com/)
2. Update `backend/.env`:
```env
IBM_WATSONX_API_KEY=your-api-key
IBM_WATSONX_PROJECT_ID=your-project-id
```

### Ollama (Alternative)

1. Install [Ollama](https://ollama.ai/)
2. Pull Llama 3 model:
```bash
ollama pull llama3
```
3. Ollama runs on http://localhost:11434 by default

## Support

For issues or questions:
- Check the [PROJECT.md](PROJECT.md) for detailed documentation
- Review [docs/INSTALLATION.md](docs/INSTALLATION.md)
- Check API documentation at http://localhost:8000/docs

---

**Last Updated**: June 20, 2026
**Version**: 1.0.0