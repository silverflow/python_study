class Validation:
    def __init__(self, validation_function, error_msg: str) -> None:
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:
    def __init__(self, *validations) -> None:
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    desciptor = Field(
        Validation(lambda x: isinstance(x, (int, float)), "는 숫자가 아님"),
        Validation(lambda x: x >= 0, "는 0보다 작음"),
    )


if __name__ == "__main__":
    client = ClientClass()
    client.desciptor = 42
    print(client.desciptor)

    client.desciptor = -121
    print(client.desciptor)
