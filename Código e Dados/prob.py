# -- coding: utf-8 --

#le o arquivo...
arq  = open("limpezanova.csv", "r")

#separa em linhas
linhas =  arq.readlines()
instancias = []
#transforma as linhas em vetores de string
for x in linhas:
    #poe na lista nova de dados a linhas convertida pra um vetor de string
    #strip, retira o ";"
    #split separa pelo ";"
    instancias.append(x.strip().split(';'))

#conta qnts  atributo 2 é = 1, pela tabela de dados
def prob(regiao):
    
    cont1 = 0
    
    for x in instancias:
        if(int(x[1])==  regiao and (int(x[5])- int(x[4]))>6 ):
            cont1= cont1+1
    print("Qntdade = ",cont1)           
    print("\n")
           
def main():
    regiao = 1
    while regiao <=5:
           
        print(" Regiao: ",regiao)
        prob(regiao)
        regiao = regiao + 1

main()
