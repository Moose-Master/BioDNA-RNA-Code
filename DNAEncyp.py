import random
from re import S, T
start = input("Text: ").replace(" ","").lower()
def to_3_char(first_two,options):
    choice = random.randint(0,len(options)-1)
    rna.append(str(first_two)+str(options[choice]))
rna = ["aug"]
any = ["a","u","c","g"]
for i in start:
    if i == "a":
        to_3_char("gc",any)
    if i == "c":
        to_3_char("ug",["u","c"])
    if i == "d":
        to_3_char("ga",["u","c"])
    if i == "e":
        to_3_char("ga",["a","g"])
    if i == "f":
        to_3_char("uu",["u","c"])
    if i == "g":
        to_3_char("gg",any)
    if i == "h":
        to_3_char("ca",["c","u"])
    if i == "i":
        to_3_char("au",["a","c","u"])
    if i == "k":
        to_3_char("aa",["g","a"])
    if i == "l":
        choice = random.randint(0,1)
        if choice == 0:
            to_3_char("cu",any)
        else:
            to_3_char("uu",["a","g"])
    if i == "m":
        rna.append("aug")
    if i == "n":
        to_3_char("aa",["c","u"])
    if i == "p":
        to_3_char("cc",any)
    if i == "q":
        to_3_char("ca",["g","a"])
    if i == "r":
        choice = random.randint(0,1)
        if choice == 0:
            to_3_char("ag",["g","a"])
        else:
            to_3_char("cg",any)
    if i == "s":
        choice = random.randint(0,1)
        if choice == 0:
            to_3_char("ag",["c","u"])
        else:
            to_3_char("uc",any)
    if i == "t":
        to_3_char("ac",any)
    if i == "v":
        to_3_char("gu",any)
    if i == "w":
        rna.append("ugg")
    if i == "y":
        to_3_char("ua",["u","c"])
to_3_char("ua",["a","g"])
rna_combined = ",".join(rna)
dna = []
for i in range(len(rna_combined)):
    if rna_combined[i] == "u":
        dna.append("a")

    if rna_combined[i] == "a":
        dna.append("t")

    if rna_combined[i] == "g":
        dna.append("c")

    if rna_combined[i] == "c":
        dna.append("g")
        
    if rna_combined[i] == ",":
        dna.append(",")
dna_final = "".join(dna)
print("DNA: " + str(dna_final))
print("RNA: " + str(rna_combined))