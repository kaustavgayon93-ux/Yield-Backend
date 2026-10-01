from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class EstimateUpdate(BaseModel):
    area_hectares: float = Field(..., description="Estimated cropped area in Hectares")
    yield_mt_ha: float = Field(..., description="Forecasted yield in Metric Tonnes per Hectare")
    yield_uncertainty_ci95_lower: Optional[float] = Field(None, description="Lower bound of 95% Confidence Interval")
    yield_uncertainty_ci95_upper: Optional[float] = Field(None, description="Upper bound of 95% Confidence Interval")
    approval_stage: Optional[str] = Field("Department Approved", description="Stage: Draft, Pending Review, Field Verified, ASSAC Calibrated, Department Approved")
    updated_by: Optional[str] = Field("Departmental Officer", description="Reviewer name and designation")
    justification: Optional[str] = Field("Reconciliation with ground CCE points", description="Audit reasoning for manual change")
    notes: Optional[str] = Field(None, description="Additional technical notes")

class EstimateCreate(BaseModel):
    district_id: str
    district_name: str
    crop_id: str
    crop_name: str
    category: str = "Cereals & Food Grains"
    season: str = "Kharif 2026"
    area_hectares: float
    yield_mt_ha: float
    yield_uncertainty_ci95_lower: Optional[float] = None
    yield_uncertainty_ci95_upper: Optional[float] = None
    approval_stage: str = "Draft"
    notes: Optional[str] = None
    updated_by: Optional[str] = "System User"

class FieldRecordCreate(BaseModel):
    enumerator_name: str = Field(..., description="Name of field enumerator or ADO")
    enumerator_phone: str = Field(..., description="Contact phone of enumerator")
    district_id: str
    district_name: str
    block: str
    village: str
    dag_no: Optional[str] = None
    farmer_name: Optional[str] = None
    farmer_phone: Optional[str] = None
    crop_id: str
    crop_name: str
    variety: Optional[str] = None
    sowing_date: Optional[str] = None
    phenology_stage: str = "Maturity / Harvest Ready"
    plot_lat: float
    plot_lng: float
    gps_accuracy_m: float = 3.0
    cce_plot_shape: str = "Square (5m x 5m)"
    cce_plot_area_sqm: float = 25.0
    fresh_biomass_kg: float
    moisture_pct: float = 14.0
    flood_submergence_depth_cm: int = 0
    flood_inundation_days: int = 0
    pest_disease_incidence: Optional[str] = "Nil / Negligible"
    notes: Optional[str] = None
    photo_url: Optional[str] = None

class FieldRecordVerify(BaseModel):
    verification_status: str = "Verified & Approved"
    reviewer_notes: Optional[str] = None

class MLPredictRequest(BaseModel):
    sar_vh_db: float = Field(-13.5, description="Sentinel-1 SAR C-Band VH backscatter in dB")
    sar_vv_db: float = Field(-9.0, description="Sentinel-1 SAR C-Band VV backscatter in dB")
    optical_ndvi: float = Field(0.78, description="Sentinel-2 Optical NDVI (0.0 to 1.0)")
    optical_ndre: float = Field(0.48, description="Sentinel-2 Optical Red-Edge NDRE (0.0 to 1.0)")
    cumulative_rainfall_mm: float = Field(1420.0, description="Cumulative seasonal rainfall in mm from IMD")
    flood_inundation_days: int = Field(0, description="Days field was submerged under floodwater")
