from math import log2

def alphabeta(depth, nodeIndex, alpha, beta, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]
    if isMax:
        best = -1000
        for i in range(2):
            print("Enter score for child", i+1, "of node", nodeIndex+1, ":")
            val = int(input())
            best = max(best, alphabeta(depth+1, nodeIndex*2+i, alpha, beta, False, scores, h))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            print("Enter score for child", i+1, "of node", nodeIndex+1, ":")
            val = int(input())
            best = min(best, alphabeta(depth+1, nodeIndex*2+i, alpha, beta, True, scores, h))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = []
n = int(input("Enter the number of nodes: "))
for i in range(n):
    print("Enter score for node", i+1, ":")
    val = int(input())
    scores.append(val)

h = int(log2(n))
res = alphabeta(0, 0, -1000, 1000, True, scores, h)
print("The optimal value is:", res)
