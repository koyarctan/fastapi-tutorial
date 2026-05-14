from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/items/{item_id}")#ここのitem_idが関数の引数になるので注意。
async def read_item(item_id: int):#型ヒントもつけることができる。この場合、URLでは文字列だった３をAPIが整数に変換して入力してくれる。
    return {"item_id": item_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}
