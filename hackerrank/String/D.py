
# 1) 
S = input()
print("True" if len([s for s in S if s.isalnum()]) > 0 else "False")
print("True" if len([s for s in S if s.isalpha()]) > 0 else "False")
print("True" if len([s for s in S if s.isdigit()]) > 0 else "False")
print("True" if len([s for s in S if s.islower()]) > 0 else "False")
print("True" if len([s for s in S if s.isupper()]) > 0 else "False")

# 2)

S = input()
print (any(s.isalnum() for s in S))
print (any(s.isalpha() for s in S))
print (any(s.isdigit() for s in S))
print (any(s.islower() for s in S))
print (any(s.isupper() for s in S))
