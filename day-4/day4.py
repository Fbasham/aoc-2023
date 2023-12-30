# part one
# 24180 (too high)
with open('data.txt') as f:
    a = f.read().splitlines()
    r = 0
    for s in a:
        card,_ = s.split(': ')
        winning,cards = _.split(' | ')
        winning = [int(e) for e in winning.split() if e]
        cards = [int(e) for e in cards.split() if e]
        t = {e for e in cards if e in winning}
        if t: r += 2**(len(t)-1)