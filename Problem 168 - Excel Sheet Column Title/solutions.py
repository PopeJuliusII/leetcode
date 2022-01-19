def solution_1(columnNumber: int) -> str:
    row_name = ""
    while columnNumber:
        columnNumber, char_index = divmod(columnNumber - 1, 26)
        row_name = chr(65 + char_index) + row_name
    return row_name
