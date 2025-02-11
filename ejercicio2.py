class SistemaEcuaciones:
    def __init__(self, A, b):
        """
        Inicializa el sistema de ecuaciones lineales.
        :param A: Matriz de coeficientes (lista de listas).
        :param b: Vector de términos independientes (lista).
        """
        self.A = A  # Matriz de coeficientes
        self.b = b  # Vector de términos independientes

    def obtener_matriz_coeficientes(self):
        """
        Devuelve la matriz de coeficientes A.
        """
        return self.A

    def obtener_vector_terminos(self):
        """
        Devuelve el vector de términos independientes b.
        """
        return self.b

    def es_diagonal_dominante(self):
        """
        Verifica si la matriz A cumple con la condición de diagonal dominante.
        :return: True si es diagonal dominante, False en caso contrario.
        """
        for i in range(len(self.A)):
            suma = sum(abs(self.A[i][j]) for j in range(len(self.A)) if j != i)
            if abs(self.A[i][i]) < suma:
                return False
        return True


class GaussSeidel:
    def __init__(self, sistema, max_iteraciones=100, tolerancia=1e-10):
        """
        Inicializa el método de Gauss-Seidel.
        :param sistema: Instancia de la clase SistemaEcuaciones.
        :param max_iteraciones: Número máximo de iteraciones.
        :param tolerancia: Tolerancia para verificar la convergencia.
        """
        self.sistema = sistema
        self.max_iteraciones = max_iteraciones
        self.tolerancia = tolerancia
        self.soluciones = [0] * len(sistema.obtener_vector_terminos())

    def iterar(self):
        """
        Realiza las iteraciones del método de Gauss-Seidel.
        :return: Número de iteraciones realizadas.
        """
        for iteracion in range(self.max_iteraciones):
            soluciones_anterior = self.soluciones.copy()
            for i in range(len(self.sistema.obtener_vector_terminos())):
                suma = self.sistema.obtener_vector_terminos()[i]
                for j in range(len(self.sistema.obtener_matriz_coeficientes())):
                    if j != i:
                        suma -= self.sistema.obtener_matriz_coeficientes()[i][j] * self.soluciones[j]
                self.soluciones[i] = suma / self.sistema.obtener_matriz_coeficientes()[i][i]

            if self.verificar_convergencia(soluciones_anterior):
                return iteracion + 1  # Retorna el número de iteraciones realizadas

        return self.max_iteraciones  # Retorna el máximo de iteraciones si no converge

    def verificar_convergencia(self, soluciones_anterior):
        """
        Verifica si las soluciones han convergido.
        :param soluciones_anterior: Soluciones de la iteración anterior.
        :return: True si ha convergido, False en caso contrario.
        """
        for i in range(len(self.soluciones)):
            if abs(self.soluciones[i] - soluciones_anterior[i]) > self.tolerancia:
                return False
        return True


class Main:
    @staticmethod
    def main():
        # Definir un sistema de ecuaciones lineales
        A = [
            [4, -1, 0, 0],
            [-1, 4, -1, 0],
            [0, -1, 4, -1],
            [0, 0, -1, 3]
        ]
        b = [15, 10, 10, 10]

        sistema = SistemaEcuaciones(A, b)

        if not sistema.es_diagonal_dominante():
            print("Advertencia: El sistema no cumple con la condición de diagonal dominante.")

        gauss_seidel = GaussSeidel(sistema)
        iteraciones_realizadas = gauss_seidel.iterar()

        if iteraciones_realizadas < gauss_seidel.max_iteraciones:
            print(f"Convergencia alcanzada en {iteraciones_realizadas} iteraciones.")
            print("Soluciones obtenidas:")
            for i, sol in enumerate(gauss_seidel.soluciones):
                print(f"x{i} = {sol:.6f}")
        else:
            print("El sistema no converge en el número máximo de iteraciones.")


# Ejecutar el programa
if __name__ == "__main__":
    Main.main()