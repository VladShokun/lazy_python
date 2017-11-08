firstnames = ['Anthony', 'Timothy', 'Bob', 'Sean', 'John']
lastnames = ['Smith', 'Parker', 'Conrad', 'Washington', 'Kennedy']
temporarylist = []
i = 0
b = 0
c = 0
for item in lastnames:
    for item in firstnames:
        temporarylist.insert(c, firstnames[i] + lastnames[b])
        i = i + 1
        c = c + 1
    if i > len(firstnames) - 1:

        # New block 1. Now writing current family name to Families.txt
        file = open("Families.txt", 'a')
        file.write(lastnames[b] + '\n')
        file.close()

        # New block 2. Now writing chain of cyborg-names to Smith.txt, Parker.txt etc.
        print(lastnames[b], '=', temporarylist)
        file = open(lastnames[b] + ".txt", 'w')
        temporarylist = str(temporarylist)
        file.write(temporarylist)
        temporarylist = []
        file.close()

        b = b + 1
        i = 0
        с = 0