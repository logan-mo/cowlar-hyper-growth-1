from fastapi import FastAPI, File, UploadFile
from DataIntegration import LLM
import openai
import os

# To run app, Use:
# uvicorn app:app --reload

# api_key = ""
# os.environ["OPENAI_API_KEY"] = api_key
# openai.api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI()
model = LLM()


@app.get("/")
def read_root():
    return {
        "response": "Server is running.\n To read the documentation, go to http://127.0.0.1:8000/docs#/"
    }


"""
POST {
    user_id: ,
    source_name: ,
    url: 
}
or:
POST {
    user_id: ,
    source_name: ,
    file: 
}
"""


@app.post("/add_source/")
async def add_source(
    user_id: str, source_name: str, url: str = None, file: UploadFile = None
):
    if url is not None:
        return model.add_to_index(user_id, source_name, url)
    elif file is not None and source_name == "txt":
        return model.add_to_index(user_id, source_name, file=file)
    else:
        return {"response": "Please provide either a URL or a file."}


# http://127.0.0.1:8000/get_response/?&user_id=101&prompt=What happend to the Maergo rebrand?
# http://127.0.0.1:8000/get_response/?&user_id=101&prompt=How can ecommerce retailers reduce their carbon footprint?


"""
GET {
    user_id: ,
    prompt: ,
}
"""


@app.get("/get_response/")
async def get_response(user_id: str, prompt: str):
    response = model.generate_response(user_id, prompt)
    if type(response) == dict:
        return {"response": response["response"]}
    elif type(response) == str:
        return {"response": response}
    return {"response": response.response}


@app.get("/reset_chat/")
async def get_response(session: str):
    model.clear_engine(session)
    return {"response": "Chat Reset"}
