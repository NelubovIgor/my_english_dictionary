#api
import requests
from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

TRANSLATE_URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"
IAM_TOKEN = 'Api-Key y0__xCWgMJuGMHdEyDU6ZOPEll9FHjhEwHOMOuKRN-VFzNI1TIF'
API_KEY = "y0__xCWgMJuGMHdEyDU6ZOPEll9FHjhEwHOMOuKRN-VFzNI1TIF"
folder_id = 'b1gv28feb82msrc1q73h'
target_language = 'ru'


@app.post("/translate/")
async def translate_text(
    text: str, target_language: str = "ru"
    # text: str = Body(..., embed=True),  # Параметр text в теле запроса
    # target_language: str = Body("ru")   # Параметр target_language в теле запроса

    ):

    text = "game"

    body = {
        "targetLanguageCode": target_language,
        "texts": [text],
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}",
        # "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post(TRANSLATE_URL,
        json = body,
        headers = headers
)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Ошибка при переводе текста")
    
    translated_text = response.json().get("translations", [])[0].get("text", "")
    
    return {"translated_text": translated_text}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
