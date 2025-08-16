#TAREFA DE CASA (Calculadora Média)

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))

media = (nota1 + nota2 + nota3)/3

print("Média Final:", media)

if media < 7:
  print("Aluno Reprovado")
else: print("Aluno Aprovado")