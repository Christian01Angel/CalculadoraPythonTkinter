import tkinter as tk
from tkinter import ttk, Frame


class Ventana(tk.Tk):
    variable_texto = ''

    def __init__(self):
        super().__init__()
        self.title('Calculadora')
        self.geometry('420x320')
        self._crear_frame()
        self._crear_componentes()

    def _crear_frame(self):
        self.frame_entrada = Frame(self, width=450, height=100)
        self.frame_entrada.grid(row=0, column=0)
        self.frame_botones = Frame(self, width=450, height=350)
        self.frame_botones.grid(row=1, column=0)

    def _crear_componentes(self):
        self.entrada = tk.Entry(self.frame_entrada, textvariable=self.variable_texto, width=30, justify=tk.RIGHT)
        self.entrada.grid(column=0, row=0, columnspan=4, pady=0, padx=0, ipadx=40, ipady=10)

        self._crear_boton('9', 2, 0, lambda: self._agregar_calculo('9'))
        self._crear_boton('8', 2, 1, lambda: self._agregar_calculo('8'))
        self._crear_boton('7', 2, 2, lambda: self._agregar_calculo('7'))
        self._crear_boton('C', 2, 3, self._limpiar)

        self._crear_boton('6', 3, 0, lambda: self._agregar_calculo('6'))
        self._crear_boton('5', 3, 1, lambda: self._agregar_calculo('5'))
        self._crear_boton('4', 3, 2, lambda: self._agregar_calculo('4'))
        self._crear_boton('', 3, 3, lambda: self._agregar_calculo(''))

        self._crear_boton('3', 4, 0, lambda: self._agregar_calculo('3'))
        self._crear_boton('2', 4, 1, lambda: self._agregar_calculo('2'))
        self._crear_boton('1', 4, 2, lambda: self._agregar_calculo('1'))
        self._crear_boton('/', 4, 3, lambda: self._agregar_calculo('/'))

        self._crear_boton('.', 5, 0, lambda: self._agregar_calculo('.'))
        self._crear_boton('0', 5, 1, lambda: self._agregar_calculo('0'))
        self._crear_boton('+', 5, 2, lambda: self._agregar_calculo('+'))
        self._crear_boton('-', 5, 3, lambda: self._agregar_calculo('-'))

        self._crear_boton('=', 6, 0, self._igual)
        self._crear_boton('(', 6, 1, lambda: self._agregar_calculo('('))
        self._crear_boton(')', 6, 2, lambda: self._agregar_calculo(')'))

    def _crear_boton(self, texto, renglon, columna, funcion):
        boton = ttk.Button(self.frame_botones, text=texto, command=funcion)
        boton.grid(row=renglon, column=columna, padx=5, pady=5, ipadx=10, ipady=10)

    def _agregar_calculo(self, texto):
        self.variable_texto += texto
        self.entrada.insert(tk.END, texto)

    def _limpiar(self):
        self.variable_texto = ''
        self.entrada.delete(0, tk.END)

    def _igual(self):
        resultado = eval(self.variable_texto)
        self._limpiar()
        self.entrada.insert(tk.END, resultado)
        self.entrada.select_range(0, tk.END)
        self.entrada.focus()

    def _borrar(self):
        largo = len(self.variable_texto)
        texto = self.variable_texto[0:largo - 2]
        self.entrada.insert(0, texto)


if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()
