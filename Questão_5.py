def inverso (n):
    i = 0
    lista = []
    while i < len(n):
        lista.append(n[i]) 
        i += 1
    mudar = n[6] + n[5] + n[4] + n[3] + n[2] + n[1] + n[0]
    print(mudar)
    return
inverso('dracula')