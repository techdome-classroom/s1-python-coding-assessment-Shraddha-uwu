def decode_message( s: str, p: str) -> bool:

# write your code here
 
    def match_helper(i, j):
        if j == len(p):
            return i == len(s)  
        
        if j < len(p) and p[j] == '*':
            return match_helper(i, j + 1) or (i < len(s) and match_helper(i + 1, j))
        
        if i < len(s) and (p[j] == '?' or p[j] == s[i]):
            return match_helper(i + 1, j + 1)
        
        return False
    
    return match_helper(0, 0)


