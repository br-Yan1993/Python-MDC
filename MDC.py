valores_2 = []
vet_sub = 1
vet_alg_1 = []
vet_alg_2 = []
vet_alg_3 = []
vet_alg_4 = []
vet_alg_5 = []

def func_inicial (vet_1, vet_2):
    while (vet_2 != 0):
        vet_2 = (int(input('\nDigite os valores do MDC!\nCaso queira começar a fatorar, digite 0.\n(Numeros já Inseridos:{}: '.format(vet_1))))
        vet_1.append(vet_2)
        if (vet_2 == 0):
            del vet_1[-1]
    return(vet_1)
    print(vet_1)

def func_mdc (vet_valor, res_1, res_2, res_3, res_4, res_5):
    for i in vet_valor:
        contador_1 = 1
        vet_resultante_0 = [1]
        while (contador_1 != i):
            div_1 = (i // contador_1)
            contador_1 += 1
            if (i % contador_1 == 0):
                vet_resultante_0.append(contador_1)
        if (len(res_1) == 0):
            res_1 = vet_resultante_0
        elif (len(res_2) == 0 and len(res_1) != 0):
            res_2 = vet_resultante_0
        elif (len(res_3) == 0 and len(res_2) != 0):
            res_3 = vet_resultante_0
        elif (len(res_4) == 0 and len(res_3) != 0):
            res_4 = vet_resultante_0
        elif (len(res_5) == 0 and len(res_4) != 0):
            res_5 = vet_resultante_0

    res_0 = []
    
    if (len(res_1) < (len(res_2))):
        res_0 = res_2
        res_2 = res_1
    else:
        res_0 = res_1

    if (len(res_0) and len(res_2) != 0 ):
        vetor_final = []
        i = 0
        for i in res_0:
            if i in res_2:
                vetor_final.append(i)
        print('O MDC de {} e:'.format(valores_2))
        print(vetor_final[-1])


if __name__ == "__main__":
    func_inicial(valores_2, vet_sub)
    func_mdc(valores_2, vet_alg_1, vet_alg_2, vet_alg_3, vet_alg_4, vet_alg_5)