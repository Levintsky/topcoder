"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""


class Codec:
    alphabet = string.ascii_letters + "0123456789"

    def __init__(self):
        self.short_2_long = {}
        self.long_2_short = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.long_2_short:
            while longUrl not in self.long_2_short:
                code = "".join(random.choice(Codec.alphabet) for _ in range(6))
                if code not in self.long_2_short:
                    self.long_2_short[longUrl] = code
                    self.short_2_long[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short_2_long[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
