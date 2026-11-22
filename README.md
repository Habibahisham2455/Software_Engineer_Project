# SmartSpend AI

SmartSpend AI is a personal finance web app that helps people understand where their money goes and make smarter spending decisions. Users log their income and daily expenses, set budgets and savings goals, and get instant alerts and insights, such as how small daily purchases add up each month.

**Target users:** university students, young professionals, and families.

## Features (Phase 1)

- **Income & expenses:** add, view, and delete transactions with a live balance
- **Daily spending log:** quick entry with one-tap categories (food, transport, coffee, etc.)
- **Dashboard:** summary cards, spending-by-category chart, and monthly overview
- **Budgets & alerts:** set monthly limits per category and get warnings at 80% and 100%
- **Savings goals:** track progress toward goals with progress bars
- **Smart insights:** rule-based tips that highlight top spending categories and small-spend habits
- **About page:** the project presentation (problem, solution, market, roadmap)

> Phase 1 uses rule-based insights and browser `localStorage`. LLM-powered chat, forecasting, and bank integrations are planned for later phases.

## Tech Stack

React 18 · Vite · React Router · Recharts · Vitest · ESLint · GitHub Actions

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) 18 or newer
- npm (comes with Node.js)
- Git

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-org>/SpendSmart.git
cd SpendSmart

# 2. Install dependencies
npm install

# 3. Start the development server
npm run dev
```

Open the URL shown in the terminal (usually http://localhost:5173).

### Other commands

| Command | Description |
|---|---|
| `npm run dev` | Start the dev server |
| `npm run build` | Create a production build in `dist/` |
| `npm run preview` | Preview the production build |
| `npm run lint` | Run ESLint |
| `npm test` | Run unit tests |

## Project Structure

```
src/
  pages/        Dashboard, Transactions, Budgets, Goals, About
  components/   Reusable UI components
  context/      Global state (FinanceContext)
  hooks/        useLocalStorage, useFinance
  utils/        Pure logic: calculations, budget, insights, goals
  data/         Categories, seed data, slides
tests/          Unit tests for the logic layer
.github/        CI workflow, issue and PR templates
```

## Team Workflow

- Tasks are tracked on our **GitHub Project board** (Todo / In Progress / Done) with milestones and deadlines.
- Work happens on `feature/<issue#>-<name>` branches, never directly on `main`.
- Every change goes through a **pull request** linked to an issue (`Closes #N`) and is reviewed by a teammate.
- **GitHub Actions** runs lint, tests, and build on every push and PR.

## Team

| Member | Responsibility |
|---|---|
| _Name_ | _e.g. Transactions & state_ |
| _Name_ | _e.g. Dashboard & charts_ |
| _Name_ | _e.g. Budgets, alerts & goals_ |
| _Name_ | _e.g. Insights, tests & CI_ |

## License

For educational use as part of a university course project.
