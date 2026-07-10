class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append(i)
        t=0
        while q:
            i = q.popleft()
            tickets[i] -= 1
            t += 1
            if tickets[i] == 0:
                if i == k:
                    return t
            else:
                q.append(i)