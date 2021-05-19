DNA = open("C:/Users/lenartc/downloads/rosalind_revc (1).txt").read()
DNA = DNA
DNA=DNA.replace("A", "t")
DNA=DNA.replace("C","g")
DNA=DNA.replace("T","a")
DNA=DNA.replace("G","c")
DNA=DNA[::-1]
print (DNA.upper())