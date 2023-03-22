#!/usr/bin/env python3

def filter_text(text): #cool ahh solution

    #lines = text.split('\n')
    #del lines[0]    #deletes first and last empty rows from text
    #del lines[-1]

    #list_a = [] #creates lists for x and xyz
    #list_b = []

    #for line in lines:
    #    if '#' in line: #finds the rules
    #        rules = line.split(' = ')   #splits into '# x' 'xyz'
    #        rules[0] = rules[0][2:]     #creates list 'x' 'xyz'

    #        list_a.append(rules[0])     #appends x
    #        list_b.append(rules[1])     #appends xyz
            
    #for i in range(len(list_a)):        #for item in list a
    #    for i2 in range(len(list_b)):   #for item in list b
    #        if list_a[i] in list_b[i2]: #check if item a is in item b
    #            return False            #return False if found

###################### boooring ahh solution
    rules = {}
    res = ""
    for l in text.split("\n"):
        # Rules starts with # symbol
        if l.startswith("#"):
            # removes trailing spaces from the rule
            (key, val) = map(str.strip, l[1:].split("="))
            rules[key] = val
    
    for key in rules:
        for value in rules.values():
            if key in value:
                return False
####################

    return True                         #return True if not found
