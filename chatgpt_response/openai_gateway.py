from chatgpt_response.responseParser import jsonParser
import os
import sys
import json
import requests


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


class OpenAiGateway:

    def __init__(self, jsonparser=jsonParser()):
        self.jsonparser = jsonparser

    def completion(self, requestData):

        endpoint = "https://api.openai.com/v1/chat/completions"
        api_key = os.getenv('CHATGPT_API_KEY')
        headers = {"Authorization": f"Bearer {api_key}",
                   "Content-Type": "application/json"}

        response = requests.post(
            endpoint, json=json.loads(requestData), headers=headers)
        print(response)
        print(response.text)
        self.jsonparser.set_api_response(response.text)

        self.jsonparser.parse_api_response()

        return self.jsonparser.prepare_json_from_api_response()
