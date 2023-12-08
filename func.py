from googletrans import Translator

translator = Translator()


def translate(q, target, source):
    return translator.translate(text=q, dest=target, src=source).text
