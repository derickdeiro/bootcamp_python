# 1) Solicitar ao usuário que digite seu nome
nome_do_usuario = input('Digite seu nome: ')
print(f'O nome do usuário é: {nome_do_usuario}')

# 2) Solicitar ao usuário que digite o valro do seu salário. 
# Converta a entrada para um número de ponto flutuante
salario = float(input('Digite seu salário: '))
print(f'O salário é: R$ {salario}')

# 3) Solicitar ao usuário que digite o valor do bônus recebido
# Converta a entrada para um número de ponto flutuante
bonus = float(input('Digite o percentual do bônus: '))
print(f'O bônus é de {bonus}%')

CONSTANTE_BONUS = 1000

# 4) Calcule o valor do bônus final
bonus_final = (CONSTANTE_BONUS + salario) * bonus
print(f'O bônus é no valor de: {bonus_final}')

# 5) Imprima o cálculo do KPI para o usuário
print(f'O KPI é: Salário: {salario} vezes o percentual do bonus: {bonus}% + 1000,00. O valor total é de {bonus_final}')

