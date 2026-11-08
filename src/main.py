from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "World"}

@app.get("/api/v1/upload/{input}")
def display_data(input):
    return {"Test": input}

@app.post("/upload/data")
def upload(req):
    print("test")