import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    if(text == None):
        payload = {
            "recipient": {"id": id},
            "message": {"text": "請輸入文字"}
        }
    else:
        payload = {
            "recipient": {"id": id},
            "message": {"text": text}
        }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text


def send_image_message(id, picurl):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    if url is None:
        return -1
    else:
        payload = {
            "recipient": {"id": id},
            "message": {
                "attachment": {
                  "type": "image",
                  "payload": {
                    "url": picurl,
                    "is_reusable": "true"
                  }
                }
            }
        }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
