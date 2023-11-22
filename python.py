from fastapi import FastAPI

app = FastAPI()

@app.get("/")

@app.get("/home")    
def home():
    return {"sucesss":True,"message":"This is a defalult page"}

def home():
    return {"success":True,"message":"This is a home page"}