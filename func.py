import requests


def translate(q, target, source):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = {
        "q": q,
        "target": target,  # qaysi tilga tarjima qilish
        "source": source  # qaysi til dan
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "0e1e80d5bfmsh213ed89c8e67ef5p10d6b3jsn0c4cbb51f1b1",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.json())
    return response.json()['data']['translations'][0]['translatedText']
