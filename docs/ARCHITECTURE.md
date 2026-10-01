# Technical Architecture Blueprint

**Platform:** GeoAgri-Assam (NESFIC-D-12)  
**Entities:** Assam State Space Applications Centre (ASSAC) & Directorate of Agriculture, Govt. of Assam

---

## 1. High-Level System Architecture

```mermaid
flowchart TD
    subgraph DataIngestion ["1. Satellite, Drone & Weather Ingestion"]
        S1["Sentinel-1 SAR C-Band (10m GRD)<br/>Dual-Pol VV/VH (100% Cloud Penetration)"]
        S2["Sentinel-2 Optical MSI (10m/20m)<br/>Bands B2-B8A, Red-Edge NDRE, NDVI"]
        UAV["UAV Drone Orthomosaics (3cm GSD)<br/>MicaSense RedEdge Multispectral"]
        MET["Agro-Meteorological Streams<br/>IMD Gridded Rainfall, ERA5, SMAP Soil Moisture"]
    end

    subgraph FeatureEngineering ["2. Spatial & Phenological Engine"]
        SAR_PROC["SAR Radiometric Terrain Correction (RTC)<br/>Speckle Filtering (Refined Lee)<br/>Cross-Pol Ratio (VH/VV) & RVI"]
        OPT_PROC["Cloud/Shadow Masking (s2cloudless)<br/>Temporal Interpolation & Gap Filling<br/>NDRE & LAI Biophysical Inversion"]
        MASK["Vector Boundary & Land-Use Masking<br/>District, Block, Gaon Panchayat, Revenue Village"]
    end

    subgraph MLEngine ["3. Machine Learning Yield & Area Models"]
        AREA_ML["Area Delineation Model<br/>Temporal CNN & Random Forest<br/>Phenological Boundary Detection"]
        YIELD_ML["Multivariate Satellite-Weather Regressor<br/>Ridge & Gradient Boosted Regression<br/>Calibrated with Historical & Real-Time CCEs"]
        UNCERTAIN["Uncertainty Quantifier<br/>Residual Error Variance & Conformal Bounds<br/>Explicit 95% Confidence Interval (± MT/Ha)"]
    end

    subgraph GroundTruth ["4. Mobile Field CCE Application"]
        MOBILE_APP["Field Enumerator Smartphone App<br/>• Auto-GPS Geotagging (±2.5m)<br/>• 5m x 5m Standard Cut Weighing<br/>• Moisture Standardization to 14%<br/>• Flood Inundation Depth & Duration<br/>• Watermarked Field Camera Capture"]
    end

    subgraph Dashboard ["5. Departmental GIS & Reconciliation Portal"]
        GIS_VIEW["Executive GIS Dashboard<br/>• Leaflet Map with District & CCE Clusters<br/>• Live Sensor Telemetry (SAR vs Optical)"]
        EDITOR["Reconciliation & Calibration Editor<br/>• Edit Area (Ha/Bighas) & Yield (MT/Ha)<br/>• Recalculate Production = Area × Yield<br/>• Approval Stages & Immutable Audit Trail"]
        EXPORTS["Departmental Export Engine<br/>• Official Schedule VI (JSON/CSV)<br/>• OGC-Compliant GeoJSON Layers"]
    end

    DataIngestion --> FeatureEngineering
    FeatureEngineering --> MLEngine
    MOBILE_APP -.->|"Ground Reality Calibration"| MLEngine
    MLEngine --> Dashboard
    MOBILE_APP --> Dashboard
```

---

## 2. Mathematical Formulations

### 2.1 Standardized Crop Cutting Experiment (CCE) Yield Formula
In the field application, enumerators measure fresh cut biomass in a standardized 5m $\times$ 5m ($25\text{ m}^2$) quadrant. The ground truth dry yield normalized to standard 14% storage moisture is calculated as:

$$\text{Raw Yield (MT/Ha)} = \left(\frac{\text{Fresh Cut Biomass (kg)}}{\text{Plot Area (m}^2)}\right) \times \frac{10{,}000\text{ m}^2}{1{,}000\text{ kg}} = \frac{\text{Biomass (kg)}}{25} \times 10$$

$$\text{Moisture Adjustment Factor} = \frac{100 - \text{Measured Moisture \%}}{100 - 14.0}$$

$$\text{Standardized Yield (MT/Ha)} = \text{Raw Yield} \times \text{Moisture Adjustment Factor}$$

Conversion to Assamese Bighas ($1\text{ Hectare} \approx 7.47\text{ Bighas}$):
$$\text{Yield (kg/Bigha)} = \frac{\text{Yield (MT/Ha)} \times 1{,}000}{7.47}$$

### 2.2 Satellite-Agrometeorological ML Yield Formulation
The multivariate regressor predicts crop yield $\hat{Y}$ per pixel and plot using standardized features:
$$\hat{Y} = w_0 + \sum_{i=1}^{M} w_i \left(\frac{x_i - \mu_i}{\sigma_i}\right)$$

Where the features include:
1. $x_1$: Sentinel-1 SAR VH backscatter in dB ($\sigma^0_{VH}$ biomass volume scattering, weight: $+0.2618$)
2. $x_2$: Sentinel-1 SAR VV backscatter in dB ($\sigma^0_{VV}$ surface/soil interaction, weight: $+0.0860$)
3. $x_3$: SAR cross-polarization ratio ($\sigma^0_{VH} - \sigma^0_{VV}$, weight: $+0.1455$)
4. $x_4$: Sentinel-2 Optical NDVI (Canopy greenness, weight: $+0.2467$)
5. $x_5$: Sentinel-2 Optical NDRE (Red-Edge Chlorophyll vigor, weight: $+0.1305$)
6. $x_6$: IMD gridded cumulative rainfall anomaly (weight: $-0.0340$)
7. $x_7$: Flood inundation duration in days (Damage penalty, weight: $-0.4673$)

### 2.3 Explicit 95% Confidence Interval (CI) Formulation
Every yield estimate outputs bounded uncertainty:
$$\text{CI}_{95\%} = \hat{Y} \pm 1.96 \times \text{SE}_{\text{residuals}}$$
In the Assam pilot cohort, $\text{SE} \approx 0.186\text{ MT/Ha}$, yielding an explicit bound of $\pm 0.36\text{ MT/Ha}$.

### 2.4 Total Production Formula
$$\text{Total Production (MT)} = \text{Estimated Area (Ha)} \times \text{Forecast Yield (MT/Ha)}$$

---

## 3. Technology Stack & Component Architecture

### 3.1 Frontend (`Yield-Frontend`)
* **Framework:** Next.js 14 (React 18, App Router)
* **GIS Mapping:** Leaflet.js with OpenStreetMap and CARTO Voyager tiles
* **Charts & Telemetry:** Chart.js, Lucide Icons, FontAwesome 6
* **Language:** TypeScript
* **State Management:** React hooks with optimistic local UI updates and instant REST synchronization

### 3.2 Backend (`Yield-Backend`)
* **Framework:** FastAPI (Python 3.12+)
* **Server Runtime:** Uvicorn (ASGI)
* **Data Validation:** Pydantic v2
* **Numerical Computing & ML:** NumPy, Scikit-learn
* **Documentation:** OpenAPI Swagger UI (`/docs`) and ReDoc (`/redoc`)
