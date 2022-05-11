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

    print("\n")
    print("*"*100, end="\n\n")
    print(f"Length: {colors.BLUE}{lenOfLCS}{colors.END}")
    print(f"Common seq: {colors.GREEN}{commonSeq}{colors.END}\n")

    seqIt = 0
    for i in range(len(seq1)):
        if seqIt < len(commonSeq) and seq1[i] == commonSeq[seqIt]:
            seqIt += 1
            print(f"{colors.GREEN}{seq1[i]}{colors.END}", end="")
        else:
            print(f"{colors.RED}{seq1[i]}{colors.END}", end="")
    print()

    seqIt = 0
    for i in range(len(seq2)):
        if seqIt < len(commonSeq) and seq2[i] == commonSeq[seqIt]:
            seqIt += 1
            print(f"{colors.GREEN}{seq2[i]}{colors.END}", end="")
        else:
            print(f"{colors.RED}{seq2[i]}{colors.END}", end="")

    print("\n")
    print("#"*100)
    print("\n")

    file1 = open("1.txt", "r")
    file2 = open("2.txt", "r")

    toTrimLines1 = file1.readlines()
    toTrimLines2 = file2.readlines()

    lines1 = []
    lines2 = []

    for i in range(len(toTrimLines1)):
        lines1.append(toTrimLines1[i].strip())
    
    for i in range(len(toTrimLines2)):
        lines2.append(toTrimLines2[i].strip())

    for i in range(min(len(lines1), len(lines2))):
        lenOfLCS, commonSeq = longest_common_subsequence(lines1[i], lines2[i])
        isSeqEqual = (lenOfLCS == len(lines1[i]) == len(lines2[i]))

        print(f"(LCS: {colors.BLUE}{lenOfLCS}{colors.END})", end=" ")
        
        if isSeqEqual:
            print(f"{colors.YELLOW}{lines1[i]}{colors.END}", end="")
        else:
            seqIt = 0
            for j in range(len(lines1[i])):
                if seqIt < len(commonSeq) and lines1[i][j] == commonSeq[seqIt]:
                    seqIt += 1
                    print(f"{colors.GREEN}{lines1[i][j]}{colors.END}", end="")
                else:
                    print(f"{colors.RED}{lines1[i][j]}{colors.END}", end="")

        if isSeqEqual:
            print(" == ", end="")
        else:
            print(" != ", end="")

        if isSeqEqual:
            print(f"{colors.YELLOW}{lines2[i]}{colors.END}", end="")
        else:
            seqIt = 0
            for j in range(len(lines2[i])):
                if seqIt < len(commonSeq) and lines2[i][j] == commonSeq[seqIt]:
                    seqIt += 1
                    print(f"{colors.GREEN}{lines2[i][j]}{colors.END}", end="")
                else:
                    print(f"{colors.RED}{lines2[i][j]}{colors.END}", end="")

        print()

    print("\n")
    print("*"*100, end="\n\n")
