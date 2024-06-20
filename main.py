from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import webbrowser

# Sample data
sample_data = [
    {
        "id": 1,
        "company_name": "Company A",
        "job_title": "Software Engineer",
        "industry": "Tech",
        "job_description": "Join our dynamic team!",
        "experience": "2+ years",
        "package_upto": "$100,000",
        "skills": ["Python", "FastAPI", "SQL"],
        "location": "Remote",
        "job_type": "Full-time",
        "email": "info@companyA.com"
    },
    {
        "id": 2,
        "company_name": "Company B",
        "job_title": "Data Analyst",
        "industry": "Analytics",
        "job_description": "Seeking data enthusiasts!",
        "experience": "1+ years",
        "package_upto": "$80,000",
        "skills": ["SQL", "Excel", "Statistics"],
        "location": "New York, NY",
        "job_type": "Part-time",
        "email": "info@companyB.com"
    }
]

# Pydantic model for job posting
class JobPosting(BaseModel):
    company_name: str
    job_title: str
    industry: str
    job_description: str
    experience: str
    package_upto: str
    skills: List[str]
    location: str
    job_type: str
    email: str

# FastAPI instance
app = FastAPI()

# GET method to fetch all job postings
@app.get("/jobs", response_model=List[JobPosting])
async def get_jobs():
    return sample_data

# POST method to create a new job posting
@app.post("/jobs", response_model=JobPosting)
async def create_job(job: JobPosting):
    job_data = job.dict()
    job_data["id"] = len(sample_data) + 1
    sample_data.append(job_data)
    return job_data

# Run the app with uvicorn
if __name__ == "__main__":
    import uvicorn

    # Open Swagger UI in the default web browser
    url = "http://localhost:8000/docs"
    webbrowser.open(url)

    # Start the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)
