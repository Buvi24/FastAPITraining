from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}

@app.get("/about")
def about():
    return {"page":"About","Author":"Buvi"}
@app.get("/health")
def health():
    return {"status":"ok"}
#POST request
@app.post("/create")
def create_something():
    return {"message":"Created"}
#Path Parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","USN":usn}
#Path parameters with type hint
@app.get("/candidate/{roll}")
def get_candidate(roll:int):
    return {"Result":"Distinction","Roll no":"roll","type":str(type(roll))}


           