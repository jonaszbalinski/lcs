# Program requires ANSICON/VT100 to show colors in terminal
class colors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def longest_common_subsequence(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)

    valuesTab = [[None]*(len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                valuesTab[i][j] = 0
            elif seq1[i - 1] == seq2[j - 1]:
                valuesTab[i][j] = valuesTab[i-1][j-1] + 1
            else:
                valuesTab[i][j] = max(valuesTab[i-1][j], valuesTab[i][j-1])
            
    
    i = len1
    j = len2
    subsequence = ""

    while i != 0 and j != 0:
        if valuesTab[i][j] == valuesTab[i][j-1]:
            j -= 1
        elif valuesTab[i][j] == valuesTab[i-1][j]:
            i -= 1
        else:
            subsequence += seq1[i-1] # seq1 with i or j?
            i -= 1
            j -= 1

    return valuesTab[len1][len2], subsequence[::-1]

if __name__ == "__main__":
    seq1 = "asdcasbd liaubaisj dlabslhi dbvasuygvdyiasbldjabsldiyvao liyu;bjsd;u"
    seq2 = "andsiaubs;dn'podiha9[ hduaosb dniypgh7uo;iankm ihouyvalhbk .jdlknahg6foayvukgd"

    lenOfLCS, commonSeq = longest_common_subsequence(seq1, seq2)
    print(f"Length: {lenOfLCS}\nCommon seq: {commonSeq}\n")

    for i in range(len(seq1)):
        print(seq1[i], end="")
    print()

    for i in range(len(seq2)):
        print(seq2[i], end="")
    print()
