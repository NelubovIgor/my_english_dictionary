import requests

TRANSLATE_URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"
IAM_TOKEN = 'AQVNza2o8pCi_uNFw7vZHO6ghx_sYZHiyMWql8GE'
folder_id = 'b1gv28feb82msrc1q73h'
target_language = 'ru'
texts = ["Hello", "World"]

body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(IAM_TOKEN)
}

response = requests.post(TRANSLATE_URL,
    json = body,
    headers = headers
)

print(response.text)
