def fibonacci(n):
    var1 = 1
    var2 = 0
    i = 0
    lista = []
    while var2 < n + 1:
        soma = var1 + var2
        var1 = var2
        var2 = soma
        i = [var1]
        lista.append(var1)
    valor = (int(input('Digite um número:')))
    i = 0
    pert = []
    naoPert = []
    while i < (len(lista)):    
        if valor == lista[i]:
            pert.append('pertence')
        else:
            naoPert.append('não pertence')
        i += 1
        
    if pert == ['pertence']:
        print ('Este numero pertence a sequência.')
    else :
        print ('Este número não pertence a sequência.')
    return 

fibonacci(34)