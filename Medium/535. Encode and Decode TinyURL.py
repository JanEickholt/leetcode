import random
import string


class Codec:
    urls = {}
    chars = string.ascii_letters + string.digits

    def encode(self, longUrl):
        if longUrl not in self.urls:
            url = "http://tinyurl.com/" + "".join(
                random.choice(self.chars) for _ in range(6)
            )
            self.urls[url] = longUrl
            return url
        return self.urls[longUrl]

    def decode(self, shortUrl):
        return self.urls[shortUrl]
