
class Message:
    def __init__(self, sent_on: int, src: str, dest: str, body: str):
        self.sent_on = sent_on
        self.src = src
        self.dest = dest
        self.body = body

    def __repr__(self):
        return str(self.__dict__)
