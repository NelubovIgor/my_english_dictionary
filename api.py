from fastapi import FastAPI, HTTPException
import requests
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

IAM_TOKEN = os.getenv('IAM_TOKEN')
FOLDER_ID = os.getenv('FOLDER_ID')

TRANSLATE_URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"

@app.get("/translate/")
async def translate():
    body = {
        "targetLanguageCode": 'ru',
        "texts": ['hello'],
        "folderId": FOLDER_ID,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {IAM_TOKEN}"
    }

    response = requests.post(TRANSLATE_URL,
                             json=body, headers=headers)

    if response.status_code == 200:
        translated_text = response.json().get("translations", [{}])[0].get("text", "")
        return {"translated_text": translated_text}
    else:
        raise HTTPException(status_code=response.status_code, detail="Translation failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
