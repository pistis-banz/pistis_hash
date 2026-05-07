class PB64:
    def __init__(self):
        self.h = 0x5042535449533634

    def rotate_left(self, x, n):
        return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

    def hash(self, message):
        h = self.h

        data = message.encode("utf-8")

        for i, byte in enumerate(data):
            h ^= byte
            h = self.rotate_left(h, (i % 13) + 1)
            h = (h * 0x9E3779B185EBCA87) & 0xFFFFFFFFFFFFFFFF
            h ^= 0x5042

        return f"{h:016x}"


algo = PB64()

texte = input("Entrer un texte : ")

print("Hash PB64 :", algo.hash(texte))