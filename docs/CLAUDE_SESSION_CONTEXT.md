# Claude AI Session Reference & Context Guide

> **Note for Future AI Agents & Claude Sessions:**  
> Read this document first when resuming, maintaining, or extending this project. It outlines the problem statement constraints, technical architecture, repository links, data structures, and operational state.

---

## 1. Project Background & Challenge Statement
* **Challenge:** NESFIC 2026 Challenge Stream 1 (NESFIC-D-12)
* **Official URL:** [https://startup.assam.gov.in/nesfic26/problem-statements/nesfic-d-12](https://startup.assam.gov.in/nesfic26/problem-statements/nesfic-d-12)
* **Problem Objective:** Improve the timeliness, repeatability, and spatial detail of crop-area, yield, and production estimates for planning, procurement, and programme monitoring in Assam.
* **Sponsoring Agency:** Assam State Space Applications Centre (ASSAC), Science, Technology & Climate Change Department, Government of Assam, in coordination with the Directorate of Agriculture & Horticulture.

### Strict User Directives
1. **Stick to the Problem Solution Only:** Do not introduce unrelated features, bloated SaaS pricing tiers, or unrequested modules.
2. **Include All Crops Grown in Assam:** The system must cover all 56 agricultural, horticultural, plantation, and cash crops across Assam (listed in `docs/CROPS_CATALOG_ASSAM.md`).

---

## 2. GitHub Repositories
* **Frontend Repository (Next.js 14):**  
  [https://github.com/kaustavgayon93-ux/Yield-Frontend.git](https://github.com/kaustavgayon93-ux/Yield-Frontend.git)
* **Backend Repository (FastAPI & ML Engine):**  
  [https://github.com/kaustavgayon93-ux/Yield-Backend.git](https://github.com/kaustavgayon93-ux/Yield-Backend.git)

---

## 3. Local Workspace Layout

```
C:\Users\kaust\.gemini\antigravity\scratch\
│
├── yield-frontend/                        <-- Next.js 14 Frontend Application
│   ├── app/                              # App Router (layout.tsx, page.tsx, globals.css)
│   ├── components/                       # GisMap, KpiCards, DataEditor, FieldApp, UncertaintyView, ExportView
│   ├── data/                             # crops.json (56 crops), districts.json, db.json
│   ├── docs/                             # PRD.md, ARCHITECTURE.md, CROPS_CATALOG_ASSAM.md, CLAUDE_SESSION_CONTEXT.md
│   └── package.json                      # Next.js, React, Leaflet, Chart.js
│
├── yield-backend/                         <-- Python FastAPI Backend & ML Service
│   ├── main.py                           # FastAPI application with REST endpoints
│   ├── models.py                         # Pydantic schemas for data validation
│   ├── ml/                               # satellite_ml_engine.py & trained_model.json
│   ├── data/                             # crops.json, districts.json, db.json
│   ├── tests/test_backend.py             # Automated test suite
│   ├── docs/                             # Complete mirrored documentation
│   └── requirements.txt                  # fastapi, uvicorn, pydantic, numpy, requests
│
└── mingit/                               <-- Portable MinGit 64-bit installation
    └── cmd/git.exe                       # Used for git operations in PowerShell
```

---

## 4. Key Business Logic & Math to Preserve

### 4.1 CCE Yield Formula (Field Mobile App)
Enumerators measure fresh biomass in a standardized 5m $\times$ 5m ($25\text{ m}^2$) quadrant. The yield standardized to 14% moisture is:
$$\text{Yield (MT/Ha)} = \left(\frac{\text{Biomass (kg)}}{25\text{ m}^2}\right) \times 10 \times \left(\frac{100 - \text{Moisture \%}}{100 - 14.0}\right)$$
$$\text{Yield (kg/Bigha)} = \frac{\text{Yield (MT/Ha)} \times 1{,}000}{7.47}$$

### 4.2 Machine Learning Model (`ml/trained_model.json`)
* **Algorithm:** Multivariate Ridge Regressor trained on Sentinel-1 SAR dual-pol backscatter ($VH, VV, VH/VV$), Sentinel-2 optical ($NDVI, NDRE$), IMD rainfall, and flood duration.
* **Performance:** $R^2 = 0.912$, $\text{RMSE} = 0.186\text{ MT/Ha}$, $\text{MAPE} = 5.06\%$.
* **Uncertainty Bounds:** Explicit 95% Confidence Interval ($\pm 0.36\text{ MT/Ha}$).

### 4.3 Total Production Formula (Dashboard & Editor)
$$\text{Production (MT)} = \text{Area (Ha)} \times \text{Yield (MT/Ha)}$$

---

## 5. How to Run & Test

### Frontend (Next.js)
```bash
cd yield-frontend
npm install
npm run dev
# Running on http://localhost:3000
```

### Backend (FastAPI)
```bash
cd yield-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python tests/test_backend.py
uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Docs at http://localhost:8000/docs
```
