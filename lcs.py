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
    

    return valuesTab[len1][len2]

if __name__ == "__main__":
    sequenceUno = "asdnoub12eu9b128dvo uibasdy8avso8 dfvqybihyavsutidgcayudcvyailsvdgo7qi6yqvlhi \
                   bashvdouylq idwhasilo"
    sequenceDos = "abidhbas;udoipbg2o8q6gep19783hei 1[in912r0 g79pg1h2e2jodwmqljhp97ghuon 1io2h \
                   euphdip qnmwipd jauh12m doqnipwu9ghqpuwd"
    print(f"LCS: {longest_common_subsequence(sequenceUno, sequenceDos)}")
