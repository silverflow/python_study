from datetime import datetime


def hide_field(field) -> str:
    return "***deleted information"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    return event_field


class EventSerializer:
    def __init__(self, serializtion_fields: dict) -> None:
        self.serializtion_fields = serializtion_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serializtion:
    def __init__(self, **transformations) -> None:
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serializtion(
    username=show_original, password=hide_field, ip=show_original, timestamp=format_time
)
class LoginEvent:
    def __init__(self, username, password, ip, timestamp) -> None:
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp
