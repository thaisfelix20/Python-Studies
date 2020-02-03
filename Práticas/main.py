from ex01 import Empregados

obj1 = Empregados('matheus', 'braga', 100)
obj2 = Empregados('math', 'Bra', 300)
obj3 = Empregados('Jo', 'mat', 500)

print 'Nome:', obj1.getNome()
print 'Sobrenome:', obj1.getSobrenome()
print 'Salario Mensal:', obj1.getSalario_mensal()
print 'Salario Anual:', (obj1.getSalario_mensal()*12)
print ""

print 'Nome:', obj2.getNome()
print 'Sobrenome:', obj2.getSobrenome()
print 'Salario Mensal:', obj2.getSalario_mensal()
print 'Salario Anual:', (obj2.getSalario_mensal()*12)
print ""

print 'Nome:', obj3.getNome()
print 'Sobrenome:', obj3.getSobrenome()
print 'Salario Mensal:', obj3.getSalario_mensal()
print 'Salario Anual:', (obj3.getSalario_mensal()*12)
print ""

print "Salario Atualizado"
print ""
print 'Nome:', obj1.getNome()
print 'Sobrenome:', obj1.getSobrenome()
obj1.aumentarSalario(0.12)
print 'Salario Mensal:', obj1.getSalario_mensal()
print 'Salario Anual:', (obj1.getSalario_mensal()*12)
print ""

print 'Nome:', obj2.getNome()
print 'Sobrenome:', obj2.getSobrenome()
obj2.aumentarSalario(0.12)
print 'Salario Mensal:', obj2.getSalario_mensal()
print 'Salario Anual:', (obj2.getSalario_mensal()*12)
print ""

print 'Nome:', obj3.getNome()
print 'Sobrenome:', obj3.getSobrenome()
obj3.aumentarSalario(0.12)
print 'Salario Mensal:', obj3.getSalario_mensal()
print 'Salario Anual:', (obj3.getSalario_mensal()*12)
print ""

