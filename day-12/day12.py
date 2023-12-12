with open('data.txt') as f:
    a = f.read().splitlines()

# a = '''???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1'''

def part_one():
    from itertools import product
    import re
    
    t = [(('#.' if e=='?' else e for e in s.split()[0]),list(map(int,s.split()[1].split(',')))) for s in a]
    r = 0
    for x,y in t:
        for p in product(*x):
            s = ''.join(p)
            m = [len(e) for e in re.findall('#+',s)]
            if m==y:
                print(s,y)
                r += 1
    return r
