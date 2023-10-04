def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    c=0
    while a<len(s):
        c+=int(s[a])
        a+=1
    return c
print(main("123456789"))