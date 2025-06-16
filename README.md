# JUEGO
# 1. **Importación de módulos**

* tkinter: Librería para crear interfaces gráficas en Python.
* messagebox: Se usa para mostrar ventanas emergentes.
* random: Para generar números aleatorios (por ejemplo, para ataques).


# 2. Clase base "Personaje" 
class Personaje:</br>
    def __init__(self, nombre, vida, ataque, defensa):</br>
Esta es la **clase madre** de los personajes. Define los atributos y comportamientos comunes:

* nombre: Nombre del personaje.
* vida: Puntos de vida (entre 0 y 100).
* ataque_base: Valor base del ataque.
* defensa: Capacidad de defenderse.

## Métodos importantes:

* validar_vida(vida): Asegura que la vida esté entre 0 y 100.
* generar_ataque(): Devuelve un valor de ataque aleatorio basado en el ataque base.
* atacar(objetivo): Es un método vacío, será sobreescrito por las subclases.

# 3. **Subclases: Guerrero, Mago y Arquero**
Cada una representa un tipo diferente de personaje con su forma de atacar.</br>

## Guerrero
class Guerrero(Personaje):</br>
    def atacar(self, objetivo):</br>

* Usa su fuerza: multiplica el ataque por 1.2 y lo resta con la defensa del objetivo.

## Mago
class Mago(Personaje):</br>
    def atacar(self, objetivo):</br>

* Lanza hechizos: ignora la defensa del enemigo completamente.

## Arquero
class Arquero(Personaje):</br>
    def atacar(self, objetivo):</br>

* Si el ataque supera la defensa, hace el doble de daño. Si no, solo la diferencia.

# 4. Clase principal del juego: "JuegoBatalla"
Esta clase controla **toda la interfaz gráfica** y la **lógica del combate**.</br>

## Constructor "__init__"

def __init__(self, root):</br>
* Crea la ventana inicial donde el usuario:

  * Ingresa su nombre.
  * Elige su tipo de personaje.
  * Hace clic en "Iniciar Batalla".

## Método "crear_personaje()"
def crear_personaje(self, tipo, nombre):</br>
* Crea un objeto del tipo de personaje elegido (Guerrero, Mago o Arquero).

## Método "iniciar_juego()"
def iniciar_juego(self):</br>

* Toma el nombre y tipo de personaje del jugador.
* Crea un enemigo aleatorio para la CPU.
* Cambia la interfaz a la de batalla.

##  Método "mostrar_interfaz_batalla()"
def mostrar_interfaz_batalla(self):</br>

* Crea:

  * Las barras de vida de ambos personajes.
  * Un pequeño campo de batalla visual.
  * Un área de texto para mostrar el registro de acciones.
  * Botones para turno y salir.


## Métodos auxiliares:

- **estado_jugador(jugador)**
Devuelve una cadena con el nombre y la vida actual del personaje.

- **actualizar_interfaz()**
Actualiza los textos y las barras de vida.
- **actualizar_barras()**
Dibuja las barras de vida verdes proporcionales a los puntos de vida restantes.
- **mostrar_log(mensaje)**
Muestra mensajes en el área de texto (registro del combate).

##  Método principal del combate: "turno_batalla()"
def turno_batalla(self):</br>
Cada vez que haces clic en "Siguiente Turno":

1. Tu personaje ataca primero.
2. Se muestra el daño en el log.
3. Si el enemigo muere, termina el juego y se anuncia el ganador.
4. Si no, el enemigo contraataca.
5. Si tú mueres, también se anuncia el ganador y termina el juego.
6. En ambos casos, se desactiva el botón de turno para que no se pueda seguir.

##  5. **Bloque principal del programa**
if __name__ == "__main__":</br>
    root = tk.Tk()</br>
    juego = JuegoBatalla(root)</br>
    root.mainloop()</br>
Este bloque:

* Crea la ventana principal (`root`).
* Inicia la clase `JuegoBatalla`.
* Ejecuta el bucle de eventos de `tkinter`.



