from fastapi import FastAPI

from api.routers import task, done, calc

app = FastAPI()


app.include_router(task.router)
app.include_router(done.router)
app.include_router(calc.router)



@app.get("/hello")
async def hello():
    return {"message": "hello wooorld!"}