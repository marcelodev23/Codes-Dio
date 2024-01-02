from fastapi import FastAPI

app = FastAPI(title = 'WorkoutAPI')
@app.get('/')
async def root():
    return 'opa porrra'
