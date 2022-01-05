def solution_1(s: str) -> bool:
    parentheses_dict = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for char in s:
        if char in parentheses_dict:
            stack.append(parentheses_dict[char])
        elif not stack or stack.pop() != char:
            return False
    return not stack
