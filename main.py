from fastapi import FastAPI, HTTPException
from info import COMPANIES  # import your data from info.py

app = FastAPI()

@app.get("/companies/{company_id}")
def get_company(company_id: int):
    """
    Fetch company info by ID.
    Example: GET /companies/1
    """
    company = COMPANIES.get(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"id": company_id, "data": company}
