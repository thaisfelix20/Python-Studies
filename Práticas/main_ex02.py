from ex02 import Ingresso
from ex02vip import VIP
from ex02CamaroteS import CamaroteSuperior

obj1 = Ingresso(100)
obj2 = VIP(100)
obj3 = CamaroteSuperior(100, 'Tal local')

print "Obj1 "
obj1.imprimiValor()

print "Obj2 "
print "Sem acrescimo:"
obj2.imprimiValor()
obj2.valorIngressoVIP(50)
print "Com acrescimo:"
obj2.imprimiValor()

print "Obj3 "
print "Sem acrescimo:"
obj3.imprimiValor()
obj3.valorIngressoVIP(80)
print "Com acrescimo:"
obj3.imprimiValor()
obj3.imprimiLocal()
#obj3 gettar e settar tbm