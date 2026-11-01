from fastapi import FastAPI

app = FastAPI(title="GameMetrics API")


@app.get("/")
async def root():
    return {"message": "GameMetrics API is running successfully!"}