import json

print("1-> Quantos exames estão registados?")
print("2-> Quantos exames tiveram um resultado válido?")
print("3-> Qual a distribuição dos exames por género?")
print("4-> Qual a distribuição dos exames por modalidade?")
print("5-> Quantos atletas federados do GDGoma fizeram EMD?")
print("5-> Quantos atletas do género feminino que praticam Triatlo fizeram EMD?")

with open ("emd.json") as f:
    data = json.load(f)

while(True):
    numero = input()

    if numero == "1":
        nr_exames = len(data["pessoas"])
        print("Estão resgistados: "+str(nr_exames)+" exames!")

    if numero == "2":
        validos = 0

        for p in data["pessoas"]:
            if p["resultado"] == True:
                validos +=1

        print(str(validos) + " exames válidos!")

    if numero == "3":
        masculinos = 0
        femininos = 0

        for p in data["pessoas"]:
            if p["género"] == "M":
                masculinos +=1
            else:
                femininos +=1
        print("Existem "+ str(masculinos) + " exames masculinos e "+ str(femininos) + " exames femininos!")

    if numero == "4":
        modalidades = {}

        for p in data["pessoas"]:
            modalidade = p["modalidade"]

            if modalidade in modalidades:
                modalidades[modalidade] +=1

            else:
                modalidades[modalidade] = 1

        for m in modalidades:
            print("Existem "+ str(len(m)) + " exames da modalidade " + str(m) + "!")


    if numero == "5":
        nr = 0

        for p in data["pessoas"]:
            if p["clube"] == "GDGoma":
                nr += 1

        print(str(nr) + " exames feitos por atletas do clube GDGoma")

    if numero == "6":
        fm_triatlo = 0

        for p in data["pessoas"]:
            if p["género"] == "F" and p["modalidade"] == "Triatlo" :
                fm_triatlo += 1

        print(str(fm_triatlo) + " exames feitos por atletas do sexo feminino praticantes de triatlo")

    else:
        print("Escolha um nr válido...")