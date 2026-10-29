def alphabeta(depth, node, maximizing, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float('-inf')
        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(depth + 1, child, False, values, alpha, beta, max_depth)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(depth + 1, child, True, values, alpha, beta, max_depth)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3

result = alphabeta(0, 0, True, values, float('-inf'), float('inf'), max_depth)

print("Optimal value:", result)