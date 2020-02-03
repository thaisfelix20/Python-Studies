class NumeroComplexo(object): # cria a classe

    def __init__(self, a=0, b=0):# metodo inicializador
        # como aqui nao tem sobregarca de metodo, a forma para considerar
        # a falta de paramentro e ja inicializar as variaveis na criacao do metodo
        self.__a = a  # __a e __b estao encapsuladas (__ antes da var encapsula)
        self.__b = b


    def inicializaNumero(self,a,b):
        # pega o q passar por paramentro e guarda
        self.__a = a
        self.__b = b

    def imprimeNumero(self):
        # pega os numeros guardados e imprimi
        print("{} + {}i".format(self.__a,self.__b))

    def eIgual(self,c,d):
        if self.__a == c and self.__b == d:
            # se as partes reais e as partes imaginarias forem iguais
            return True
        else:
            return False

    def get_real(self):
        # pega a parte real
        return self.__a

    def get_imag(self):
        # pega a parte imaginaria
        return self.__b

    def soma(self,c,d):
        p_real = self.__a + c
        p_imag = self.__b + d
        print("Soma: {} + {}i".format(p_real,p_imag))

    def subtrai(self,c,d):
        p_real = self.__a - c
        p_imag = self.__b - d
        print("Subtracao: {} + {}i".format(p_real,p_imag))

    def multiplica(self,c,d):
        p_real = (self.__a*c) - (self.__b*d)
        p_imag = (self.__a*d) + (self.__b*c)
        print("Multiplicacao: {} + {}i".format(p_real,p_imag))

    def divide(self,c,d):
        p_real = ((self.__a*c*1.0) + (self.__b*d*1.0))/((1.0*c**2) + (1.0*d**2))
        p_imag = ((self.__b*c*1.0) - (self.__a*d*1.0))/((1.0*c**2) + (1.0*d**2))
        # esses 1.0 multiplicando e pq tava pegando so a parte inteira, assim
        # "transforma" em real
        print("Divisao: {} + {}i".format(p_real,p_imag))

