operador = input("Você deseja somar(+), subtrair(-), multiplicar(*) ou dividir(/)? Digite o sinal algébrico!")

if operador == "+":
    x = input("Certo, então digite um número: ")
    y = input("Entre com o segundo número: ")
    
    soma = float(x) + float(y)
    
    simOuNao = input("Deseja somar mais algum número? Digite sim ou nao: ")
    
    while simOuNao == "sim":
        numero = input("Digite o próximo número: ")
        numero = float(numero)
        soma += numero
        simOuNao = input("Deseja somar mais algum número? Digite sim ou nao: ")
    else:
        print("O resultado final é: ",soma)  
elif operador == "-":
    x = float(input("Certo, então digite um número: "))
    y = float(input("Subtraia o número anterior por: "))
    
    subtracao = x - y
    
    simOuNao = input("Deseja subtrair mais algum número? Digite sim ou não: ")

    while simOuNao == "sim":
        numero = float(input("Subtraia do resultado anterior o número: "))
        subtracao -= numero
        simOuNao = input("Deseja subtrair mais algum número? Digite sim ou nao: ")
    else:
        print("O resultado final é: ",subtracao)
elif operador == "*":
    x = float(input("Certo, então digite um número: "))
    y = float(input("Multiplique o número anterior por: "))
    
    multipliacacao = x * y
    
    simOuNao = input("Deseja multiplicar por mais algum número? Digite sim ou nao: ")

    while simOuNao == "sim":
        numero = float(input("Multiplique o resultado anterior por: "))
        multipliacacao *= numero
        simOuNao = input("Deseja multiplicar por mais algum número? Digite sim ou nao: ")
    else:
        print("O resultado final é: ",multipliacacao)
elif operador == "/":
    x = float(input("Certo, então digite um número: "))
    y = float(input("Divida o número anterior por: "))
    
    divisao = x / y
    
    simOuNao = input("Deseja dividir por mais algum número? Digite sim ou nao: ")

    while simOuNao == "sim":
        numero = float(input("Divida o resultado anterior por: "))
        divisao /= numero
        simOuNao = input("Deseja dividir por mais algum número? Digite sim ou nao: ")
    else:
        print("O resultado final é: ",divisao)