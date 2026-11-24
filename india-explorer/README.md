# 🇮🇳 India Explorer

An interactive, full-stack digital atlas and discovery platform for India. Explore all **28 States**, **8 Union Territories**, historic districts, and iconic world heritage monuments with interactive 3D visualizations, cultural insights, and geographic statistics.

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![React](https://img.shields.io/badge/React-18.3-61dafb.svg?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.5-3178c6.svg?logo=typescript)
![Three.js](https://img.shields.io/badge/Three.js-0.168-black.svg?logo=three.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-47A248.svg?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)

---

## ✨ Features

- **🌐 Interactive 3D Three.js Globe**:
  - Smooth 3D rotating globe rendered with WebGL.
  - Earth's 23.5° axial tilt, glowing atmosphere, and latitude/longitude navigation rings.
  - Pulsing beacon highlight calibrated to India's exact geographic coordinates (20.59° N, 78.96° E).
  - Drag-to-rotate with inertia physics, mouse hover indicators, and responsive resizing.

- **🗺️ Complete Pan-India Coverage**:
  - Full data coverage for all **28 States** and **8 Union Territories**.
  - Hierarchical structure: `Country` ➔ `State / Union Territory` ➔ `District` ➔ `Place / Heritage Landmark`.
  - Detailed profiles for world-renowned sites: *Taj Mahal*, *Mysore Palace*, *Golden Temple*, *Gateway of India*, *Hawa Mahal*, *Jog Falls*, *Lalbagh Botanical Garden*, *Kashi Vishwanath*, and more.

- **🧭 Seamless Breadcrumb Navigation**:
  - Automatically constructed hierarchical breadcrumbs on every destination view (`Home / India / Karnataka / Mysuru / Mysore Palace`).
  - One-click navigation to jump back to parent regions or the country overview.

- **🔍 Instant Multi-Field Search**:
  - Fast autocomplete search scanning place names, administrative paths, and summary descriptions.
  - Keyboard-friendly navigation, search result icons, and click-outside dismissal.

- **📊 Comprehensive Fact Profiles**:
  - Capitals, official languages, state birds, animals, flowers, and iconic local foods.
  - Population and land area metrics, UNESCO World Heritage highlights, and verified Wikipedia references.

- **🛡️ Production Security & Performance**:
  - Sliding-window IP rate limiter (120 req/minute).
  - Essential security headers (`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `X-XSS-Protection`).
  - Client-side in-memory caching to eliminate redundant network roundtrips.

---

## 🏗️ Architecture & Tech Stack

```
india-explorer/
├── backend/                  # FastAPI REST API (Python 3.12)
│   ├── main.py               # API endpoints, middleware, rate limiter, breadcrumbs
│   ├── seed.py               # Database seeder and index builder
│   ├── seed.json             # Seed dataset (States, UTs, Districts, Landmarks)
│   ├── requirements.txt      # Python dependencies (FastAPI, Uvicorn, PyMongo)
│   └── Dockerfile            # Container configuration for backend
├── frontend/                 # React 18 + TypeScript + Vite 5 + Three.js
│   ├── src/
│   │   ├── App.tsx           # Main application layout, routing & UI views
│   │   ├── Globe.tsx         # Interactive Three.js 3D Globe component
│   │   ├── api.ts            # Typed API client, data models & cache layer
│   │   ├── styles.css        # Modern responsive dark theme styling
│   │   ├── main.tsx          # Application entry point
│   │   └── vite-env.d.ts     # Vite client type definitions
│   ├── public/               # Static assets, sitemap.xml, robots.txt
│   ├── index.html            # HTML entry point with metadata
│   ├── package.json          # Node dependencies and scripts
│   ├── tsconfig.json         # TypeScript compiler configuration
│   ├── vite.config.ts        # Vite build tool configuration
│   ├── nginx.conf            # Nginx production reverse proxy config
│   └── Dockerfile            # Multi-stage production container build
├── docker-compose.yml        # Multi-container orchestration (Mongo, Backend, Frontend)
└── README.md                 # Project documentation
```

### Technology Highlights

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, TypeScript 5.5, Vite 5, React Router 6, Three.js 0.168 |
| **Backend** | Python 3.12+, FastAPI, Uvicorn, PyMongo, Pydantic |
| **Database** | MongoDB 7.0 (with indexes on `id`, `parent`, `name`, `type`) |
| **Infrastructure** | Docker, Docker Compose, Nginx Alpine |

---

## 🚀 Quick Start with Docker (Recommended)

Run the complete multi-service stack with a single command:

```bash
docker compose up --build
```

Once started:
- 🌐 **Frontend Web App**: [http://localhost:8080](http://localhost:8080)
- 🔌 **Backend REST API**: [http://localhost:8000](http://localhost:8000)
- 📖 **Interactive Swagger API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 🍃 **MongoDB Service**: `localhost:27017`

To shut down the services and remove containers:
```bash
docker compose down
```

---

## 💻 Manual Local Development Setup

### Prerequisites

- **Python 3.10+** (Python 3.12+ recommended)
- **Node.js 18+** (Node.js 20+ recommended) and `npm`
- **MongoDB 6.0+** running locally on port `27017`

---

### 1. Backend Setup

Run it from inside the backend folder, because that is where `requirements.txt` lives.

```bash
cd india-explorer/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

> `venv\Scripts\activate` is for Windows. On Mac or Linux, use `source venv/bin/activate` instead.

The file `backend/requirements.txt` contains:
```
fastapi
uvicorn
pymongo
```

After installing, start the backend (MongoDB must already be running on your computer):

```bash
python seed.py
uvicorn main:app --reload
```

`seed.py` loads the sample data into MongoDB, and the API then runs at [http://localhost:8000](http://localhost:8000). You can open [http://localhost:8000/docs](http://localhost:8000/docs) to test it.

> If you use Docker (`docker compose up --build`), you don't need to run `pip install` yourself, because the backend container installs these packages automatically.

---

### 2. Frontend Setup

1. In a new terminal, navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install npm dependencies:
   ```bash
   npm install
   ```

3. Verify TypeScript types:
   ```bash
   npx tsc --noEmit
   ```

4. Launch the Vite development server:
   ```bash
   npm run dev
   ```
   *The frontend will run at [http://localhost:5173](http://localhost:5173).*

---

## 📡 REST API Reference

### 1. Health Check
`GET /api/health`
- **Description**: Returns database connectivity and total indexed document count.
- **Response**:
  ```json
  {
    "status": "ok",
    "places_count": 55
  }
  ```

### 2. Overview Statistics
`GET /api/stats`
- **Description**: Returns counts of total records, states, union territories, districts, and landmarks.
- **Response**:
  ```json
  {
    "total": 55,
    "states": 28,
    "union_territories": 8,
    "districts": 8,
    "landmarks": 10
  }
  ```

### 3. Get Direct Children
`GET /api/children/{pid}`
- **Parameters**: `pid` (string) — The parent identifier (e.g. `india`, `karnataka`, `uttar-pradesh`).
- **Example**: `GET /api/children/india` returns all 28 states and 8 union territories.
- **Response**:
  ```json
  [
    {
      "id": "karnataka",
      "name": "Karnataka",
      "type": "state",
      "parent": "india",
      "summary": "Cradle of stone architecture, tech capital of India, and land of coffee...",
      "path": "Karnataka, India"
    }
  ]
  ```

### 4. Get Place Details with Breadcrumbs
`GET /api/place/{pid}`
- **Parameters**: `pid` (string) — Unique slug identifier (e.g. `taj-mahal`, `mysore-palace`, `karnataka`).
- **Response**:
  ```json
  {
    "id": "taj-mahal",
    "name": "Taj Mahal",
    "type": "place",
    "parent": "agra",
    "path": "Taj Mahal, Agra, Uttar Pradesh, India",
    "summary": "The jewel of Muslim art in India and universally admired masterpiece of world heritage...",
    "points": [
      "Commissioned in 1632 by Mughal emperor Shah Jahan...",
      "Designated a UNESCO World Heritage Site in 1983..."
    ],
    "wiki": "https://en.wikipedia.org/wiki/Taj_Mahal",
    "breadcrumbs": [
      { "id": "india", "name": "India", "type": "country" },
      { "id": "uttar-pradesh", "name": "Uttar Pradesh", "type": "state" },
      { "id": "agra", "name": "Agra", "type": "district" },
      { "id": "taj-mahal", "name": "Taj Mahal", "type": "place" }
    ]
  }
  ```

### 5. Search Destinations
`GET /api/search?q={query}`
- **Parameters**: `q` (string) — Search term (minimum 2 characters).
- **Example**: `GET /api/search?q=palace`
- **Response**:
  ```json
  [
    {
      "id": "mysore-palace",
      "name": "Mysore Palace",
      "type": "place",
      "path": "Mysore Palace, Mysuru, Karnataka, India",
      "summary": "The magnificent royal residence of the Wadiyar dynasty..."
    }
  ]
  ```

---

## ⚙️ Environment Variables

| Variable | Scope | Default | Description |
|---|---|---|---|
| `MONGO_URL` | Backend | `mongodb://localhost:27017` | MongoDB connection URI string |
| `ALLOWED_ORIGINS` | Backend | `http://localhost:8080,http://localhost:5173` | Comma-separated CORS allowed origins |
| `VITE_API` | Frontend | `http://localhost:8000` | Base URL of the backend API for client requests |

---

## 🛠️ Adding New Data

To add new states, districts, or attractions:
1. Open `backend/seed.json`.
2. Add a new JSON object adhering to the schema:
   ```json
   {
     "id": "unique-kebab-case-slug",
     "name": "Display Name",
     "type": "state | union-territory | district | place",
     "parent": "parent-id",
     "path": "Display Name, Parent Name, India",
     "summary": "Brief 1-2 sentence overview of the location.",
     "profile": {
       "Language": "Primary Language",
       "Capital": "Capital City",
       "Food": "Famous Local Delicacies"
     },
     "area": "12,345 km²",
     "population": "1.2 million",
     "points": [
       "Key historical or geographical fact",
       "Prominent attraction or UNESCO status"
     ],
     "wiki": "https://en.wikipedia.org/wiki/..."
   }
   ```
3. Run `python seed.py` (or restart the docker container) to apply changes.

---

## 📦 Production Build

To test the production build of the frontend locally:

```bash
cd frontend
npm run build
npx vite preview
```

---

## 📄 License

This project is open-source under the MIT License. Feel free to use, modify, and distribute it for personal and educational purposes.
