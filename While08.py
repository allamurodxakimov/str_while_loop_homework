def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    c=0
    k=""
    while a<len(s):
        if s[a].isdigit():
            if int(s[a])%2==1:
                k+=s[a]
                c+=1
        a+=1
    return k,c
print(main("56786543250"))
print(main("123456"))