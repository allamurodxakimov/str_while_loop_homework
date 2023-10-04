def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    c=0
    k=""
    while a<len(s):
        if s[a].isupper():
            k+=s[a]
            c+=1
        a+=1
    return k,c
print(main("CodeschoolUz"))