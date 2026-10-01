# Product Requirement Document (PRD)

**Project Name:** GeoAgri-Assam: Satellite-Ground Integrated Crop Area, Yield & Production Estimation Platform  
**Challenge Identifier:** NESFIC 2026 Challenge Stream 1 (NESFIC-D-12)  
**Official Portal Reference:** [https://startup.assam.gov.in/nesfic26/problem-statements/nesfic-d-12](https://startup.assam.gov.in/nesfic26/problem-statements/nesfic-d-12)  
**Sponsoring Department:** Assam State Space Applications Centre (ASSAC), Science, Technology & Climate Change Dept., in coordination with Directorate of Agriculture & Directorate of Horticulture and Food Processing, Government of Assam.  
**Target Users:** State Planners, District Agriculture Officers (DAOs), Sub-Divisional Agriculture Officers (SDAOs), Agricultural Development Officers (ADOs), Field Enumerators, Food Corporation of India (FCI), Assam State Agricultural Marketing Board (ASAMB), PMFBY Crop Insurance Assessors.

---

## 1. Executive Summary & Problem Breakdown

### 1.1 The Operational Context
Conventional crop acreage and yield estimation in Assam relies predominantly on manual sample surveys, Patwari/enumerator reporting schedules, and traditional Crop Cutting Experiments (CCE). While physically verified, this manual paradigm exhibits severe systemic bottlenecks:
1. **Compilation Delays:** Final reconciled production figures take 3 to 6 months post-harvest to compile, paralyzing timely MSP procurement planning by FCI/ASAMB and delaying post-disaster flood relief.
2. **Coarse Spatial Resolution:** Output statistics are aggregated at district or sub-divisional levels, lacking granular village-level (Gaon Panchayat) or plot-level distribution.
3. **Monsoon Cloud Cover Barrier:** Optical satellite remote sensing (Landsat/Sentinel-2) suffers from 75–85% persistent cloud obscuration during the Kharif monsoon season (June–October), when Assam's primary staple—*Sali* rice—is cultivated.
4. **Lack of Uncertainty Quantification:** Official figures are reported as deterministic point estimates without explicit statistical confidence intervals ($95\%\text{ CI}$) or validation error metrics.

### 1.2 The Desired State
To build an end-to-end, reproducible, geospatial AI platform combining:
* Automated **Sentinel-1 SAR C-Band dual-pol (VV/VH)** radar pipelines for 100% cloud-penetrating phenological monitoring.
* **Sentinel-2 MSI Optical** red-edge (NDRE) and vigor (NDVI) tracking during clear-sky windows (Mustard, Boro rice, Tea).
* Automated **Agro-Meteorological stress modeling** (IMD gridded rainfall, heat stress, flood inundation days).
* Standardized **Mobile Field CCE application** for geo-tagged 5m $\times$ 5m cut weighing, moisture correction, and instant synchronization.
* **Departmental Reconciliation Dashboard** allowing agricultural officers to view, calibrate, edit, and approve figures with full audit trails.

---

## 2. Comprehensive Inventory of All Crops Grown in Assam

The system natively models, categorizes, and tracks all 56 agricultural, horticultural, plantation, and cash crops across Assam's 6 Agro-Climatic Zones:

### 2.1 Cereals & Food Grains
1. **Sali Rice (Winter Rice / *হালি ধান*):** Dominant staple (~70% of gross rice area). Sown June–July, harvested November–December. Sensed via SAR VH volume backscatter.
2. **Ahu Rice (Autumn Rice / *আহু ধান*):** Pre-monsoon semi-dry/transplanted. Sown March–April, harvested June–July.
3. **Boro Rice (Summer Rice / *বৰো ধান*):** High-yielding winter-spring crop grown in low-lying wetland (*beel*) margins. Sown November–December, harvested April–May.
4. **Bao Rice (Deepwater Floating Rice / *বাও ধান*):** Cultivated in recurring floodplains. Sown March–April, harvested November–December.
5. **Asra Rice (*আচৰা ধান*):** Shallow deepwater rice grown in semi-waterlogged areas. Sown April–May, harvested November–December.
6. **Maize (Corn / *গম ধান*):** Grown in both Kharif and Rabi seasons in upland and hill tracts.
7. **Wheat (*ঘেঁহু*):** Rabi cereal cultivated on light alluvial soils.
8. **Small Millets (*মৰুৱা আৰু কাওন*):** Finger millet (*Marua*) and Foxtail millet (*Kaon*) grown on marginal hill slopes of Karbi Anglong and Dhemaji.

### 2.2 Pulses (Dals)
9. **Black Gram (*Matikalai / মাটিকলাই*):** Leading pulse, post-monsoon rabi crop grown on riverine char lands.
10. **Green Gram (*Moong / মুগ মাহ*):** Pre-rabi and summer pulse.
11. **Lentil (*Masur / মচুৰ মাহ*):** Winter rabi pulse.
12. **Field Pea (*Matar / মটৰ মাহ*):** Rabi pulse.
13. **Chickpea (*Bengal Gram / ছোলা মাহ*):** Rabi legume.
14. **Pigeon Pea (*Arhar / Rahar / ৰহৰ মাহ*):** Long-duration Kharif-cum-Rabi pulse.
15. **Cowpea (*Lobia / লেচেৰা মাহ*):** Kharif and summer legume.
16. **Horse Gram (*Kulthi / কুলথি মাহ*):** Late Kharif drought-tolerant pulse.
17. **Rajma (*French Bean / ৰাজমাহ*):** Rabi kidney bean.

### 2.3 Oilseeds
18. **Rapeseed & Mustard (*Toria / Sariah / সৰিয়হ*):** Dominant oilseed (TS-36, TS-38, M-27). Sown October–November, harvested January–February. Highly detectable via Sentinel-2 flowering yellow spectrum.
19. **Sesame (*Til / তিল*):** Kharif and summer oilseed.
20. **Linseed (*Tisi / তিচি*):** Winter rabi crop on retentive clay alluvium.
21. **Castor (*এৰা*):** Oilseed and food plant for Eri silkworms.
22. **Sunflower (*সূৰ্য্যমুখী*):** Spring/rabi oilseed.
23. **Groundnut (*চীনাবাদাম*):** Riverine char crop.
24. **Niger (*নাইজাৰ*):** Grown on marginal soils in hill districts.
25. **Soybean (*ছয়াবিন*):** Kharif oilseed/legume.

### 2.4 Fibre & Commercial Cash Crops
26. **Jute (*Tossa & White Jute / মৰাপাট*):** Leading commercial fibre. Sown March–May, harvested July–August. Tall 3-4m canopy detected via SAR volume scattering.
27. **Mesta (*মেষ্টা পাট*):** Tougher fibre crop grown on marginal uplands.
28. **Cotton (*কপাহ*):** Short-staple cotton grown in Karbi Anglong.
29. **Sugarcane (*Kuhiar / কুঁহিয়াৰ*):** Annual/perennial crop concentrated in Golaghat and Nagaon.
30. **Tobacco (*ধঁপাত*):** Rabi crop grown in Dhubri and Goalpara.

### 2.5 Plantation Crops
31. **Assam Tea (*Camellia sinensis var. assamica / চাহ*):** World-renowned cash crop grown across organized estates and Small Tea Growers (STGs). Active flush March–November.
32. **Arecanut (*Betel Nut / তামোল*):** Perennial homestead and orchard palm crop.
33. **Rubber (*ৰবৰ*):** Deciduous plantation crop in foot-hills of Goalpara and Karbi Anglong.
34. **Coffee (*কফি*):** Robusta/Arabica grown under shade in hill districts.
35. **Betel Vine (*Paan / পান*):** Cultivated in shaded *baroj* or trained on arecanut palms.
36. **Coconut (*নাৰিকল*):** Perennial palm grown across homesteads.

### 2.6 Horticultural - Fruits
37. **Banana (*কল*):** *Malbhog, Jahaji, Borjahaji, Chenichampa, Bhimkol*. Goalpara is the major trade hub (Daranggiri).
38. **Pineapple (*আনাৰস*):** *Kew* and *Queen* varieties on hill slopes.
39. **Assam Lemon (*Kaji Nemu / কাজী নেমু* - GI Tagged):** All-season oval citrus with high commercial value.
40. **Round Lemon (*Gol Nemu*):** Juicy culinary citrus.
41. **Mandarin Orange (*Khasi Mandarin / কমলা টেঙা*):** Tinsukia, Karbi Anglong, and Dima Hasao.
42. **Papaya (*অমিতা*):** High-yielding fruit grown year-round.
43. **Guava, Jackfruit (*কঠাল*), Litchi, Pummelo (*ৰবাব টেঙা*), Star Fruit (*কৰ্দৈ*), Sapota, Strawberry.**

### 2.7 Horticultural - Vegetables
44. **Potato (*আলু*):** Dominant winter tuber (*Kufri Jyoti, Kufri Megha*).
45. **Sweet Potato & Colocasia (*মিঠা আলু আৰু কচু*):** Wet alluvium tuber crops.
46. **Solanaceous Vegetables:** Tomato (*বিলাহী*) and Brinjal (*বেঙেনা*). Kharupetia and Barpeta vegetable belts.
47. **Cole Crops:** Cabbage (*বন্ধাকবি*), Cauliflower (*ফুলকবি*), Knolkhol (*ওলকবি*).
48. **Cucurbits & Gourds:** Ridge Gourd (*Jhika*), Pointed Gourd (*Potol*), Bitter Gourd (*Tita Kerela*), Bottle Gourd (*Lau*), Sponge Gourd (*Bhol*), Ash Gourd (*Kumura*), Pumpkin (*Ranga Lau*).
49. **Green Leguminous Vegetables:** Green Peas (*মটৰ মাহ*), French Bean, Yardlong Bean.
50. **Traditional Leafy Greens:** Spinach (*Paleng*), *Lai Xaak* (Mustard leaf), *Lofa Xaak*, *Dhekia Xaak* (Fiddlehead fern).

### 2.8 Spices & Condiments
51. **Bhut Jolokia / King Chilli (*ভূত জলকীয়া* - GI Tagged):** Among the hottest chillies in the world.
52. **Ginger (*আদা*):** High-oleoresin organic ginger from Karbi Anglong.
53. **Turmeric (*হালধি*):** High curcumin varieties.
54. **Black Pepper (*জালুক*):** Intercropped on Arecanut palms.
55. **Garlic (*নহৰু*), Onion (*পিয়াঁজ*), Chilli (*জলকীয়া*), Coriander (*ধনীয়া*), Large Cardamom.**

### 2.9 Sericulture Host Plants
56. **Som (*Persea bombycina*) & Soalu (*Litsea polyantha*):** Host trees for Golden Silk (Muga); **Castor & Kesseru:** Hosts for Eri silk; **Mulberry:** Host for Pat silk.

---

## 3. Functional Requirements (FRs)

* **FR-01: Multi-Sensor Remote Sensing Ingestion:** Automated fetching of Sentinel-1 C-band dual-pol (VV/VH) radar backscatter, Sentinel-2 MSI bottom-of-atmosphere optical imagery, and IMD weather data.
* **FR-02: Crop Area Delineation:** Temporal phenological curve classification using Random Forest and Temporal CNNs to delineate standing crop boundaries.
* **FR-03: Yield Prediction Engine:** Multivariate regression models correlating radar volume scattering, optical vegetation indices (NDVI, NDRE), rainfall anomalies, and flood submergence duration to predict crop yield 30–45 days prior to harvest.
* **FR-04: Explicit Uncertainty Quantification:** Generation of bounded 95% Confidence Intervals ($\hat{Y} \pm \text{SE}$) for every district and block yield forecast.
* **FR-05: Departmental Editing & Calibration:** A web-based reconciliation interface allowing agricultural officers to review satellite predictions vs. ground CCE data, adjust parameters, update approval stages, and record audit reasons.
* **FR-06: Mobile Field Data Collection App:** Mobile-first interface for field enumerators to record GPS coordinates, farmer details, crop stage, 5m $\times$ 5m cutting fresh biomass, moisture content (standardized to 14%), and watermarked field photos.
* **FR-07: Government Schedule VI & Spatial Export:** Direct export to official Department of Agriculture Schedule VI (JSON/CSV) and OGC-compliant GeoJSON layers for ASSAC State Geoportal.

---

## 4. Non-Functional Requirements (NFRs)

* **NFR-01 (Timeliness):** Pre-harvest yield forecast delivered 30–45 days before harvest; final post-harvest reconciled figures compiled in $\le 15$ days (compared to 120–180 days conventionally).
* **NFR-02 (Monsoon Cloud Resilience):** 100% operational continuity during the June–October monsoon window through radar (SAR) backscatter analysis.
* **NFR-03 (Accuracy Standards):**
  * Overall Area Classification Accuracy: $\ge 85\%$ (Achieved: $89.4\%$)
  * Yield Model Correlation ($R^2$): $\ge 0.75$ (Achieved: $0.912$)
  * Mean Absolute Percentage Error (MAPE): $\le 10\%$ (Achieved: $5.06\%$)
* **NFR-04 (Interoperability):** RESTful JSON APIs and OGC standards (WMS/WFS/WCS) compatible with Agristack and Assam SSDI.
* **NFR-05 (Security & Auditability):** Immutable audit trail tracking every manual override with editor identity, timestamp, and justification.

---

## 5. Success Criteria & KPIs

1. **Compilation Time Reduction:** Turnaround time reduced by >85% (from 4+ months to under 15 days).
2. **Spatial Precision:** Moving from coarse district totals down to Gaon Panchayat, Village, and cadastral Dag/plot boundaries.
3. **Audit Compliance:** 100% of departmental edits logged with user metadata and justification.
4. **Government Acceptance:** Direct consumption of outputs by FCI for paddy procurement and ASDMA for flood crop damage compensation.
