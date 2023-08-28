# A unica diferença de WHILE para FOR é que while nos não sabemos quantas repetiçoes vai ter e FOR, vc sabe o começo e o final 


for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')