import Luis

def fatorialsoma(valor1,valor2):
    a = 1
    b = 1

    fatmax = Luis.soma(valor1,valor2)
    
    while(a*b < fatmax):
        a *= b
        b += 1

    return a
