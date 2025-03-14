class SistemaEcuaciones:
    def __init__(self, A, b):
        """
        Inicializa el sistema de ecuaciones lineales.
        :param A: Matriz de coeficientes (lista de listas).
        :param b: Vector de términos independientes (lista).
        """
        self.A = A  # Matriz de coeficientes
        self.b = b  # Vector de términos independientes

    def matriz_aumentada(self):
        """
        Devuelve la matriz aumentada [A | b].
        """
        return [row + [self.b[i]] for i, row in enumerate(self.A)]

    def visualizar_matriz_aumentada(self):
        """
        Muestra la matriz aumentada en la consola.
        """
        print("Matriz Aumentada:")
        for fila in self.matriz_aumentada():
            print(fila)


class GaussJordan:
    def __init__(self, sistema):
        """
        Inicializa el método de Gauss-Jordan.
        :param sistema: Instancia de la clase SistemaEcuaciones.
        """
        self.sistema = sistema
        self.matriz = sistema.matriz_aumentada()

    def intercambiar_filas(self, i, j):
        """
        Intercambia dos filas de la matriz.
        :param i: Índice de la primera fila.
        :param j: Índice de la segunda fila.
        """
        self.matriz[i], self.matriz[j] = self.matriz[j], self.matriz[i]

    def multiplicar_fila_por_escalar(self, fila, escalar):
        """
        Multiplica una fila por un escalar.
        :param fila: Índice de la fila.
        :param escalar: Escalar por el que se multiplica la fila.
        """
        for j in range(len(self.matriz[fila])):
            self.matriz[fila][j] *= escalar

    def sumar_filas(self, fila_a, fila_b, escalar):
        """
        Suma a una fila otra fila multiplicada por un escalar.
        :param fila_a: Fila a la que se suma.
        :param fila_b: Fila que se suma.
        :param escalar: Escalar por el que se multiplica la fila_b.
        """
        for j in range(len(self.matriz[fila_a])):
            self.matriz[fila_a][j] += escalar * self.matriz[fila_b][j]

    def eliminar(self):
        """
        Aplica el método de eliminación Gaussiana para transformar la matriz en su forma escalonada.
        """
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
        """
        Resuelve el sistema de ecuaciones y devuelve las soluciones.
        :return: Lista de soluciones [A, B, C].
        """
        self.eliminar()
        soluciones = [self.matriz[i][-1] for i in range(len(self.matriz))]
        return soluciones


class Main:
    @staticmethod
    def main():
        # Definir el sistema de ecuaciones
        A = [
            [2, 1, 1],
            [1, 2, 1],
            [1, 3, 1]
        ]
        b = [100, 120, 150]

        sistema = SistemaEcuaciones(A, b)
        sistema.visualizar_matriz_aumentada()

        gauss_jordan = GaussJordan(sistema)
        soluciones = gauss_jordan.resolver()

        print("Soluciones encontradas:")
        print(f"Producto A: {soluciones[0]:.2f} unidades")
        print(f"Producto B: {soluciones[1]:.2f} unidades")
        print(f"Producto C: {soluciones[2]:.2f} unidades")

        # Verificación
        for i in range(len(A)):
            suma = sum(A[i][j] * soluciones[j] for j in range(len(soluciones)))
            assert suma == b[i], f"La ecuación {i+1} no se satisface: {suma} != {b[i]}"

# Ejecutar el programa
if __name__ == "__main__":
    Main.main()