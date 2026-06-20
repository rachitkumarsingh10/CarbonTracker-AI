# CarbonTracker AI - Installation Guide

Complete step-by-step guide to set up the CarbonTracker AI development environment.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop/)
- **Git** - [Download](https://git-scm.com/downloads)

### Optional Software
- **VS Code** - Recommended IDE
- **Postman** - For API testing
- **pgAdmin** - PostgreSQL management (included in Docker Compose)

### System Requirements
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 10GB free space
- **OS**: Windows 10/11, macOS 10.15+, or Linux

## 🚀 Installation Steps

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone <repository-url>
cd carbontracker-ai

# Or if starting fresh (already done)
# The project structure is already created
```

### Step 2: Set Up Backend Environment

#### 2.1 Create Python Virtual Environment

**Windows (PowerShell):**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (Command Prompt):**
```cmd
cd backend
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

```bash
# Ensure virtual environment is activated
# You should see (venv) in your terminal prompt

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# This will install:
# - FastAPI and Uvicorn
# - SQLAlchemy and PostgreSQL driver
# - LangChain and AI libraries
# - IBM watsonx.ai SDK
# - ChromaDB
# - Scikit-learn and ML libraries
# - Tesseract OCR
# - And all other dependencies
```

**Note**: Installation may take 5-10 minutes depending on your internet speed.

#### 2.3 Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your configuration
# Use any text editor (VS Code, Notepad, nano, vim, etc.)
```

**Required Configuration:**
```env
# Database (will be created by Docker)
DATABASE_URL=postgresql://carbontracker:carbontracker_password@localhost:5432/carbontracker_db

# JWT Secret (generate a strong random key)
SECRET_KEY=your-super-secret-key-change-this

# IBM watsonx.ai (if you have access)
IBM_WATSONX_API_KEY=your-api-key-here
IBM_WATSONX_PROJECT_ID=your-project-id-here

# Or use Ollama as fallback
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
```

**Generate a secure SECRET_KEY:**
```python
# Run this in Python
import secrets
print(secrets.token_urlsafe(32))
```

### Step 3: Set Up Database Services

#### 3.1 Start Docker Services

```bash
# From project root directory
cd ..  # Go back to project root if in backend

# Start PostgreSQL and ChromaDB
docker-compose up -d

# Verify services are running
docker-compose ps

# You should see:
# - carbontracker-postgres (port 5432)
# - carbontracker-chromadb (port 8000)
# - carbontracker-pgadmin (port 5050) - optional
```

#### 3.2 Verify Database Connection

```bash
# Test PostgreSQL connection
docker exec -it carbontracker-postgres psql -U carbontracker -d carbontracker_db

# If successful, you'll see PostgreSQL prompt
# Type \q to exit

# Test ChromaDB
curl http://localhost:8000/api/v1/heartbeat
# Should return: {"nanosecond heartbeat": ...}
```

### Step 4: Initialize Database

```bash
# Go to backend directory
cd backend

# Activate virtual environment if not already active
# Windows: .\venv\Scripts\Activate.ps1
# Linux/Mac: source venv/bin/activate

# Initialize Alembic (database migrations)
alembic init alembic

# Create initial migration
alembic revision --autogenerate -m "Initial database schema"

# Apply migrations
alembic upgrade head
```

### Step 5: Set Up Frontend Environment

#### 5.1 Initialize Next.js Project

```bash
# From project root
cd frontend

# Initialize Next.js with TypeScript
npx create-next-app@latest . --typescript --tailwind --app --no-src-dir

# Answer the prompts:
# ✔ Would you like to use ESLint? Yes
# ✔ Would you like to use Turbopack? No
# ✔ Would you like to customize the default import alias? No
```

#### 5.2 Install Frontend Dependencies

```bash
# Install additional dependencies
npm install axios recharts zustand
npm install -D @types/node @types/react @types/react-dom

# All packages will be installed in node_modules/ (local to frontend)
```

#### 5.3 Configure Frontend Environment

```bash
# Create environment file
cp .env.local.example .env.local

# Edit .env.local
```

**Frontend Environment Variables:**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=CarbonTracker AI
```

### Step 6: Install OCR (Tesseract)

#### Windows:
```powershell
# Download Tesseract installer from:
# https://github.com/UB-Mannheim/tesseract/wiki

# Install and note the installation path
# Update backend/.env with the path:
TESSERACT_PATH=C:/Program Files/Tesseract-OCR/tesseract.exe
```

#### macOS:
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### Step 7: Set Up IBM watsonx.ai (Optional)

If you have IBM Cloud account:

1. **Create IBM Cloud Account**
   - Go to https://cloud.ibm.com/
   - Sign up or log in

2. **Create watsonx.ai Instance**
   - Navigate to watsonx.ai service
   - Create a new instance
   - Note your API key and Project ID

3. **Update Backend .env**
   ```env
   IBM_WATSONX_API_KEY=your-api-key
   IBM_WATSONX_PROJECT_ID=your-project-id
   ```

### Step 8: Set Up Ollama (Alternative to IBM)

If not using IBM watsonx.ai:

```bash
# Install Ollama
# Windows/Mac: Download from https://ollama.ai/
# Linux:
curl https://ollama.ai/install.sh | sh

# Pull Llama 3 model
ollama pull llama3

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

## ✅ Verification

### Test Backend

```bash
# From backend directory with venv activated
cd backend
uvicorn app.main:app --reload

# Open browser to:
# http://localhost:8000 - API root
# http://localhost:8000/docs - Swagger UI
# http://localhost:8000/health - Health check
```

### Test Frontend

```bash
# From frontend directory
cd frontend
npm run dev

# Open browser to:
# http://localhost:3000
```

### Test Database

```bash
# Access pgAdmin
# Open browser to: http://localhost:5050
# Login: admin@carbontracker.com / admin

# Add server connection:
# Host: postgres
# Port: 5432
# Username: carbontracker
# Password: carbontracker_password
```

## 🔧 Troubleshooting

### Python Virtual Environment Issues

**Problem**: Cannot activate virtual environment
```bash
# Windows: Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Recreate virtual environment
rm -rf venv
python -m venv venv
```

### Docker Issues

**Problem**: Docker containers won't start
```bash
# Check Docker is running
docker --version

# Stop all containers
docker-compose down

# Remove volumes and restart
docker-compose down -v
docker-compose up -d
```

### Database Connection Issues

**Problem**: Cannot connect to PostgreSQL
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Check logs
docker logs carbontracker-postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### Port Conflicts

**Problem**: Port already in use
```bash
# Find process using port (Windows)
netstat -ano | findstr :8000

# Find process using port (Linux/Mac)
lsof -i :8000

# Kill process or change port in configuration
```

### Import Errors

**Problem**: Module not found errors
```bash
# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### ChromaDB Issues

**Problem**: ChromaDB not responding
```bash
# Check ChromaDB logs
docker logs carbontracker-chromadb

# Restart ChromaDB
docker-compose restart chromadb

# Test connection
curl http://localhost:8000/api/v1/heartbeat
```

## 📦 Next Steps

After successful installation:

1. ✅ **Create Database Models** - Define SQLAlchemy models
2. ✅ **Implement API Endpoints** - Build REST APIs
3. ✅ **Set Up AI Components** - Configure LangChain and agents
4. ✅ **Build Frontend Pages** - Create React components
5. ✅ **Test Integration** - End-to-end testing

## 🆘 Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review error logs
3. Consult project documentation
4. Open an issue on GitHub

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [IBM watsonx.ai Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)
- [Docker Documentation](https://docs.docker.com/)

---

**Installation Complete!** 🎉

You're now ready to start developing CarbonTracker AI.