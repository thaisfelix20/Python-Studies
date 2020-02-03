class Cripto(object): # cria a classe

    def __init__(self, a=0):# metodo inicializador
        self.__a = a

    def recebe(self,a):
        # pega o q passar por paramentro e guarda
        self.__a = a

    def exibe(self):
        # pega os numeros guardados e imprimi
        print("Numero = {}".format(self.__a))

    def criptografa(self):
        # primeira parte e adicionar 6
        self.__a[0] = self.__a[0] + 6
        self.__a[1] = self.__a[1] + 6
        self.__a[2] = self.__a[2] + 6
        self.__a[3] = self.__a[3] + 6
        # segunda parte e obter o modulo por 10
        self.__a[0] = self.__a[0] % 10
        self.__a[1] = self.__a[1] % 10
        self.__a[2] = self.__a[2] % 10
        self.__a[3] = self.__a[3] % 10
        # depois faz a troca (1 -- 3) (2 -- 4)
        x = self.__a[0]
        self.__a[0] = self.__a[2]
        self.__a[2] = x
        x = self.__a[1]
        self.__a[1] = self.__a[3]
        self.__a[3] = x
        print ("Numero criptografado: {}".format(self.__a))

    def descriptografa(self):
        # para descriptografar faz o contrario
        # primeiro a troca (1 -- 3) (2 -- 4)
        x = self.__a[0]
        self.__a[0] = self.__a[2]
        self.__a[2] = x
        x = self.__a[1]
        self.__a[1] = self.__a[3]
        self.__a[3] = x
        # segunda parte do modulo de 10
        # se for analisado os numeros que eram acima de 6
        # nao mudam nesta parte, e os que sao abaixo de 6
        # eh como se fosse subtraido 10
        for x in range(0, 4):
            if self.__a[x] < 6:
                self.__a[x] = self.__a[x]+10
        # e por fim so e subtrair 6
        self.__a[0] = self.__a[0] - 6
        self.__a[1] = self.__a[1] - 6
        self.__a[2] = self.__a[2] - 6
        self.__a[3] = self.__a[3] - 6
        print ("Numero descriptografado: {}".format(self.__a))
