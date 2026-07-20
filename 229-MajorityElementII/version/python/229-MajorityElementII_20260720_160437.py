# Last updated: 7/20/2026, 4:04:37 PM
1class Solution:
2    def findWinners(self, matches):
3        losses = {}
4
5        for winner, loser in matches:
6            if winner not in losses:
7                losses[winner] = 0
8            losses[loser] = losses.get(loser, 0) + 1
9
10        zeroLoss = []
11        oneLoss = []
12
13        for player in sorted(losses):
14            if losses[player] == 0:
15                zeroLoss.append(player)
16            elif losses[player] == 1:
17                oneLoss.append(player)
18
19        return [zeroLoss, oneLoss]