# Assignment 4: Fractional Knapsack using Greedy Method

n = int(input("Number of items: "))

values = list(map(float, input("Values (space separated): ").split()))

weights = list(map(float, input("Weights (space separated): ").split()))

cap = float(input("Knapsack capacity: "))

if len(values) != n or len(weights) != n or min(weights) <= 0:
    raise SystemExit("Enter n values and n positive weights")


items = sorted(
    zip(range(1, n + 1), values, weights),
    key=lambda x: x[1] / x[2],
    reverse=True
)

left, total = cap, 0.0

print("\nItem  Value  Weight  Ratio  Taken   Profit")

for i, v, w in items:

    frac = max(0.0, min(1.0, left / w))

    # Whole item, a fraction, or nothing

    left -= frac * w
    total += frac * v

    print("%-5d %-6g %-7g %-6.2f %-7.2f %.2f"
          % (i, v, w, v / w, frac, frac * v))


print("\nMaximum profit = %.2f" % total)