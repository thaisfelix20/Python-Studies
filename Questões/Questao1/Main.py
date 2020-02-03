from modela_complexo import NumeroComplexo

inst_1 = NumeroComplexo(1,1)
print("Inst 1:")
inst_1.imprimeNumero()
inst_2 = NumeroComplexo(1)
print("Inst 2:")
inst_2.imprimeNumero()
inst_3 = NumeroComplexo()
print("Inst 3:")
inst_3.imprimeNumero()

print("Int 1 eh igual a 1+1i? {}".format(inst_1.eIgual(1,1)))
print("Int 1 eh igual a 0+1i? {}".format(inst_1.eIgual(0,1)))

print("Operacoes de Inst 1 com Inst 2")
inst_1.soma(inst_2.get_real(), inst_2.get_imag())
inst_1.subtrai(inst_2.get_real(), inst_2.get_imag())
inst_1.multiplica(inst_2.get_real(), inst_2.get_imag())
inst_1.divide(inst_2.get_real(), inst_2.get_imag())
