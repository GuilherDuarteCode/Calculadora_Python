# criando o visual da calculadora

print("-------------------------------------------------")
print("                 CALCULADORA                     ")
print("-------------------------------------------------")

# recebendo os numeros
Numero_1=(float(input("qual o primeiro numero?: ")))
Numero_2=(float(input("qual o segundo numero?: ")))

# recebendo qual a operaçao matematica devera ser feita

numero_calculo=input(f"""essas são as operações matematicas disponiveis em meu sistema
 1- soma
 2- subtração
 3- divisão
 4- multiplicação
 5- sair
 escolha uma: """)
while (numero_calculo != '1' and numero_calculo != '2' and numero_calculo != '3' and numero_calculo != '4' and numero_calculo != '5'):
    numero_calculo=input(f"""essas são as operações matematicas disponiveis em meu sistema
 1- soma
 2- subtração
 3- divisão
 4- multiplicação
 5- sair
 escolha uma: """)
    
print("-------------------------------------------------")
def calcular():
    match numero_calculo:
        case "1":
            resultado=(Numero_1 + Numero_2)
            print(f"   o resultado da sua conta foi: {resultado}     ")
        case "2":
            resultado=Numero_1-Numero_2
            print(f"   o resultado da sua conta foi: {resultado}     ")
        case "3":
            resultado=Numero_1*Numero_2
            print(f"   o resultado da sua conta foi: {resultado}     ")
        case "4":
            resultado=Numero_1/Numero_2
            print(f"   o resultado da sua conta foi: {resultado}     ")
        case "5":
            print("reinicie a calculadora para uma nova consulta")
        

               
            
calcular()








    

   


 












