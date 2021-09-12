class Matriz:
  def __init__(self,matriz):
      self.matriz = matriz

  def mostrar(self,dato):
      for fila in range(len(self.matriz)):
          #print(self.matriz[fila])
          #self.matriz[fila][0] = self.matriz[fila][0]
          for col in range(len(self.matriz[fila])):
              if self.matriz[fila][col] == dato:
                 print(self.matriz[fila][col],end="")
          print()

numeros = [[10,20,30],[10,20,30],[10,20,30]]
mat = Matriz(numeros)
mat.mostrar(23)