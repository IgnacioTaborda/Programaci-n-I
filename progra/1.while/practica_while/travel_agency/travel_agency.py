# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import tkinter as tk
import customtkinter
import warnings

'''
#!################ INTRODUCCION #################
# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a 
    un listado de viajeros para un nuevo transbordador de SpaceX:
'''
NOMBRE = '' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberás programar el botón 'Cargar Viajeros' para poder cargar los siguientes datos de 5 personas:
    * Nombre
    * Altura (entre 60 cm y 200 cm)
    * Peso (entre 40 kilos y 250 kilos)
    * Edad (entre 1 y 100 ) 

#!################ ACLARACION IMPORTANTE #################
Del punto B solo deberá realizar 2 informes. Para determinar que informe hacer, 
    tenga en cuenta lo siguiente:

    Informe 1- Tome el último número de su DNI Personal (Ej 7) y realice ese informe (Ej, Realizar informe 4 [A y B])
    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 7), y restarselo al numero 9 (Ej 9-7 = 2 [A y B]). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

Realizar los informes correspondientes a los números obtenidos. 
    EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
B) 
    #! 0) 
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de más de 50 años
    #! 1) 
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de menos de 50 años
    #! 2)
        A- El nombre de la persona con la mayor altura ingresada
        B- La cantidad de personas de más de 80 kilos
    #! 3)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 100 kilos
    #! 4) 
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de más de 100 cm de altura
    #! 5) 
        A- El nombre de la persona con la menor edad ingresada
        B- La cantidad de personas de menos de 170 cm de altura 
    #! 6) 
        A- El nombre de las personas que NO superen la edad promedio
        B- La cantidad de personas de menos de 160 cm de altura
    #! 7) 
        A- El nombre de las personas que NO superen la altura promedio
        B- La cantidad de personas de menos de 80 kilos
    #! 8)
        A- El nombre de las personas que NO superen el peso promedio
        B- La cantidad de personas de más  de 50 kilos
    #! 9) 
        A- El nombre de las personas que SI superen el peso promedio
        B- La cantidad de personas de menos de 18 años
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - ◄TravelCode Agency► coded by {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"◄TravelCode Agency► coded by {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./travel_agency/UTN_Travel_Agency_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Viajeros", command=self.btn_cargar_viajeros_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_viajeros_on_click(self):
        pass

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
