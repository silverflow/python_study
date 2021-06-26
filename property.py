class User:
    user_name: str
    e_mail: str

    def __init__(self, user_name, e_mail):
        self.user_name = user_name
        self.e_mail = e_mail

    def dd(self):
        return {"user_name": self.user_name, "e_mail": self.e_mail}


asdd = User("asdfasf", "asdfas")


print(asdd.dd())

