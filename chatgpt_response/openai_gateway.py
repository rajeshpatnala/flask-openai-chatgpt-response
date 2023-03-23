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
        api_key = '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'
        headers = {"Authorization": f"Bearer {api_key}",
                   "Content-Type": "application/json"}

        response = requests.post(
            endpoint, json=json.loads(requestData), headers=headers)

        self.jsonparser.set_api_response(response.text)

        self.jsonparser.parse_api_response()

        return self.jsonparser.prepare_json_from_api_response()
