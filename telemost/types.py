import json
from enum import Enum


class AccessLevel(Enum):
    PUBLIC = 'PUBLIC'
    ORGANIZATION = 'ORGANIZATION'


class LiveStreamResponse:
    def __init__(self, watch_url):
        self._watch_url = watch_url

    @classmethod
    def from_dict(cls, obj: dict):
        return cls(watch_url=obj.get('watch_url', None))

    @property
    def watch_url(self):
        return self._watch_url


class LiveStreamRequest:
    def __init__(self, access_level: AccessLevel, title, description):
        self._access_level = access_level
        self._title = title
        self._description = description

    def to_dict(self):
        response = {
            'access_level': self._access_level.value,
            'title': self._title,
            'description': self._description,
        }
        return response


class MeetingRequest:
    def __init__(
            self,
            meeting_access_level: AccessLevel,
            stream_access_level: AccessLevel = None,
            stream_title=None,
            stream_description=None,
    ):
        self._meeting_access_level = meeting_access_level
        self._live_stream = None
        if stream_access_level and stream_title:
            self._live_stream = LiveStreamRequest(stream_access_level, stream_title, stream_description)

    def to_dict(self):
        response = {
            'access_level': self._meeting_access_level.value,
        }
        if self._live_stream:
            response.update(
                {'live_stream': self._live_stream.to_dict()}
            )
        return response


class Meeting:
    def __init__(self, join_url, meeting_id, live_stream: LiveStreamResponse):
        self._join_url = join_url
        self._meeting_id = meeting_id
        self._live_stream = live_stream

    @classmethod
    def from_dict(cls, obj: dict):
        live_stream = None
        if 'live_stream' in obj:
            live_stream = LiveStreamResponse.from_dict(obj['live_stream'])
        return cls(
            join_url=obj.get('join_url', None),
            meeting_id=obj.get('id', None),
            live_stream=live_stream
        )

    @property
    def join_url(self):
        return self._join_url

    @property
    def meeting_id(self):
        return self._meeting_id

    @property
    def live_stream(self):
        return self._live_stream
