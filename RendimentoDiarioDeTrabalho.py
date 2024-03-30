#Variaveis
PesoPeixe=float(input("Insira a quantidade de Kg "))

#fórmulas
KgEx=int(PesoPeixe-50)
Multa=int(4*KgEx)

#Condições
if PesoPeixe<=50:
    print("Abaixo do peso limite")

else:
    print(KgEx,"Kg a mais","Sua multa é de", Multa )

