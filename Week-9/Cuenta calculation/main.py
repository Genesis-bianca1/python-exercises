
class Cuenta:
  def __init__(self, iban, nombre_completo, saldo_total):
      self.iban = iban
      self.nombre_completo = nombre_completo
      self.saldo_total = saldo_total

  def ingresar_dinero(self, cantidad):
      if cantidad > 0:
          self.saldo_total += cantidad
          print(f"Ingreso exitoso. Nuevo saldo: {self.saldo_total}")
      else:
          print("La cantidad a ingresar debe ser mayor que cero.")

  def retirar_dinero(self, cantidad):
      if cantidad > 0:
          if cantidad <= self.saldo_total:
              self.saldo_total -= cantidad
              print(f"Retiro exitoso. Nuevo saldo: {self.saldo_total}")
          else:
              print("Fondos insuficientes para el retiro.")
      else:
          print("La cantidad a retirar debe ser mayor que cero.")
if __name__ == "__main__":
# Crear tres objetos de la clase Cuenta
  cuenta1 = Cuenta("ES00 1234 5678 9123 4567 8901", "Ana García", 1000)
  cuenta2 = Cuenta("ES11 9876 5432 1098 7654 3210", "Carlos Ruiz", 2500)
  cuenta3 = Cuenta("ES22 1357 2468 9753 1357 2468", "Luisa Fernández", 500)

# Ejemplo de uso de los nuevos métodos
  cuenta1.ingresar_dinero(500)
  cuenta1.retirar_dinero(300)

  print(cuenta1, cuenta2, cuenta3)



