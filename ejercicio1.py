class SistemaEcuaciones:
    def __init__(self, A, b):
        self.A = A  # Matriz de coeficientes
        self.b = b  # Vector de términos independientes

    def matriz_aumentada(self):
        # Combina A y b en una matriz aumentada
        return [row + [self.b[i]] for i, row in enumerate(self.A)]

    def visualizar_matriz_aumentada(self):
        matriz = self.matriz_aumentada()
        for fila in matriz:
            print(fila)


class GaussJordan:
    def __init__(self, sistema):
        self.sistema = sistema
        self.matriz = sistema.matriz_aumentada()

    def intercambiar_filas(self, i, j):
        self.matriz[i], self.matriz[j] = self.matriz[j], self.matriz[i]

    def multiplicar_fila_por_escalar(self, fila, escalar):
        for j in range(len(self.matriz[fila])):
            self.matriz[fila][j] *= escalar

    def sumar_filas(self, fila_a, fila_b, escalar):
        for j in range(len(self.matriz[fila_a])):
            self.matriz[fila_a][j] += escalar * self.matriz[fila_b][j]

    def eliminar(self):
        filas = len(self.matriz)
        columnas = len(self.matriz[0])

        for i in range(filas):
            # Encontrar el pivote
            max_fila = i
            for k in range(i + 1, filas):
                if abs(self.matriz[k][i]) > abs(self.matriz[max_fila][i]):
                    max_fila = k

            # Intercambiar filas si es necesario
            if max_fila != i:
                self.intercambiar_filas(i, max_fila)

            # Normalizar la fila del pivote
            pivote = self.matriz[i][i]
            if pivote == 0:
                continue  # Si el pivote es cero, el sistema puede ser inconsistente

            self.multiplicar_fila_por_escalar(i, 1 / pivote)

            # Hacer ceros en la columna del pivote
            for k in range(filas):
                if k != i:
                    self.sumar_filas(k, i, -self.matriz[k][i])

    def resolver(self):
        self.eliminar()
        soluciones = [fila[-1] for fila in self.matriz]
        return soluciones


class Main:
    @staticmethod
    def main():
        # Definir un sistema de ecuaciones lineales
        A = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]
        ]
        b = [8, -11, -3]

        sistema = SistemaEcuaciones(A, b)
        print("Matriz Aumentada:")
        sistema.visualizar_matriz_aumentada()

        gauss_jordan = GaussJordan(sistema)
        soluciones = gauss_jordan.resolver()

        print("\nSoluciones del sistema:")
        for i, sol in enumerate(soluciones):
            print(f"x{i} = {sol}")


# Ejecutar el programa
if __name__ == "__main__":
    Main.main()