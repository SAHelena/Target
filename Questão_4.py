def percentual (n, total): 
    calculo = (n/total)*100
    separar = str(calculo).split('.')
    porcent = separar[0]
    print('Aproximadamente', porcent, '%')
    return 

#total = 180759.98
#sp = 67836.43
#rj = 36678.66             * valor dos estados para demonstração. *
#mg = 29229.88
#es = 27165.48
#outros = 19849.53

percentual (67836.43, 180759.98)       #  * percentual do estado de SP de exemplo. *