from ex02vip import VIP

class CamaroteSuperior(VIP):

    def __init__(self,valor,local):
        VIP.__init__(self,valor)
        self.local = local

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def imprimiLocal(self):
        print 'Local: ', self.local
