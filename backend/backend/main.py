
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Privacy-Preserving Cloud Data Analytics",
    description="Secure dataset analytics and privacy protection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Privacy-Preserving Cloud Data Analytics API",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "project": "Privacy-Preserving Cloud Data Analytics"
    }


@app.get("/api/dashboard/summary")
def dashboard_summary():
    return {
        "total_datasets": 0,
        "total_analytics_jobs": 0,
        "privacy_protected": True,
        "message": "Dashboard API is ready"
    }
