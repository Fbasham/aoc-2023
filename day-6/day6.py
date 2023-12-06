# part one
time = [48,93,85,95]
dist = [296,1928,1236,1391]
r = 1
for t,d in zip(time,dist):
    a = [i*(t-i) for i in range(1,t)]
    r *= sum(e>d for e in a)
print(r)


# part two
t = 48938595
d = 296192812361391
r = sum(i*(t-i)>d for i in range(1,t))
print(r)