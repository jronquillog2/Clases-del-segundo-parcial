class Archivo:
    def __init__(self,nombreArchivo,separador=" "):
        self.__archivo = nombreArchivo
        self.__separador = separador

    def leer(self):
        with open(self.__archivo, "r", encoding = "UTF-8") as file:
            lista=[]
            for linea in file:
                lista.append(linea[:-1])
        return lista

    def escribir(self,datos,modo):
        with open(self.__archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")

    def write(self, datos, modo):
        with open(self.__archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                linea=""
                for valor in dato:
                    if type(valor)== int or float: linea+=str(valor)+self.__separador
                    else: linea += valor + self.__separador
                file.write(linea[:-1]+"\n")

arch = Archivo("articulos.txt",";")
#lista = arch.leer()
#print(lista)
#arti2 =["Aceite","Leche"]
articulos=[[1,"aceite","girazol",2.50,100],[2,"Leche", "la vaquita",1.50,200]]
#arch.escribir(["Daniela","Juan","Kylie"], "W")
arch.write(articulos,"w")


