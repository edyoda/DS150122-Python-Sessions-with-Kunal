import copy
l = [1,2,"Sandeep","Chelli Gopal","Neeraj"]
h = copy.deepcopy(l)
h.pop()
h.append("Pls rewach the session")
print(l)
"""anjan = l
print(anjan)
anjan.append("Madhurika")
print(anjan,end=" ---- ")
print(l)"""
