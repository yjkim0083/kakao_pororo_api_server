# -*- coding:utf-8 -*-
# app.py
import uvicorn
from typing import Optional
from fastapi import FastAPI

from pororo import Pororo

app = FastAPI()

mt = Pororo(task="translation", lang="multi")


@app.get("/")
def read_root():
    #result = mt("나는 모비젠이라는 회사에 다닌다.", src="ko", tgt="en")
    return {"Hello": "World"}


@app.get("/translation/{text}")
def read_root(text: str):
    return {"ko": mt(text, src="en", tgt="ko"), "en": text}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
