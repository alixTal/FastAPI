from fastapi import FastAPI
from pydantic import BaseModel
import time
import datetime


app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}


start = time.time()
while True:
    time.sleep(1)
    end = time.time()
    time_string = str(datetime.timedelta(seconds=end - start))
      print("\r"+time_string, end="")
    # print(time_string, end =" ")
