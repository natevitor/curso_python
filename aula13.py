nome = 'João Vitor'
altura = 1.80
peso = 64
imc = peso / altura ** 2


"f-strings"
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'`{imc:.2f}'

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

# João tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987
