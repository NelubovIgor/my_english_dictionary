from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

IAM_TOKEN = 'AQVNza2o8pCi_uNFw7vZHO6ghx_sYZHiyMWql8GE'
folder_id = 'b1gv28feb82msrc1q73h'
TRANSLATE_URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"

@app.get("/translate/")
async def translate():
    body = {
        "targetLanguageCode": 'ru',
        "texts": ['hello'],
        "folderId": folder_id,
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
