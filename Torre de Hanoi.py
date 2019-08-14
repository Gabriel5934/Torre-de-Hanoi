torreA = [3, 2, 1]
torreB = []
torreC = []

def tabuleiro():
    print("Torre A ", torreA)
    print("Torre B ", torreB)
    print("Torre C ", torreC)

tabuleiro()

torreSai = input("Digite a torre que você quer alterar: ") 
torreEntra = input("Digite a torre destino: ")

euamobreak = True

while euamobreak:
    if torreSai == "a":
        if torreEntra == "a":
            print("Aí você me quebra! Jogada inválida!")
        if torreEntra == "b":
            if len(torreB) > 0 and torreA[-1] > torreB[-1]:
                print("Não pode isso")
            else:
                torreB.append(torreA[-1])
                torreA.remove(torreA[-1])
        if torreEntra == "c":
            if len(torreC) > 0 and torreA[-1] > torreC[-1]:
                print("Não pode isso")
            else:
                torreC.append(torreA[-1])
                torreA.remove(torreA[-1])

    if torreSai == "b":
        if torreEntra == "b":
            print("Aí você me quebra! Jogada inválida!")
        if torreEntra == "a":
            if len(torreA) > 0 and torreB[-1] > torreA[-1]:
                print("Não pode isso")
            else:
                torreA.append(torreB[-1])
                torreB.remove(torreB[-1])
        if torreEntra == "c":
            if len(torreC) > 0 and torreB[-1] > torreC[-1]:
                print("Não pode isso")
            else:
                torreC.append(torreB[-1])
                torreB.remove(torreB[-1])

    if torreSai == "c":
        if torreEntra == "c":
            print("Aí você me quebra! Jogada inválida!")
        if torreEntra == "a":
            if len(torreA) > 0 and torreC[-1] > torreA[-1]:
                print("Não pode isso")
            else:
                torreA.append(torreC[-1])
                torreC.remove(torreC[-1])
        if torreEntra == "b":
            if len(torreB) > 0 and torreC[-1] > torreB[-1]:
                print("Não pode isso")
            else:
                torreB.append(torreC[-1])
                torreC.remove(torreC[-1])

        if torreC = [3, 2, 1]:
            print("Gênio!")
            euamobreak = False

    tabuleiro()

    torreSai = input("Digite a torre que você quer alterar: ") 
    torreEntra = input("Digite a torre destino: ")

            
