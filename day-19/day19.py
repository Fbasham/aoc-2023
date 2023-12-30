with open('data.txt') as f:
    s = f.read()


# s = '''px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}'''


def parse(s):
    a,b = map(str.splitlines,s.split('\n\n'))

    da = {}
    for e in a:
        da[e[:e.find('{')]] = [x.split(':') for x in e[e.find('{')+1:-1].split(',')]

    db = []
    for e in b:
        db.append({x.split('=')[0]:int(x.split('=')[1]) for x in e[1:-1].split(',')})

    return da,db

def part_one():
    d,b = parse(s)
    r = 0
    for e in b:
        k = 'in'
        while k not in 'AR':
            for t in d[k]:
                if len(t)==1:
                    k = t[0]
                    break
                elif eval(f"e['{t[0][:1]}']{t[0][1:]}"):
                    k = t[1]
                    break
                else:
                    continue
        if k=='A':
            r += sum(e.values())
    
    return r

print(part_one())