def max_K(front, back):
    for k in range(min(len(front), len(back)), 0, -1):
        if front[-k:] == back[:k]:
            return k
    return 0

def answer(virus):
    def dfs(used, vacine):
        if len(used) == len(virus):
            return len(vacine)
        minimum = float('inf')
        for i in range(len(virus)):
            if i not in used:
                k = max_K(vacine, virus[i])
                minimum = min(minimum, dfs(used | {i}, vacine + virus[i][k:]))
        return minimum
    return dfs(set(), '')


N = int(input())
virus = []
for _ in range(N):
    S = input()
    virus.append(S)
print(answer(virus))