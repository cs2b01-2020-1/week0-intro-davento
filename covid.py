genName = ["AY274119", "AY278488.2", "MN908947", "MN908947", "MN988669"]
genStr = [0 for x in range(5)]

def longest(list):
    n = 0
    for i in list:
        if(len(i) > n):
            n = len(i)
    return (n)

def calcPercent (genA, genB):
    n = 0
    l = len(genA) if len(genA) < len(genB) else len(genB)
    for i in range(l):
        if (genA[i] == genB[i]):
            n += 1
    return (round(n / len(genA) * 100, 2))

for x in range(len(genName)):
    line = open(genName[x] + ".txt", "r")
    line.readline()
    genStr[x] = line.read()
    genStr[x] = genStr[x].replace('\n', '')

print ("Los resultados de la comparación de genes son:\n")
print (" " * longest(genName), end = "")

for name in range(len(genName)):
    print (genName[name], end = "\t")
print()

for i in range (len(genName)):
    print(genName[i], end = " " * (longest(genName) - len(genName[i])))
    for j in range(len(genName)):
        print(" " * (len(genName[j]) - 5), end = "")
        print(str(calcPercent(genStr[i], genStr[j])).ljust(5), end = '\t')
    print()
