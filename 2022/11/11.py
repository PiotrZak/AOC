# solution by marcodelmasttro
import re

class Monkey:
    def __init__(self,m,items,op,divtest,throw_if_true,throw_if_false):
        self.m = m
        self.items = items
        self.op = op
        self.divtest = divtest
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false
        self.inspected = 0
        self.worryMod = 0
        
    def turn(self,lowWorry=True):
        items_throw = []
        while len(self.items):
            old = self.items.pop(0)
            worry = eval(self.op)
            if lowWorry:
                worry //= 3
            if self.worryMod:
                worry %= self.worryMod
            if worry%self.divtest==0:
                items_throw.append((self.throw_if_true,worry))
            else:
                items_throw.append((self.throw_if_false,worry))
            self.inspected += 1
        return items_throw

def parseMonkey(d):
    m = int(re.findall(r"\d+", d[0])[0])
    items = [ int(i) for i in re.findall(r"\d+", d[1]) ]
    op = d[2].split(" = ")[1]
    div_test = int(re.findall(r"\d+", d[3])[0])
    throw_if_true = int(re.findall(r"\d+", d[4])[0])
    throw_if_false = int(re.findall(r"\d+", d[5])[0])
    monkey = Monkey(m, items, op, div_test, throw_if_true, throw_if_false)
    return monkey
    
def parse11(filename):
    with open(filename) as f:
        data = [ parseMonkey(  m.split("\n") ) for m in f.read().strip().split("\n\n") ]
        return data

        

def monkeyBusiness(monkeys, turns = 20, lowWorry=True, verbose=True):
    # For Part 2: no need to keep excessively high worry levels, since they'll be tested again each monkey
    # divtest value. I can keep only the reminder of the product of all monkeys' divtest values (all primes, of course!)
    worryMod = 1
    for monkey in monkeys:
        worryMod *= monkey.divtest
    for monkey in monkeys:
        monkey.worryMod = worryMod
    
    for turn in range(1,turns+1):
        for monkey in monkeys:
            throw = monkey.turn(lowWorry) # lowWorry disable division by 3 for Part 2
            for recipient,item in throw:
                monkeys[recipient].items.append(item)
        if verbose:
            print("After round {}, the monkeys are holding items with these worry levels:".format(turn))
            for monkey in monkeys:
                print("Monkey {}: {}".format(monkey.m,monkey.items))
            print("")
    inspected = [ m.inspected for m in monkeys ]
    if verbose:
        for m,i in enumerate(inspected):
            print("Monkey {} inspected items {} times".format(m,i))
        print()
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]



monkeys = parse11("11.txt")
monkeyBusiness(monkeys, turns = 20, verbose=True)
