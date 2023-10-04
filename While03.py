def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    c=0
    k=0
    while a<len(s):
        if s[a].isalpha() or s[a].isdigit():
            k+=1
        else:
            c+=1
        a+=1
    return c
print(main("akdgid@kd#$"))