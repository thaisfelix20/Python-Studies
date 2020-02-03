from ex02 import Ingresso

class VIP(Ingresso):

    #def __init__(self,add):
     #   self.add = add

    def valorIngressoVIP(self,add):
        self.valor = self.valor+add
        return self.valor
