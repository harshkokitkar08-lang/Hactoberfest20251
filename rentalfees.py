def calculateRentalFee(N, t, m):
    # Step 1: Check validity of rental duration
    if N <= 0:
        return "Invalid rental duration"

    # Step 2: Base daily fee based on rental days
    if 1 <= N <= 3:
        daily_fee = 1.0
    elif 4 <= N <= 7:
        daily_fee = 0.75
    else:  # N >= 8
        daily_fee = 0.50

    total_fee = N * daily_fee

    # Step 3: Adjustments based on book type
    if t == 1:  # New Release
        total_fee += 2
    elif t == 2:  # Classic
        total_fee *= 0.90  # 10% discount
    # t == 3 → no changes

    # Step 4: Membership adjustment
    if m == 1:  # Premium
        total_fee *= 0.90  # 10% discount
    # m == 2 → no changes

    # Step 5: Return final fee (integer)
    return int(total_fee)


# --- Driver Code (needed for Newton School) ---
if __name__ == "__main__":
    N = int(input().strip())
    t = int(input().strip())
    m = int(input().strip())
    print(calculateRentalFee(N, t, m))
