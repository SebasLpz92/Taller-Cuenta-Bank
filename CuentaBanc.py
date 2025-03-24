class TarjetaCredito:
    def __init__(self, numero_tarjeta, saldo_pendiente=0):
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente

    @staticmethod
    def validar_tarjeta(numero):
        # Implementación del algoritmo de Luhn para validar el número de tarjeta
        def digitos_de(n):
            return [int(d) for d in str(n)]
        digitos = digitos_de(numero)
        digitos_impares = digitos[-1::-2]
        digitos_pares = digitos[-2::-2]
        checksum = sum(digitos_impares)
        for d in digitos_pares:
            checksum += sum(digitos_de(d * 2))
        return checksum % 10 == 0

    def consultar_saldo_pendiente(self):
        return self.saldo_pendiente

    def pagar(self, cantidad):
        if cantidad > 0:
            self.saldo_pendiente -= cantidad
            print(f"Pago realizado. Nuevo saldo pendiente: {self.saldo_pendiente}")
        else:
            print("Cantidad de pago no válida.")

class CuentaBancaria:
    def __init__(self, titular, numero_tarjeta, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.tarjeta = TarjetaCredito(numero_tarjeta)

    def depositar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito realizado. Nuevo saldo: {self.__saldo}")
            else:
                print("Cantidad de depósito no válida.")
        else:
            print("Número de tarjeta no válido.")

    def retirar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro realizado. Nuevo saldo: {self.__saldo}")
            else:
                print("Saldo insuficiente o cantidad de retiro no válida.")
        else:
            print("Número de tarjeta no válido.")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular

    def realizar_pago_tarjeta(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad
                self.tarjeta.pagar(cantidad)
                print(f"Pago realizado desde la cuenta. Nuevo saldo: {self.__saldo}")
            else:
                print("Saldo insuficiente o cantidad de pago no válida.")
        else:
            print("Número de tarjeta no válido.")

def mostrar_menu():
    print("\nMenu - Gestor de Cuentas Bancarias y Tarjetas de Crédito")
    print("1. Crear Cuenta Bancaria")
    print("2. Consultar Saldo de la Cuenta")
    print("3. Consultar Saldo Pendiente de la Tarjeta")
    print("4. Depositar Dinero")
    print("5. Retirar Dinero")
    print("6. Realizar Pago de Tarjeta")
    print("7. Salir")

def main():
    cuenta = None

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            titular = input("Ingrese el nombre del titular: ")
            numero_tarjeta = input("Ingrese el número de la tarjeta: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuenta = CuentaBancaria(titular, numero_tarjeta, saldo_inicial)
            print("Cuenta creada exitosamente.")
        elif opcion == '2':
            if cuenta:
                print(f"Saldo de la cuenta: {cuenta.consultar_saldo()}")
            else:
                print("Primero debe crear una cuenta bancaria.")
        elif opcion == '3':
            if cuenta:
                print(f"Saldo pendiente de la tarjeta: {cuenta.tarjeta.consultar_saldo_pendiente()}")
            else:
                print("Primero debe crear una cuenta bancaria.")
        elif opcion == '4':
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
            else:
                print("Primero debe crear una cuenta bancaria.")
        elif opcion == '5':
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            else:
                print("Primero debe crear una cuenta bancaria.")
        elif opcion == '6':
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a pagar: "))
                cuenta.realizar_pago_tarjeta(cantidad)
            else:
                print("Primero debe crear una cuenta bancaria.")
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()