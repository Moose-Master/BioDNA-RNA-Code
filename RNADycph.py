dna = input("DNA String: ")
rna = []
for i in range(len(dna)):
    if dna[i] == "a":
        rna.append("u")

    if dna[i] == "t":
        rna.append("a")

    if dna[i] == "c":
        rna.append("g")

    if dna[i] == "g":
        rna.append("c")
        
    if dna[i] == ",":
        rna.append(",")
rna_combinded = "".join(rna)
rna_list = rna_combinded.split(",")
decoded_rna = []
start_printed = False
for i in rna_list:
    if i[:-1] == "gg":
        decoded_rna.append("g")
    if i == "gag" or i == "gaa":
        decoded_rna.append('e')
    if i == "gac" or i == "gau":
        decoded_rna.append("d")
    if i[:-1] == "gc":
        decoded_rna.append("a")
    if i[:-1] == "gu":
        decoded_rna.append("v")

    if i == "agg" or i == "aga":
        decoded_rna.append("r")
    if i == "agc" or i == "agu":
        decoded_rna.append("s")
    if i == "aag" or i == "aaa":
        decoded_rna.append("k")
    if i == "aac" or i == "aau":
        decoded_rna.append("n")
    if i[:-1] == "ac":
        decoded_rna.append("t")
    if i == "aug" and start_printed == True:
        decoded_rna.append("m")
    elif i == "aug" and start_printed == False:
        decoded_rna.append("[start]")
        start_printed = True
    if i == "aua" or i == "auc" or i == "auu":
        decoded_rna.append("i")
    if i[:-1] == "cg":
        decoded_rna.append("r")
    if i == "cag" or i == "caa":
        decoded_rna.append("q")
    if i == "cac" or i == "cau":
        decoded_rna.append("h")
    if i[:-1] == "cc":
        decoded_rna.append("p")
    if i[:-1] == "cu":
        decoded_rna.append("l")
    
    if i == "uuu" or i == "uuc":
        decoded_rna.append("f")
    if i == "uua" or i == "uug":
        decoded_rna.append("l")
    if i[:-1] == "uc":
        decoded_rna.append("s")
    if i == "uau" or i == "uac":
        decoded_rna.append("y")
    if i == "uaa" or i == "uag":
        decoded_rna.append("[end]")
    if i == "ugu" or i == "ugc":
        decoded_rna.append("c")
    if i == "uga":
        decoded_rna.append("[end]")
    if i == "ugg":
        decoded_rna.append("w") 
print("RNA String: " + str(rna_combinded))
print("".join(decoded_rna))