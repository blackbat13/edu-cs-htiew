def read_file(path):
    with open(path, 'r') as f:
        return f.read().split()

def ex1(data, output):
    palindromes = []
    for word in data:
        if word == word[::-1]:
            palindromes.append(word)

    print(f"4.1\n{len(palindromes)}\n\n", file=output)
    return palindromes

def ex2(palindromes, output):
    families = dict()
    for word in palindromes:
        if len(word) in families:
            families[len(word)].append(word)
        else:
            families[len(word)] = [word]
    
    print(f"4.2\n{len(families)}", file=output)
    return families

def ex3(families, output):
    for key in families:
        print(" ".join(sorted(families[key])), file=output)

data = read_file("dane/slowa.txt")

with open("wyniki4.txt", "w") as output:
    palindromes = ex1(data, output)
    families = ex2(palindromes, output)

with open("rodziny.txt", "w") as output:
    ex3(families, output)
