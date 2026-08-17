def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b


print("=== CALCULADORA ===")

a = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
b = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = soma(a, b)
elif operacao == "-":
    resultado = subtracao(a, b)
elif operacao == "*":
    resultado = multiplicacao(a, b)
elif operacao == "/":
    resultado = divisao(a, b)
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)