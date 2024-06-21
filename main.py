from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the data model
class Job(BaseModel):
    company_name: str
    job_title: str
    industry: str
    job_description: str
    experience: int
    package_upto: float
    skills: List[str]
    location: str
    job_type: str
    email: str

# In-memory storage for jobs
jobs = []

@app.post("/jobs/")
def create_job(job: Job):
    jobs.append(job)
    return job

@app.get("/jobs/")
def read_jobs():
    return jobs

@app.get("/jobs/{job_id}")
def read_job(job_id: int):
    if job_id >= len(jobs) or job_id < 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    if job_id >= len(jobs) or job_id < 0:
        raise HTTPException(status_code=404, detail="Job not found")
    jobs[job_id] = job
    return job

@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    if job_id >= len(jobs) or job_id < 0:
        raise HTTPException(status_code=404, detail="Job not found")
    deleted_job = jobs.pop(job_id)
    return deleted_job

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
