import re
from fractions import Fraction
from sys import stdin

# Part 1
# (m:={s[:4]:(lambda e:lambda:e if len(e)<9 else '(%s%s%s)'%(m[e[:4]](),e[5],m[e[7:11]]()))(s[6:-1]) for s in stdin.readlines()}) and print(eval(m['root']()))

# Part 2
#(m:={s[:4]:(lambda e:lambda:'Fraction(%s)'%e if len(e)<9 else '(%s%s%s)'%(m[e[:4]](),e[5],m[e[7:11]]()))(s[6:-1] if s[:4]!='root' else s[6:11]+'-'+s[12:]) for s in stdin.readlines()}) and (t:=[m.update({'humn':(lambda:x)}) or eval(m['root']()) for x in [0,1]]) and print(t[0]/(t[0]-t[1]))


# opRe = re.compile("(\w+): (\w+) ([+\-*/]) (\w+)")
# numRe = re.compile("(\w+): (\d+)")

# ops = {
# 	"+": add,
# 	"-": sub,
# 	"*": mul,
# 	"/": div,
# }

# monkeys[m.group(1)] = (ops[m.group(3)], m.group(2), m.group(4))

# lone number -> just yell
# aaaa + bbbb -> wait for those - then yell sum
# aaaa - bbbb -> wait for those - then yell diff
# aaaa * bbbb -> wait for those - then yell multiply
# aaaa / bbbb -> wait for those - then yell divide

#what number monkey name 'root' yell?

#monkeys = tuple()
monkeys = dict()

def recursive_monkeys(monkeys, name):
    monkey_to_find = monkeys[name]
    print(monkey_to_find)

    try:
        number = float(monkey_to_find)
    except ValueError:
        pass
    else:
        return number

    if len(monkey_to_find) > 1:
        lm, operator, rm = monkey_to_find.split()
        lm = recursive_monkeys(monkeys, lm)
        rm = recursive_monkeys(monkeys, rm)
        
        match (operator):
            case "+":
                return lm + rm
            case "-":
                return lm - rm
            case "*":
                return lm * rm
            case "/":
                return lm / rm
            case "==":
                return (lm - rm) * (lm - rm)

   # for monkey in monkeys:


for line in open("21.txt").readlines():
    monkey_value = re.findall('\d+', line)

    if len(monkey_value) == 1:
        monkey_value = monkey_value[0]
    if (len(monkey_value) == 0):
        monkey_value = line.split(': ')[1].strip('\n')

    monkeys[line[0:4]] = monkey_value
    #monkeys += ((line[0:4], monkey_value), )


root = recursive_monkeys(monkeys, 'root')
print(root)
    


# M = dict()

# def calc(m,p2=True):
#     if m == 'root' and p2:
#         a,o,b = M[m]
#         return calc(a) == 42130890593816,calc(a),calc(b)
#     if type(M[m]) is int:
#         return M[m]
#     else:
#         a,o,b = M[m]
#         if o == '+':
#             return calc(a) + calc(b)
#         if o == '-':
#             return calc(a) - calc(b)
#         if o == '*':
#             return calc(a) * calc(b)
#         if o == '/':
#             return calc(a) // calc(b)


# a = 0                                
# steps = 1000000000000                
# while not a: 
#     a,b,c =calc('root', True)
#     if b<c:                        
#         M['humn'] -= steps
#         steps = steps //10
#     if steps == 0:
#         break
#     M['humn'] += steps
# print('part2:', M['humn'])