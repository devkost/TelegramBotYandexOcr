import base64
import requests
import json

from addition.useful_functions import *

API_URL = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"
API_KEY = "AQVN0_eK53FIcSQtggB3fyuKCJa8YHmqOVHNrk_g"


def request_to_convert( content, model_type ):
    try:
        content = encode_file( content )
        request = {
            "data": {
                "mimeType": "JPG",
                "languageCodes": [ "ru", "en" ],
                "model": model_type or "page",
                "content": content,
            },
            "headers": {
                "Content-Type": "application/json",
                "x-folder-id": "b1g8jqtaonfovmr7sdkb",
                "Authorization": "Api-Key {}".format( API_KEY )
            }
        }

        response = requests.post(
            url=API_URL,
            headers=request["headers"],
            data=json.dumps(request["data"])
        )

        response.raise_for_status()
        response_data = response.json()
        full_text = response_data[ "result" ][ "textAnnotation" ][ "fullText" ]

        if not full_text:
            return "Не удалось распознать текст на изображении. Отправьте изображение снова."

        response = len( full_text ) > 50 and fix_text_hyphens( full_text ) or full_text
        return highlight_important( response )

    except requests.exceptions.RequestException as e:
        return f"Ошибка сети: {str(e)}"

    except json.JSONDecodeError as e:
        return "Неверный формат ответа от сервера. Попробуйте отправить изображение позже."

    except KeyError as e:
        return "Ошибка обработки данных сервера. Попробуйте отправить изображение позже."

    except Exception as e:
        return f"Произошла ошибка: {str(e)}. Попробуйте отправить изображение позже."

def encode_file( photo_bytes ):
    try:
        return base64.b64encode( photo_bytes ).decode( "utf-8" )
    except Exception as e:
        return e