def uppercase(str):
    i = 0
    for char in str:
        value = ord(char)
        if value >= 97 and value <= 122:
            char = chr(value - 32)
        if i == len(str) - 1:
            print(f"{char}")
        else:
            print("{char}", end='')
        i = i + 1
