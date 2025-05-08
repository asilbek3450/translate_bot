from googletrans import Translator

translator = Translator()

async def translate(q: str, target: str, source: str) -> str:
    return translator.translate(text=q, dest=target, src=source).text
