with open('data.txt') as f:
    s = f.read()

# s = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def part_one():
    a = s.split(',')
    r = 0
    for e in a:
        t = 0
        for c in e:
            t = ((t+ord(c))*17)%256
        r += t
    return r



def part_two():
    import re

    a = [[] for _ in range(256)]
    r = 0
    for e in s.split(','):
        t = 0
        label,*_ = re.findall(r'(.+)([\-=])(\d*)',e)[0]
        for c in label:
            t = ((t+ord(c))*17)%256
        
        if '-' in e:
            i = next((i for i,x in enumerate(a[t]) if x.startswith(label)),-1)
            if i==-1: continue
            a[t].pop(i)

        if '=' in e:
            i = next((i for i,x in enumerate(a[t]) if x.startswith(label)),-1)
            if i==-1: a[t].append(e)
            else: a[t][i] = e
        
    for i,b in enumerate(a):
        r += sum((i+1)*(j+1)*int(re.split('[\-=]',e)[1]) for j,e in enumerate(b))
    
    return r


print(part_two())