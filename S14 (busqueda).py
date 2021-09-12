class Busqueda:

    def __init__(self,listas=None):
        self.__lista=listas

    @property
    def lista(self):
        if self.__lista != None:
            return self.__lista
        else:
            print("lista vacia")


    #@lista.setter
    #def lista(self,value):
        #self.__lista=value

    def busquedaLineal(self,buscado):
        lon = len(self.__lista)
        enc=False
        pos=0
        while pos < lon and enc==False:
            if self.__lista[pos]["nombre"] ==buscado: enc=True
            else: pos +=1

        if enc: return pos
        else: return -1

    def ordenar(self):
        for pos in range(0,len(self.__lista)):
            for sig in range(pos+1,len(self.__lista)):
                if self.__lista[pos]["nombre"]>self.__lista[sig]["nombre"]:
                    aux = self.__lista[pos]
                    self.__lista[pos]=self.__lista[sig]
                    self.__lista[sig]=aux

    def busquedaBinaria(self,buscado):
        pass

notas= [
    {"nombre":"Juan","n1":20,"n2":40},
    {"nombre":"Luis","n1":30,"n2":50},
    {"nombre":"Domenica","n1":40,"n2":50},
    {"nombre":"Daniela","n1":50,"n2":40},
    {"nombre":"Armenia","n1":55,"n2":40},
    {"nombre":"Rolando","n1":60,"n2":40}
    ]
print(notas[3])
bus1 = Busqueda(notas)
bus1.ordenar()
print(bus1.lista)

#print(bus1.busquedaLineal(40))
#bus1.busquedaLineal("ok")
#bus2=Busqueda(["Ana","Dan","Abdon"])
#bus2.busquedaLineal("aceptar")
