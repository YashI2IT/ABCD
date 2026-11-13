# Assignment 3: 0/1 Knapsack using Dynamic Programming

n = int(input("Number of items: "))

wt = list(map(int, input("Weights (space separated): ").split()))

val = list(map(int, input("Values (space separated): ").split()))

W = int(input("Knapsack capacity: "))

if len(wt) != n or len(val) != n:
    raise SystemExit("Enter %d weights and %d values" % (n, n))


# dp[i][w] = best value using the first i items with capacity w

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):

        dp[i][w] = dp[i - 1][w]  # Skip item i

        if wt[i - 1] <= w:  # Or take it
            dp[i][w] = max(
                dp[i][w],
                val[i - 1] + dp[i - 1][w - wt[i - 1]]
            )


print("\nDP table (rows = items, columns = capacity):")

print("      " + " ".join("%3d" % w for w in range(W + 1)))

for i in range(n + 1):
    print("i=%-2d  " % i + " ".join("%3d" % x for x in dp[i]))


# Backtracking to find selected items

chosen, w = [], W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        chosen.append(i)
        w -= wt[i - 1]

chosen.reverse()


print("\nMaximum value =", dp[n][W])

print("Items chosen  =", chosen,
      "| total weight =", sum(wt[i - 1] for i in chosen))


# Brute-force check

if n <= 15:
    best = max(
        sum(val[i] for i in range(n) if m >> i & 1)
        for m in range(1 << n)
        if sum(wt[i] for i in range(n) if m >> i & 1) <= W
    )

    print("Brute force check (all 2^n subsets) =", best,
          "| matches DP:", best == dp[n][W])