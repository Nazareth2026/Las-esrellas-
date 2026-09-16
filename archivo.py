# ==========================================
# DATOS DEL ESTUDIANTE Y PROYECTO[cite: 1]
# Nombre: Nazaret Nicol Jiménez Porón
# Grado y sección: 5° Perito Contador "A"
# Clave: 16
# Materia: Programación
# Videojuego: Las estrellas (Basado en diagrama de flujo y POO)
# ==========================================

# CLASE PADRE
class Personaje:
    def __init__(self, nombre, avatar):
        self.nombre = nombre
        self.avatar = avatar

    def presentarse(self):
        return f"Hola, soy {self.nombre} y mi avatar actual es '{self.avatar}'."


# CLASE HIJA
class Heroe(Personaje):
    def __init__(self, nombre, avatar, herramienta, vidas=3):
        super().__init__(nombre, avatar)  # Hereda atributos de Personaje
        self.herramienta = herramienta
        self.vidas = vidas

    def usar_herramienta(self):
        return f"¡{self.nombre} usa su herramienta '{self.herramienta}' y derrota al enemigo con facilidad!"


def mostrar_bienvenida():
    print("       BIENVENID@ AL VIDEOJUEGO: LAS ESTRELLAS        ")
  
def simular_nivel(heroe):
    print(f"\n[INICIO] Cargando Mundo 1 - Nivel Activo...")
    print(f"Jugador: {heroe.nombre} | Vidas: {heroe.vidas} | Herramienta: {heroe.herramienta}")
    
    # Simulación de encuentro con enemigo usando while
    enemigo_activo = True
    while enemigo_activo and heroe.vidas > 0:
        print("\n¡Cuidado! ¿Aparece un enemigo?")
        opcion_enemigo = input("¿Deseas usar tu herramienta? (s/n): ").strip().lower()
        
        if opcion_enemigo == 's':
            print(heroe.usar_herramienta())
            print("¡Nivel superado con éxito! Otorgando premio especial...")
            enemigo_activo = False
        else:
            print("Decidiste saltar / esquivar al enemigo, pero perdiste una vida.")
            heroe.vidas -= 1
            print(f"Vidas restantes: {heroe.vidas}")
            
            if heroe.vidas <= 0:
                print("\n[GAME OVER] Te has quedado sin vidas. Regresando al Menú Principal...")
                return False
    
    print("¡Llegaste a la Meta! Nivel Completado.")
    print("Avanzando al siguiente mundo y actualizando avance para padres...")
    return True


def main():
    mostrar_bienvenida()
    
    # Primera vez: Permisos y vinculación (según diagrama de flujo)
    print("\n--- CONFIGURACIÓN INICIAL ---")
    permisos = input("¿Aceptas los Permisos de Privacidad? (s/n): ").strip().lower()
    if permisos != 's':
        print("Se requieren permisos para jugar. Saliendo del juego...")
        return
    
    vincular = input("¿Deseas vincular la cuenta de padres para ver avances? (s/n): ").strip().lower()
    if vincular == 's':
        print("[✔] Cuenta vinculada exitosamente con los padres.")
    else:
        print("[i] Continuando sin vinculación de padres.")

    # Creación del personaje inicial
    nombre_jugador = input("\nIngresa el nombre de tu héroe: ")
    avatar_inicial = "Explorador Estelar"
    herramienta_inicial = "Varita Mágica de Estrellas"
    
    # Instanciando la Clase Hija (Heroe)
    mi_heroe = Heroe(nombre_jugador, avatar_inicial, herramienta_inicial, vidas=3)
    print(mi_heroe.presentarse())

    # Menú Principal con bucle while
    ejecutando = True
    while ejecutando:
        print("\n" + "=" * 30)
        print("       MENÚ PRINCIPAL         ")
        print("=" * 30)
        print("1. Cambiar Avatar y Ropa")
        print("2. Empezar Juego (Cargar Mundo 1)")
        print("3. Ver Estado del Héroe")
        print("4. Créditos (Fin)")
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            nuevo_avatar = input("Ingresa el nuevo nombre para tu avatar (Ropa y Herramientas): ")
            mi_heroe.avatar = nuevo_avatar
            print(f"¡Avatar actualizado con éxito! Nuevo avatar: {mi_heroe.avatar}")
            
        elif opcion == '2':
            resultado = simular_nivel(mi_heroe)
            if not resultado:
                # Reiniciar vidas si hay Game Over
                mi_heroe.vidas = 3
                
        elif opcion == '3':
            print(f"\n--- ESTADO DEL JUGADOR ---")
            print(f"Nombre: {mi_heroe.nombre}")
            print(f"Avatar: {mi_heroe.avatar}")
            print(f"Herramienta: {mi_heroe.herramienta}")
            print(f"Vidas: {mi_heroe.vidas}")
            
        elif opcion == '4':
            print("\n" + "=" * 40)
            print(" ¡Gracias por jugar 'Las estrellas'! ")
            print(" Desarrollado por Nazaret Nicol Jiménez Porón[cite: 1]")
            print("=" * 40)
            ejecutando = False
        else:
            print("Opción inválida. Por favor, selecciona un número entre 1 y 4.")

if __name__ == "__main__":
    main()