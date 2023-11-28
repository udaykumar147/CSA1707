from math import log2

def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]
    if isMax:
        best = -1000
        for i in range(2):
            print("Enter score for child", i+1, "of node", nodeIndex+1, ":")
            val = int(input())
            best = max(best, minimax(depth+1, nodeIndex*2+i, False, scores, h))
        return best
    else:
        best = 1000
        for i in range(2):
            print("Enter score for child", i+1, "of node", nodeIndex+1, ":")
            val = int(input())
            best = min(best, minimax(depth+1, nodeIndex*2+i, True, scores, h))
        return best

scores = []
n = int(input("Enter the number of nodes: "))
for i in range(n):
    print("Enter score for node", i+1, ":")
    val = int(input())
    scores.append(val)

h = int(log2(n))
res = minimax(0, 0, True, scores, h)
print("The optimal value is:", res)

