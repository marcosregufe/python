def calcular_imc(peso, altura):
  """
  Calcula o IMC a partir do peso e altura.

  Args:
    peso: Peso em kg.
    altura: Altura em metros.

  Returns:
    O valor do IMC.
  """
  return peso / (altura ** 2)

def main():
  """
  Função principal do programa.
  """
  # Pede o peso ao usuário
  peso = float(input("Digite seu peso (em kg): "))

  # Pede a altura ao usuário
  altura = float(input("Digite sua altura (em metros): "))

  # Calcula o IMC
  imc = calcular_imc(peso, altura)

  # Exibe o valor do IMC
  print(f"Seu IMC é: {imc:.2f}")

  # Classifica o IMC
  if imc < 18.5:
    print("Classificação: Abaixo do peso")
  elif imc < 25:
    print("Classificação: Peso ideal")
  elif imc < 30:
    print("Classificação: Sobrepeso")
  elif imc < 40:
    print("Classificação: Obesidade")
  else:
    print("Classificação: Obesidade mórbida")

if __name__ == "__main__":
  main()
