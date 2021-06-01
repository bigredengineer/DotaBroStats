import json


class OpenDotaError(Exception):
    def __init__(self, status_code, message):
        self.message = f"Status: {status_code}. Error: {message}"
        super().__init__(self.message)


class MockRequest:
    """Used for UnitTests"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.ok = True if status_code == 200 else False
        self.text = message

    def json(self):
        return json.loads(self.text)
