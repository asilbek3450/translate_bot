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
        "X-RapidAPI-Key": "0be29fa1c1msha32456cb3243efbp11a1c9jsna78218136690",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.json())
    return response.json()['data']['translations'][0]['translatedText']
