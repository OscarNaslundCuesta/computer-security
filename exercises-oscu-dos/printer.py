#!/usr/bin/env python3


def decompress(text):
    rules = {}
    res = ""
    for l in text.split("\n"):
        # Rules starts with # symbol
        if l.startswith("#"):
            # removes trailing spaces from the rule
            (key, val) = map(str.strip, l[1:].split("="))
            rules[key] = val
            continue
        res += l + "\n"
    while True:
        rule_aplied = False
        for key in rules:
            if key in res:
                res = res.replace(key, rules[key])
                rule_aplied = True
        # repeat substitutions while at least one rule has been applied
        if not rule_aplied:
            break
    return res


if __name__ == '__main__':
    res = decompress("""
# H = and
# AR = are
# brh = brotherhood
All human beings AR born free H equal in dignity H rights. They
AR endowed with reason H conscience H should act towards one
another in a spirit of brh. 
    """)
    
    print(res)
