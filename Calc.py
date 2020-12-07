primeiro = input("Digite o primeiro número: ")
segundo = input("Digite o segundo número: ")
operacao = input("Digite a operação: ")

resultado = None
if operacao == "+":
    resultado = float(primeiro) + float(segundo)
elif operacao == "-":
    resultado = float(primeiro) - float(segundo)
elif operacao == "*":
    resultado = float(primeiro) * float(segundo)
elif operacao == "/":
    resultado = float(primeiro) / float(segundo)
else:
    print("Operação inexistente !")

if resultado:
    print("Resultado: {0}".format(resultado))