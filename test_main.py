

group=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

total_g_el=[i for j in group for i in j ]
# total_g_el=[i for j in group for i in j]
# print(total_g_el)

a=[[0]*3]*5
# print(a)


def one():
    
    a=4
    b=5
    return a,b

s,d=one()

print(s)
print(d)
