# v.     p.
# cat   c*t      → true
# cat   *t       → true
# dog   c*t      → false

# * can match 0 or more chars in value
# pattern has 0 or 1 * in it only

# cat   *c**t    → true
# cat   *t*a*c*  → false
# aaaxxxbbyyyccczzddd.  aaa*bb*ccc*ddd -> true
                    

# pattern has arbitrary # of *s

        # caaat c*t => 
        #   c   *    t
        # c T   T    F
        # a
        # a
        # a
        # t
        
        
#         => c - * - t
#         pqd*abcd ->   p - q - d - * - a - b - c - d

# value = pqd wxy abcd

p = [aaa, bb, ccc, ddd]
v = "aaaxxxbbyyybbccczzddd" = 21

v[3:] = "xxxbbyyybbccczzddd" (bb)
    => [6, 11]
            v[6:] ="bbyyybbccczzddd" (ccc)
                => [14]
                    v[14:] => "ccczzddd" (ddd)
                    <= false
            v[11:] = "bbccczzddd"
                => 






# 1 - *   
# 2 - in between 
# 3 - *
        

def is_match(v, p):
    if "*" not in p:
        if v == p:
            return True
        return False
    
    if len(v) < len(p)-1:
        return False
        
    if p == "*":
        return True
    
#     if p[0] == "*" and v.endswith(p[1:]):
#         return True
    
#     if p[-1] == "*" and v.startswith(p[:-1]):
#         return True
    
    star_ind = p.find("*")
    if v.startswith(p[:star_ind]) and v.endswith(p[star_ind+1:]):
        return True
    
    return False
    

print(is_match("cat", "c*t"))
print(is_match("cat", "*t"))
print(is_match("dog", "c*t"))
print(is_match("caaaat", "c*t"))
print(is_match("cat", "cat*"))
print(is_match("cat", "ca*"))
print(is_match("cat", "cat*cat"))