def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a=0
    c=0
    k=""
    while a<len(s):
        if s[a].isalpha() and s[a]!='a' and s[a]!='e' and s[a]!='i' and s[a]!='o' and s[a]!='u' and s[a]!='A' and s[a]!='E' and s[a]!='I' and s[a]!='O' and s[a]!='U':
            k+=s[a]
            c+=1
        a+=1
    return k,c
print(main("CodeschoolUz"))