
from requests import post

from telemost.types import AccessLevel, MeetingRequest, Meeting


class Telemost:
    def __init__(self, api_key):
        self._headers = {
            'Authorization': f'OAuth {api_key}',
            'content-type': 'application/json'
        }
        self._api_url = 'https://cloud-api.yandex.net/v1/telemost-api/conferences'

    def create_meeting(self, access_level: AccessLevel) -> Meeting:
        request = MeetingRequest(access_level)
        print(request.to_dict())
        response = post(url=self._api_url, headers=self._headers, json=request.to_dict())
        print(f"Response: {response.json()}")
        return Meeting.from_dict(response.json())
