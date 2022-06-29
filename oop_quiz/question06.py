import re


class HackerLanguage:
    def __init__(self):
        self.buffer = []

    def write(self, text):
        self.buffer.extend(text)

    def delete(self, length):
        self.buffer = self.buffer[:-length]

    def send(self):
        return "".join(
            bin(ord(c))[2:] if c.isalpha() else c for c in self.buffer
        ).replace(" ", "1000000")

    def read(self, coded):
        return re.sub(
            r"[01]{7}", lambda e: chr(int(e[0], 2)) if e[0] != "1000000" else " ", coded
        )


msg_4 = HackerLanguage()
millionaires = msg_4.write(
    "I have 1000000 dollars. You have 1000000 dollars. He has 1000000 dollars. In all: 1000000 + 1000000 + 1000000 = 3000000"
)
crypt = msg_4.send()
decrypt = msg_4.read(crypt)
print(decrypt)
