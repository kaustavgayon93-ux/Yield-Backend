# GeoAgri-Assam: Satellite & AI Crop Yield Estimation Backend

**NESFIC 2026 Challenge Stream 1 (NESFIC-D-12)**  
*Assam State Space Applications Centre (ASSAC) & Directorate of Agriculture, Government of Assam*

---

## 🛰️ Project Overview

This is the Python FastAPI backend and Machine Learning service for **NESFIC-D-12**:
> *"Improve the timeliness, repeatability and spatial detail of crop-area, yield and production estimates for planning, procurement and programme monitoring."*

It delivers high-performance REST APIs and real-time Machine Learning inference combining **Sentinel-1 SAR C-band radar**, **Sentinel-2 optical MSI**, **IMD weather data**, and ground-truth **Crop Cutting Experiments (CCE)** collected via the mobile app.

---

## 🧠 Machine Learning Engine Architecture

Assam experiences 75–85% monsoon cloud hindrance during the peak Kharif (*Sali* rice) season. To ensure year-round repeatability:
1. **Radar Biomass Dynamics:** Utilizes dual-polarization Sentinel-1 Ground Range Detected (GRD) C-Band backscatter ($\sigma^0_{VH}$, $\sigma^0_{VV}$, and $VH/VV$ cross-polarization ratio).
2. **Optical Canopy Vigor:** Utilizes Sentinel-2 Level-2A BOA reflectance for **NDRE** (Red-Edge Chlorophyll) and **NDVI** during clear autumn and winter windows.
3. **Agro-Meteorological Integration:** Incorporates IMD cumulative rainfall and flood submergence duration (days) to account for flood-damage penalties across the Brahmaputra floodplain.
4. **Validation Metrics (Trained on Assam Multi-Season Cohort):**
   * **Correlation ($R^2$):** `0.912` (Target $\ge 0.75$ — Met)
   * **Root Mean Square Error (RMSE):** `0.186 MT/Ha`
   * **Mean Absolute Pct Error (MAPE):** `5.06%` (Target $\le 10\%$ — Met)
   * **Confidence Interval:** Explicit 95% Confidence Interval ($\pm 0.36\text{ MT/Ha}$)

---

## 📡 REST API Specifications

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root service health check & system metadata |
| `GET` | `/api/crops` | Complete catalog of all 56 crops grown in Assam with Assamese local names |
| `GET` | `/api/districts` | Assam's 35 districts, agro-climatic zones, and sample blocks |
| `GET` | `/api/estimates` | District crop-area, yield forecasts, and 95% Confidence Intervals |
| `GET` | `/api/estimates/{id}` | Single crop estimate details |
| `PUT` | `/api/estimates/{id}` | Departmental calibration/edit endpoint with automatic audit logging |
| `POST` | `/api/estimates` | Create new crop estimate record |
| `GET` | `/api/field-records` | Retrieve ground Crop Cutting Experiment (CCE) records |
| `POST` | `/api/field-records` | Mobile field collection submission endpoint with standard 5m×5m moisture normalization |
| `PUT` | `/api/field-records/{id}/verify` | Departmental verification & approval workflow |
| `GET` | `/api/ml/model` | Inspect trained model weights, scaling parameters, and validation metrics |
| `POST` | `/api/ml/predict` | Live ML inference on satellite SAR, optical, rainfall, and flood features |
| `GET` | `/api/analytics` | Statewide summaries, category distributions, and sensor telemetry |
| `GET` | `/api/export/csv` | Download official Government Schedule VI table in CSV format |
| `GET` | `/api/export/geojson` | Download spatial GIS feature collection for QGIS/ArcGIS/ASSAC portal |
| `GET` | `/api/export/schedule` | View official Directorate of Agriculture Schedule VI JSON |

---

## 🌾 Comprehensive Assam Crop Profile (56 Crops)

The backend natively supports all crops cultivated across Assam:
* **Cereals:** Sali Rice (*হালি ধান*), Ahu Rice (*আহু ধান*), Boro Rice (*বৰো ধান*), Bao Rice (*বাও ধান*), Asra Rice, Maize, Wheat, Small Millets (*Marua & Kaon*).
* **Pulses:** Black gram (*Matikalai*), Green gram (*Moong*), Lentil (*Masur*), Field pea (*Matar*), Chickpea (*Chana*), Pigeon pea (*Arhar/Rahar*), Cowpea, Horse gram (*Kulthi*), Rajma.
* **Oilseeds:** Rapeseed & Mustard (*Toria, TS-36, TS-38, Rai*), Sesame (*Til*), Linseed (*Tisi*), Castor, Sunflower, Groundnut, Niger, Soybean.
* **Cash & Plantation:** Jute (*Tossa & White*), Mesta, Cotton, Sugarcane (*Kuhiar*), Assam Tea (*Organized Estates & Small Tea Growers*), Arecanut (*Tamul*), Rubber, Coffee, Betel Vine (*Paan*), Coconut.
* **Horticulture & Spices:** Banana (*Malbhog, Jahaji*), Pineapple (*Kew, Queen*), Assam Lemon (*Kaji Nemu - GI Tagged*), Mandarin Orange, Bhut Jolokia (*King Chilli - GI Tagged*), Ginger (*Karbi Anglong organic*), Turmeric, Black Pepper, Potato, Tomato, Brinjal, Cucurbits, Cole crops, Leafy greens (*Lai Xaak, Lofa, Paleng*).
* **Sericulture Host Plants:** Som, Soalu (*Muga host*), Castor, Kesseru (*Eri host*), Mulberry (*Pat host*).

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/kaustavgayon93-ux/Yield-Backend.git
cd Yield-Backend
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Retrain / Evaluate ML Model (Optional)
```bash
python ml/engine.py
```

### 5. Start the FastAPI Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Interactive API Documentation (Swagger UI)
Visit [http://localhost:8000/docs](http://localhost:8000/docs) in your browser for the full interactive Swagger documentation.
