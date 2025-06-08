from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is our first route.", deprecated=True)
async def root():
    return {"message": "hello world!"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}

@app.get("/items")
async def list_items():
    return {"message": "list items route."}

@app.get("/users/me")
async def get_current_user():
    return {"message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}
