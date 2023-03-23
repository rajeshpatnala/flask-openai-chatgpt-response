import unittest
from unittest.mock import MagicMock

from chatgpt_response.pilotService import PilotService


class pilotServiceTest(unittest.TestCase):

    openai_gateway = MagicMock()
    pilot_service = PilotService(openai_gateway)

    def test_service_call_gateway(self):

        query = "command to find files that start with xyz"

        response = self.pilot_service.ask(query)

        assert self.openai_gateway.completion.iscalled
