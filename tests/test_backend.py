"""
FastAPI Backend Test Suite for GeoAgri-Assam (NESFIC-D-12)
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "OPERATIONAL"
    print("[PASS] GET / passed")

def test_crops():
    response = client.get("/api/crops")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert json_data["count"] >= 50
    print(f"[PASS] GET /api/crops passed ({json_data['count']} crops)")

def test_districts():
    response = client.get("/api/districts")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert json_data["count"] >= 10
    print(f"[PASS] GET /api/districts passed ({json_data['count']} districts)")

def test_estimates():
    response = client.get("/api/estimates")
    assert response.status_code == 200
    assert response.json()["success"] is True
    print("[PASS] GET /api/estimates passed")

def test_ml_predict():
    payload = {
        "sar_vh_db": -13.2,
        "sar_vv_db": -8.5,
        "optical_ndvi": 0.82,
        "optical_ndre": 0.54,
        "cumulative_rainfall_mm": 1420.0,
        "flood_inundation_days": 0
    }
    response = client.post("/api/ml/predict", json=payload)
    assert response.status_code == 200
    data = response.json()["data"]
    assert "predicted_yield_mt_ha" in data
    assert "ci95_lower_mt_ha" in data
    assert data["predicted_yield_mt_ha"] > 0
    print(f"[PASS] POST /api/ml/predict passed (Predicted Yield: {data['predicted_yield_mt_ha']} MT/Ha)")

def test_cce_submission():
    payload = {
        "enumerator_name": "Test ADO",
        "enumerator_phone": "+91 94350 00000",
        "district_id": "nagaon",
        "district_name": "Nagaon",
        "block": "Raha",
        "village": "Nonoi",
        "crop_id": "rice-sali",
        "crop_name": "Sali Rice",
        "plot_lat": 26.21,
        "plot_lng": 92.51,
        "fresh_biomass_kg": 9.2,
        "moisture_pct": 14.0
    }
    response = client.post("/api/field-records", json=payload)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["computed_yield_mt_ha"] == 3.68
    print(f"[PASS] POST /api/field-records passed (Computed Yield: {data['computed_yield_mt_ha']} MT/Ha)")

if __name__ == "__main__":
    test_root()
    test_crops()
    test_districts()
    test_estimates()
    test_ml_predict()
    test_cce_submission()
    print("\nALL FASTAPI BACKEND TESTS PASSED SUCCESSFULLY!")
