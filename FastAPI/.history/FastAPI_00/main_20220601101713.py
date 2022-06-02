import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Medium API") 

@app.get("/")  # Decorator - assigning URL to a function
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)