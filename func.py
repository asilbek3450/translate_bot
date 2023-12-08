from googletrans import Translator

translator = Translator()


def translate(q, target, source):
    return translator.translate(q, dest=target, src=source).text
