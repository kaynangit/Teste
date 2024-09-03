# Resposta Questão 1
def fibon(numero):
    f1, f2 = 0, 1
    
    if numero == 0:
        return f"O número {numero} pertence à sequência de Fibonacci."
    while f2 < numero:
        f1, f2 = f2, f1 + f2
    
    if f2 == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
r = fibon(numero)
print(r)


# Resposta Questão 2
frase = input('Digite uma frase:').lower().strip()
letras = frase.find('a')
print(f'Sua frase possuí {letras} letras "a"')

#Resposta Qustão 3 = 77
indice, soma, K = 12, 0, 1 

while K < indice:
    K += 1
    soma += K
print(soma)


# Qustão 4 
'''4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, --> Progreção aritimética com razão 2. Resposta = 1,3,5,7,9,11,13,15,17...
b) 2, 4, 8, 16, 32, 64, --> Multiplica por 2 o número anterior partindo do número 2. Resposta = 2,4,8,16,32,64,128,256,512,1024...
c) 0, 1, 4, 9, 16, 25, 36, --> A diferença entre os números é uma soma entre a difença anterior + 2. Resposta =  0,1,4,9,16,25,36,49,64,81,100...
d) 4, 16, 36, 64, --> A diferença entre os números é uma soma de 8 começando no número 4 e a diferença em 12. Resposta = 4,16,36,64,100,144,196,250...
e) 1, 1, 2, 3, 5, 8, --> Sequência de fibonacci. Resposta = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
f) 2,10, 12, 16, 17, 18, 19, --> A lógica é números que começam com a letra D então o próximo número da sequência é 200'''

#Questão 5 
'''
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
 Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores
 quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
 Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, 
 qual interruptor controla cada lâmpada?  


 1º identifico os interruptores 1-2-3 
 2º ligo o interruptor 1 e deixo ligado por 10 minutos 
 3º ligo o interruptor 2 e deixo ligado por 4 minutos
 4º vou na primeira sala e verifico qual a temperatura da lâmpada, se ela estiver muito quente
    isso significa que ela pertence ao primeiro interruptor 
 5º vou na segunda sala e verifico se a lâmpada está fria ou menos quente, isso me faz identificar
    qual interruptor está ligada a sala. 
'''


