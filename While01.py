def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c=0
    a=0
    while a<len(s):
        if s[a].isdigit():
            c+=1
        a+=1
    return c
print(main("python 2022"))
print(main("e324xE"))