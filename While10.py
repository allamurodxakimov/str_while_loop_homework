def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    c=0
    k=""
    while a<len(s):
        if int(s[a])%2==1:
            k+=s[a]
            c+=int(s[a])
        a+=1
    return k,c
print(main("12345"))