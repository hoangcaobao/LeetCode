class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens={}
        self.live=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=currentTime+self.live

    def renew(self, tokenId: str, currentTime: int) -> None:
        for token in self.tokens:
            if token==tokenId and self.tokens[token]>currentTime:
                self.tokens[token]=currentTime+self.live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        result=0
        for token in self.tokens:
            if self.tokens[token]>currentTime:
                result+=1
        return result


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)