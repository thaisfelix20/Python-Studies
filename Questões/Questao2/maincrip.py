from cripto import Cripto
num = -1 # numero que o usuario vai inserir

c = Cripto()

while num > 9999 or num < 0:
    #para forcar o usuario a digitar entre 0 e 9999
    num = input("Digite o numero criptografado (entre 0 e 9999)\n"
                "Numeros de 1 a 3 digitos serao completados com 0\n")
    if num > 9999 or num < 0:
        print "Digite corretamente"

x = [0,0,0,0]
# lista que guarda o numero separado

x[0] = num // 1000 % 10 # para separar milhar
x[1] = num // 100 % 10 # centena
x[2] = num // 10 % 10 # dezena
x[3] = num // 1 % 10 # unidade

c.recebe(x) # manda pra outra classe

#c.criptografa() # nao precisa criptografar

c.descriptografa()
