def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c=0
    a=0
    while a<len(s):
        if s[a].isalpha():
            c+=1
        a+=1
    return c
print(main("Python 2022"))
print(main("ered2iri"))