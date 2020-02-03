class Empregados(object):

    def __init__(self, Nome, sobrenome, salario_mensal):
        self.Nome = Nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal
        if (salario_mensal<0):
            self.salario_mensal = 100

    def getNome(self):
        return self.Nome

    def setNome(self, Nome):
        self.Nome = Nome

    def getSobrenome(self):
        return self.sobrenome

    def setSobreNome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSalario_mensal(self):
        return self.salario_mensal

    def setSalario_mensal(self,salario):
        if (salario < 0):
            self.salario_mensal = 100
        else:
            self.salario_mensal = salario

    def aumentarSalario(self, porcent):
        self.salario_mensal = self.salario_mensal*(1+porcent)
