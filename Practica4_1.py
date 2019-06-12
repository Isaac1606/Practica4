#Autor: Carballo Pérez Isaac
#Fecha:27/03/19
import re
import math

class Practica4:

    __caracter=""
    __regla=""
    __casos=[]
    __casos_base=[]
    __casos_recursivos=[]
    __formato_regla = "^[A-Z]-> [^|^<^>^.]+(?:\|[^|^<^>^.]+)*$"  # tomo un formato de referencia para las reglas

    # empieza la cadena puede tomar valor el primer caracter entre A-Z continua un guion luego mayor que, posteriormente cualquier catracter que no sea el definido entre corchetes al menos 1 vez  de ahi le dices que un operador or seguido de minimo un caracter (que no sea los que estan entre corchetes), o de lo contrario ningun operador or

    #Constructor de la clase
    def __init__(self):
        print("Hola mundo!")
        print("Programa para evaluar una Gramática Libre de Contexto")

    #Analizador de regla
    def setRegla(self,regla):
        encontrado = re.search(self.__formato_regla, regla)
        if encontrado is not None:
            print("La regla fue correctamente escrita")
            self.__regla=regla
            self.__caracter=regla[0]
        else:
            print("La regla no fue correctamente escrita")

    def getRegla(self):
        return self.__regla

    def getCaracter(self):
        return self.__caracter

    #Separador de reglas
    def separadorReglas(self):
        regla=self.__regla[4:]
        self.__casos=list(set(re.split("[|]",regla)))
        for i, caso in enumerate(self.__casos): #por cada caso en la lista de casos
            if 'λ' in self.__casos:
                self.__casos.remove('λ')
                self.__casos.append('')
            if re.search(self.__caracter,self.__casos[i]) is not None:
                self.__casos_recursivos.append(caso)
            else:
                self.__casos_base.append(caso)

    def getCasosBase(self):
        return self.__casos_base

    def getCasos(self):
        return self.__casos

    def getCasosRecursivos(self):
        return self.__casos_recursivos

    def setCadena(self,cadena):
        self.__cadena=cadena

    def eliminaEpsilons(self):
        cad=self.__cadena.split(' ')
        lista = list(cad)
        count = lista.count(' ')
        while count > 0:
            lista.remove(' ')
            count -= 1
        cad = "".join(lista)
        self.__cadena=cad

    def validaCaracteres(self):
        c1 = set(list(self.__cadena))
        c2 = set(self.__casos_base)
        if c1.issubset(c2):
            return True
        else:
            return False

    def esDeEstaGramatica(self):
        cadena=self.__cadena
        if len(cadena) == 0:
            print("La cadena:", "λ", ", Es palindromo")
        else:
            if (cadena[::-1]==cadena) and (self.validaCaracteres())==True:
                print("La cadena:",cadena,", Es un palindromo")
            else:
               print("La cadena:",cadena,", No es una cadena valida para esta gramatica")


    def paraEste(self):
        cadena=self.__cadena
        count=len(cadena)
        if len(cadena)%2==0:
            count=count/2
        else:
            count=(count+1)/2
        count=int(count)
        if (cadena[::-1]==cadena) and (self.validaCaracteres()==True):
            print(" "+self.__caracter)
            if len(cadena)==0:
                print(' λ')
            if len(cadena)==1:
                if cadena=='1':
                   print(" 1")
                if cadena=='0':
                 print(" 0")
            for i in range(count):
                if len(cadena)>1:
                    if cadena.startswith('0') and cadena.endswith('0'):
                        print("0S0")
                        if cadena=='00':
                            print(' λ')
                        if cadena=='010':
                            print(' 1')
                        if cadena=='000':
                            print(' 0')
                    if cadena.startswith('1') and cadena.endswith('1'):
                        print("1S1")
                        if cadena=='11':
                            print(' λ')
                        if cadena=='101':
                            print(' 0')
                        if cadena=='111':
                            print(' 1')
                    cadena=cadena[1:-1]

#Menu
a=Practica4()
#regla= input("\nIngrese la regla con la cual sera evaluada la cadena: ") #pido que ingrese la regla
#regla="S-> λ|0|1|1S1|0S0|00|11"
regla="S-> λ|0|1|1S1|0S0"

a.setRegla(regla)
print(a.getRegla())
print("El simbolo inicial es: {}".format(a.getCaracter()))
a.separadorReglas()

print("Los casos son:{}\nLos casos base son:{}\nLos casos recursivos son:{}".format(a.getCasos(),a.getCasosBase(),a.getCasosRecursivos()))

cadena=""

while (cadena!='-1'):
    cadena=input("\nIngrese una cadena y veamos si cumple con la regla: ")

    a.setCadena(cadena)
    a.validaCaracteres()
    a.eliminaEpsilons()
    a.esDeEstaGramatica()
    print()
    a.paraEste()