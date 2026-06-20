# CarbonTracker AI - Frontend

Next.js 14 frontend for CarbonTracker AI application.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create environment file:
```bash
cp .env.local.example .env.local
```

3. Run development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000)

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Forms**: React Hook Form + Zod
- **Charts**: Recharts
- **HTTP Client**: Axios

## Project Structure

```
src/
├── app/              # Next.js App Router pages
├── components/       # React components
│   ├── ui/          # Reusable UI components
│   ├── charts/      # Chart components
│   ├── forms/       # Form components
│   └── layout/      # Layout components
├── services/        # API services
├── hooks/           # Custom React hooks
├── context/         # React Context
├── utils/           # Utility functions
└── types/           # TypeScript types
```

## Environment Variables

See `.env.local.example` for required environment variables.