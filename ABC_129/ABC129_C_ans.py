N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

MOD = 10**9 + 7

dp = [1 for _ in range(N + 1)]
#print(dp)
for A in a:
    dp[A] = 0
for i in range(2, N + 1):
    #print(dp[i])
    if dp[i]:
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
ans = dp[N]
print(ans)
#edanokazu wo tasiteru?
