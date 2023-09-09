"""	[Midterm 2020] One For All"""

def oneforall(gen):
    'allmight'
    generationname = ""
    #input name for gen
    for gene in range(1, int(gen) + 1):
        name = str(input())
        if gene == int(gen):
            generationname += (name + ('_') + str(gene))
        elif gene % 2 == 0:
            generationname += (name + ('-' * gene))
        else:
            generationname += (name + ('*' * gene))
    print(generationname)
oneforall(int(input()))
