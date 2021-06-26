class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


token = BaseTokenizer("24asdkln-3njsk389sd-3ji901ci-3ljnj134nkl124nl")
print(token)
print(list(token))
