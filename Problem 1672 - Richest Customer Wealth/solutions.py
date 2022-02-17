def solution_1(accounts: list[list[int]]) -> int:
    return max(sum(account) for account in accounts)
