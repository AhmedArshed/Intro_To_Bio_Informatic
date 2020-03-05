splitLst = []

def getdata():
    res = []
    with open("input.txt", 'r') as a:
        sequence = a.readline()
        sequence = sequence.upper()
        
        n = int(a.readline())

        for i in range(n):
            l1 = a.readline()
            l1 = l1.strip()
            l1 = l1.split(" ")
            splitLst.append(l1)
        
        res.append(sequence)
        res.append(splitLst)
    
    return res

def checkIntrons_toremove(sequence, splitLst):
    extralen = 0

    print(splitLst)
    for i in range(len(splitLst)):
        start = int(splitLst[i][0]) - extralen
        end = (int(splitLst[i][1])+1) - extralen
        extralen = end - start

        sequence = sequence[0:start] + sequence[end:]

    return sequence




def changevalues(sequence):
    change = ""
    
    for i in sequence:
        if i == "A":
            change += "U"
        elif i == "C":
            change += "G"
        elif i == "G":
            change += "C"
        elif i == "T":
            change += "A"
    
    return change


def translation(change):
    flag = False
    p = []
    temp = ""
    table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", 
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
        
    for i in range(0, len(change), 3):
        codon = change[i:i+3]

        if len(codon) < 3:
            continue

        if codon == "AUG":
            flag = True

        if flag == True:
            amin = table[codon]
            temp += amin

            if amin == "STOP":
                flag = False
                p.append(temp)
                temp = ""
    return p
def main():
    
    rs = getdata()
    sequence = rs[0]
    splitLst = rs[1]
    sequence = checkIntrons_toremove(sequence, splitLst)
    change = changevalues(sequence)
    p = translation(change)
    print(p)

main()
