from heapq import heappush,heappop,heapify
class Leaderboard:

    def __init__(self):
        self.d = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.d:
            self.d[playerId] += score
        else:
            self.d[playerId] = score

    def top(self, K: int) -> int:
        val = [v for k,v in self.d.items()]
        val.sort(reverse=True)
        sm = 0
        for i in range(K):
            sm += val[i]
        return sm
    
    def reset(self, playerId: int) -> None:
        del self.d[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
