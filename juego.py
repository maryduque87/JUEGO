import tkinter as tk
from tkinter import messagebox
import random

# Clase base
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self._nombre = nombre
        self._vida = self.validar_vida(vida)
        self._ataque_base = ataque
        self._defensa = defensa

    def validar_vida(self, vida):
        if vida < 0:
            return 0
        elif vida > 100:
            return 100
        return vida

    def get_vida(self):
        return self._vida

    def set_vida(self, nueva_vida):
        self._vida = self.validar_vida(nueva_vida)

    def get_nombre(self):
        return self._nombre

    def generar_ataque(self):
        return random.randint(int(self._ataque_base * 0.8), int(self._ataque_base * 1.2))

    def atacar(self, objetivo):
        pass

# Subclases con habilidades especiales
class Guerrero(Personaje):
    def atacar(self, objetivo):
        ataque = self.generar_ataque()
        danio = ataque * 1.2 - objetivo._defensa
        danio = max(0, int(danio))
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self._nombre} ataca con fuerza. Ataque: {ataque}, Daño: {danio}"

class Mago(Personaje):
    def atacar(self, objetivo):
        ataque = self.generar_ataque()
        danio = ataque  # Ignora defensa
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self._nombre} lanza un hechizo. Ataque: {ataque}, Daño: {danio} (ignora defensa)"

class Arquero(Personaje):
    def atacar(self, objetivo):
        ataque = self.generar_ataque()
        if ataque > objetivo._defensa:
            danio = (ataque - objetivo._defensa) * 2
        else:
            danio = ataque - objetivo._defensa
        danio = max(0, int(danio))
        objetivo.set_vida(objetivo.get_vida() - danio)
        return f"{self._nombre} dispara una flecha. Ataque: {ataque}, Daño: {danio}"

# Interfaz Gráfica
class JuegoBatalla:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Batalla de Personajes")

        self.usuario_nombre = ""
        self.personaje_usuario = None
        self.jugador_cpu = None

        self.frame_inicio = tk.Frame(root)
        self.frame_inicio.pack()

        tk.Label(self.frame_inicio, text="Ingresa tu nombre:").pack()
        self.entry_nombre = tk.Entry(self.frame_inicio)
        self.entry_nombre.pack()

        tk.Label(self.frame_inicio, text="Elige tu personaje:").pack()
        self.var_personaje = tk.StringVar(value="Guerrero")
        tk.OptionMenu(self.frame_inicio, self.var_personaje, "Guerrero", "Mago", "Arquero").pack()

        tk.Button(self.frame_inicio, text="Iniciar Batalla", command=self.iniciar_juego).pack()

    def crear_personaje(self, tipo, nombre):
        if tipo == "Guerrero":
            return Guerrero(nombre, 100, 30, 20)
        elif tipo == "Mago":
            return Mago(nombre, 80, 40, 10)
        elif tipo == "Arquero":
            return Arquero(nombre, 90, 35, 15)

    def iniciar_juego(self):
        self.usuario_nombre = self.entry_nombre.get()
        tipo = self.var_personaje.get()
        if not self.usuario_nombre:
            messagebox.showwarning("Advertencia", "Debes ingresar un nombre.")
            return

        self.personaje_usuario = self.crear_personaje(tipo, self.usuario_nombre)

        tipo_cpu = random.choice(["Guerrero", "Mago", "Arquero"])
        self.jugador_cpu = self.crear_personaje(tipo_cpu, "CPU - " + tipo_cpu)

        self.frame_inicio.destroy()
        self.mostrar_interfaz_batalla()

    def mostrar_interfaz_batalla(self):
        self.label1 = tk.Label(self.root, text=self.estado_jugador(self.personaje_usuario))
        self.label1.pack()
        self.barra_vida1 = tk.Canvas(self.root, width=100, height=20)
        self.barra_vida1.pack()

        self.label2 = tk.Label(self.root, text=self.estado_jugador(self.jugador_cpu))
        self.label2.pack()
        self.barra_vida2 = tk.Canvas(self.root, width=100, height=20)
        self.barra_vida2.pack()

        self.canvas = tk.Canvas(self.root, width=300, height=100)
        self.canvas.pack()
        self.rect1 = self.canvas.create_rectangle(30, 30, 130, 80, fill="blue")
        self.rect2 = self.canvas.create_rectangle(170, 30, 270, 80, fill="red")

        self.log = tk.Text(self.root, height=10, width=50, state="disabled")
        self.log.pack()

        self.boton_turno = tk.Button(self.root, text="Siguiente Turno", command=self.turno_batalla)
        self.boton_turno.pack()

        self.boton_salir = tk.Button(self.root, text="Salir", command=self.root.destroy)
        self.boton_salir.pack()

        self.actualizar_barras()

    def estado_jugador(self, jugador):
        return f"{jugador.get_nombre()} - Vida: {jugador.get_vida()}"

    def actualizar_interfaz(self):
        self.label1.config(text=self.estado_jugador(self.personaje_usuario))
        self.label2.config(text=self.estado_jugador(self.jugador_cpu))
        self.actualizar_barras()

    def actualizar_barras(self):
        self.barra_vida1.delete("all")
        self.barra_vida2.delete("all")

        vida1 = self.personaje_usuario.get_vida()
        vida2 = self.jugador_cpu.get_vida()

        self.barra_vida1.create_rectangle(0, 0, vida1, 20, fill="green")
        self.barra_vida2.create_rectangle(0, 0, vida2, 20, fill="green")

    def mostrar_log(self, mensaje):
        self.log.config(state="normal")
        self.log.insert(tk.END, mensaje + "\n")
        self.log.config(state="disabled")

    def turno_batalla(self):
        if self.personaje_usuario.get_vida() <= 0 or self.jugador_cpu.get_vida() <= 0:
            self.mostrar_log("El juego ha terminado.")
            return

        mensaje1 = self.personaje_usuario.atacar(self.jugador_cpu)
        self.mostrar_log(mensaje1)
        if self.jugador_cpu.get_vida() <= 0:
            self.mostrar_log(f"{self.jugador_cpu.get_nombre()} ha sido derrotado.")
            self.mostrar_log(f"{self.personaje_usuario.get_nombre()} ha ganado la batalla.")
            self.boton_turno.config(state="disabled")
            self.actualizar_interfaz()
            return

        mensaje2 = self.jugador_cpu.atacar(self.personaje_usuario)
        self.mostrar_log(mensaje2)
        if self.personaje_usuario.get_vida() <= 0:
            self.mostrar_log(f"{self.personaje_usuario.get_nombre()} ha sido derrotado.")
            self.mostrar_log(f"{self.jugador_cpu.get_nombre()} ha ganado la batalla.")
            self.boton_turno.config(state="disabled")

        self.actualizar_interfaz()

# Ejecutar el juego
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoBatalla(root)
    root.mainloop()
