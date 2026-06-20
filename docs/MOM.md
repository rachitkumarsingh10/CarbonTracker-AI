# CarbonTracker AI - Minutes of Meeting (MOM)

## Project Development Log

---

## Meeting #1: Project Initiation & Requirements Gathering
**Date**: June 20, 2026  
**Time**: 06:34 IST  
**Attendees**: Project Team, Stakeholders  
**Meeting Type**: Requirements Discussion

### Agenda
1. Project introduction and objectives
2. Technology stack discussion
3. Feature requirements review
4. Architecture planning

### Discussion Points

#### 1. Project Overview
- **Project Name**: CarbonTracker AI
- **Purpose**: AI-powered web application for carbon footprint tracking and reduction
- **Target Users**: Individuals concerned about their environmental impact
- **SDG Alignment**: SDG 11, 12, and 13

#### 2. Core Requirements Confirmed
✅ **User Management**
- User registration and authentication
- Profile management with sustainability goals
- JWT-based security

✅ **Carbon Footprint Calculator**
- Input: Electricity, transportation, food, water consumption
- Output: Monthly/annual CO₂ emissions, sustainability score (0-100)
- Category-wise breakdown

✅ **Analytics Dashboard**
- Visual charts and graphs (using Recharts)
- Monthly trends and comparisons
- Emission breakdown by category

✅ **AI Features**
- AI chatbot for sustainability advice
- RAG-based knowledge system
- 4 specialized AI agents
- Personalized recommendations
- ML-based predictions (6-month forecast)

✅ **Additional Features**
- Document upload with OCR (bills, receipts)
- Admin panel for system management
- Mobile-responsive design

#### 3. Technology Stack Decisions

**Frontend Decision**
- ✅ **Selected**: Next.js 14 (App Router)
- **Rationale**: 
  - Better SEO with SSR
  - Built-in API routes
  - Superior performance
  - Easy deployment to Vercel
- **Alternative Considered**: Create React App (rejected - less features)

**Backend Decision**
- ✅ **Selected**: FastAPI (Python 3.11+)
- **Rationale**:
  - Fast and modern
  - Excellent for AI/ML integration
  - Auto-generated API docs
  - Type hints support

**Database Decision**
- ✅ **Selected**: PostgreSQL 15
- **Rationale**:
  - Robust and reliable
  - Excellent for structured data
  - Good performance
  - Wide ecosystem support

**AI/ML Stack Decisions**
- ✅ **LLM**: IBM Granite (via watsonx.ai) - **PRIMARY CHOICE**
  - **Rationale**: Enterprise-grade, IBM ecosystem integration
  - **Fallback**: Llama 3 (via Ollama) if IBM access unavailable
- ✅ **AI Framework**: LangChain
  - **Rationale**: Industry standard, excellent for RAG and agents
- ✅ **Vector Database**: ChromaDB
  - **Rationale**: Easy to use, good for RAG, Docker support
- ✅ **ML Libraries**: Scikit-learn, Pandas, NumPy
  - **Rationale**: Standard Python ML stack

**OCR Decision**
- ✅ **Selected**: Tesseract (pytesseract)
- **Rationale**: Open-source, reliable, good accuracy
- **Alternative**: Cloud OCR services (AWS Textract, Google Vision) - for future

#### 4. Environment Strategy - CRITICAL DECISION
🎯 **Key Requirement**: All packages must be installed in isolated environments, NOT globally

**Backend Environment**
- ✅ Python virtual environment (`venv`)
- All dependencies in `requirements.txt`
- Isolated from system Python

**Frontend Environment**
- ✅ Local `node_modules` directory
- All dependencies in `package.json`
- No global npm packages

**Database & Services**
- ✅ Docker containers for PostgreSQL and ChromaDB
- Isolated from host system
- Easy to replicate across environments

#### 5. Carbon Calculation Methodology
✅ **Emission Factors Decided**:
- Electricity: ~0.92 lbs CO₂/kWh (EPA standard)
- Car: ~0.404 kg CO₂/km
- Flights: ~0.255 kg CO₂/km
- Food (Meat-based): ~7.2 kg CO₂/day
- Food (Vegan): ~2.9 kg CO₂/day
- Public Transport: ~0.089 kg CO₂/km

**Note**: Regional variations can be added in future versions

#### 6. RAG Knowledge Base Strategy
✅ **Data Sources Confirmed**:
1. UN SDG documentation
2. EPA climate reports
3. IPCC reports (publicly available)
4. Renewable energy guides
5. Government sustainability guidelines

**Implementation Approach**:
- Start with curated document set
- Manual collection and preprocessing
- Store in ChromaDB with embeddings
- Future: Add web scraping capability

#### 7. AI Agents Architecture
✅ **Four Agents Confirmed**:

1. **Carbon Calculation Agent**
   - Purpose: Calculate emissions from user input
   - Data Source: PostgreSQL database
   - Output: CO₂ values, breakdowns

2. **Recommendation Agent**
   - Purpose: Generate personalized recommendations
   - Data Source: ChromaDB (RAG), user profile
   - Output: Actionable suggestions with CO₂ savings

3. **Education Agent**
   - Purpose: Explain climate concepts
   - Data Source: ChromaDB (RAG)
   - Output: Educational content, explanations

4. **Goal Tracking Agent**
   - Purpose: Monitor and encourage goal progress
   - Data Source: PostgreSQL (goals table)
   - Output: Progress updates, motivational messages

**Agent Orchestration**: LangChain's agent framework with custom tools

#### 8. Development Phases Agreed
✅ **Phase 1: Foundation (Weeks 1-2)**
- Environment setup (venv, node_modules, Docker)
- Database schema implementation
- Basic authentication (JWT)
- Simple carbon calculator
- Basic frontend structure

✅ **Phase 2: Core Features (Weeks 3-4)**
- Analytics dashboard with charts
- Basic AI chatbot (without RAG initially)
- Recommendations engine
- User profile management

✅ **Phase 3: Advanced AI (Weeks 5-6)**
- RAG implementation with ChromaDB
- 4 AI agents system
- ML prediction model
- Enhanced chatbot with RAG

✅ **Phase 4: Polish & Deploy (Weeks 7-8)**
- OCR document upload
- Admin panel
- Comprehensive testing
- Documentation completion
- Deployment setup

### Action Items

| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Create PROJECT.md documentation | Development Team | June 20, 2026 | ✅ COMPLETED |
| Create MOM.md document | Development Team | June 20, 2026 | ✅ COMPLETED |
| Set up project folder structure | Development Team | Week 1 | 🔄 PENDING |
| Initialize Git repository | Development Team | Week 1 | 🔄 PENDING |
| Set up Python virtual environment | Backend Team | Week 1 | 🔄 PENDING |
| Set up Node.js environment | Frontend Team | Week 1 | 🔄 PENDING |
| Configure Docker Compose | DevOps | Week 1 | 🔄 PENDING |
| Design database schema | Backend Team | Week 1 | 🔄 PENDING |
| Obtain IBM watsonx.ai access | Project Lead | Week 1 | 🔄 PENDING |
| Collect sustainability documents | Content Team | Week 2 | 🔄 PENDING |

### Decisions Made

| Decision | Option Chosen | Rationale |
|----------|---------------|-----------|
| Frontend Framework | Next.js 14 | SSR, better SEO, built-in features |
| Backend Framework | FastAPI | Fast, modern, great for AI/ML |
| Database | PostgreSQL 15 | Robust, reliable, good performance |
| LLM | IBM Granite (Primary) | Enterprise-grade, IBM ecosystem |
| LLM Fallback | Llama 3 via Ollama | Free, local deployment option |
| AI Framework | LangChain | Industry standard, RAG support |
| Vector DB | ChromaDB | Easy to use, Docker support |
| OCR | Tesseract | Open-source, reliable |
| Environment Strategy | Isolated (venv, node_modules) | Best practice, reproducible |
| Deployment | Docker Compose | Easy setup, portable |

### Risks & Mitigation

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| IBM Granite API access delay | High | Use Llama 3 as fallback |
| Complex AI agent coordination | Medium | Start simple, iterate |
| ML model accuracy | Medium | Use proven algorithms, validate thoroughly |
| OCR accuracy on varied documents | Medium | Implement manual correction option |
| Large dataset for RAG | Low | Start with curated set, expand gradually |
| Performance with multiple users | Medium | Implement caching, optimize queries |

### Technical Constraints

1. **Environment Isolation**: All packages MUST be in isolated environments
2. **IBM Tools Priority**: Prefer IBM tools where available
3. **Sustainability Focus**: All features must align with SDG goals
4. **User Privacy**: Secure handling of personal data
5. **Scalability**: Design for growth from day one

### Next Steps

1. ✅ Review and approve PROJECT.md
2. ✅ Review and approve MOM.md
3. 🔄 Switch to Code mode for implementation
4. 🔄 Begin Phase 1: Foundation setup
5. 🔄 Create folder structure
6. 🔄 Set up development environments

### Questions & Clarifications

**Q1**: Do we have IBM watsonx.ai API access?  
**A1**: To be confirmed - will use Llama 3 as fallback if needed

**Q2**: Should we implement all features at once or in phases?  
**A2**: Phased approach agreed (4 phases over 8 weeks)

**Q3**: What about mobile app?  
**A3**: Future enhancement - focus on responsive web app first

**Q4**: How to handle regional emission factor variations?  
**A4**: Start with EPA standards, add regional support in future

### Meeting Outcomes

✅ **Approved**: Complete project architecture  
✅ **Approved**: Technology stack with IBM tools priority  
✅ **Approved**: Phased development approach  
✅ **Approved**: Environment isolation strategy  
✅ **Approved**: Feature set and priorities  

### Documentation Created

1. ✅ **PROJECT.md** - Comprehensive project documentation
   - Technology stack
   - Project structure
   - Database schema
   - API endpoints
   - Features description
   - Setup instructions

2. ✅ **MOM.md** - This document
   - Meeting minutes
   - Decisions log
   - Action items
   - Risk assessment

### Attachments

- PROJECT.md (638 lines)
- Architecture diagrams (to be created)
- Database schema (to be finalized)

---

## Meeting #2: Implementation Planning
**Date**: TBD  
**Attendees**: Development Team  
**Agenda**: Detailed implementation planning for Phase 1

*To be scheduled after PROJECT.md and MOM.md approval*

---

## Change Log

| Date | Change | Reason | Approved By |
|------|--------|--------|-------------|
| June 20, 2026 | Initial MOM created | Project kickoff | Team |
| June 20, 2026 | Added IBM tools priority | User requirement | User |
| June 20, 2026 | Confirmed environment isolation | User requirement | User |

---

## Notes

- All team members should review PROJECT.md before next meeting
- IBM watsonx.ai access to be confirmed ASAP
- Development to begin after approval of planning documents
- Regular updates to this MOM as project progresses

---

**Document Status**: ✅ ACTIVE  
**Last Updated**: June 20, 2026, 06:44 IST  
**Next Review**: After Phase 1 completion  
**Document Owner**: Project Lead  

---

## Approval Signatures

- [ ] Project Lead: _________________ Date: _______
- [ ] Technical Lead: _________________ Date: _______
- [ ] Stakeholder: _________________ Date: _______

---

*This document will be updated after each major meeting or decision point.*