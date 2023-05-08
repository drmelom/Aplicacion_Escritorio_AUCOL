
import pandas as pd
import plotly.graph_objects as go
import numpy
import datetime 
import tkinter as tk

width=580
height=480

Asociados=pd.read_excel('Asociados_df.xlsx',sheet_name="Asociados_df", header=0)
data_base=pd.read_excel('Asociados_df.xlsx',sheet_name="Asociados_df", header=0)
prueba=pd.read_csv('prueba.csv')





def oficio(num_dias,tipo_oficio,fechas):
    
    global data_base
    global Asociados
    df=Asociados.copy()
    
    
    
    for i in range(num_dias*2):
        num_oficios=df[df['TIPO']==1]['N OFICIOS']
        min_num_oficios=int(num_oficios.min())
        postulados=df[(df["N OFICIOS"]==min_num_oficios)&(df["TIPO"]==1)]
       
        asignado = (postulados["CODIGO"].iloc[0])
       
        print(num_dias)
        Asociados.loc[asignado-1,[tipo_oficio]]=fechas[i]
        Asociados.loc[asignado-1,["N OFICIOS"]]+=1
        data_base.loc[asignado-1,["N OFICIOS"]]+=1
        df= df.drop(asignado-1)
        

def generar_oficios():  
    # recuperar el año y mes seleccionados por el usuario
    year = int(year_spinbox.get())
    month = int(month_spinbox.get())

    # crear un objeto datetime para el primer día del mes
    start_date = datetime.date(year, month, 1)

    # calcular el número total de días en el mes
    num_days = (datetime.date(year, month + 1, 1) - start_date).days

    # contar los días específicos y domingos
    num_dias_especificos = 0
    num_domingos = 0
    fechas_especificas = []
    fechas_domingos = []
    for i in range(num_days):
        # crear un objeto datetime para el día actual
        date = start_date + datetime.timedelta(days=i)
        # si el día es martes, jueves o sábado, aumentar el contador de días específicos
        if date.weekday() in [1, 3, 5]:
            num_dias_especificos += 1
            fechas_especificas.append(date.strftime('%d/%m/%Y'))
        # si el día es domingo, aumentar el contador de domingos
        elif date.weekday() == 6:
            num_domingos += 1
            fechas_domingos.append(date.strftime('%d/%m/%Y'))    
    if num_domingos>4:
        num_domingos=4
        quince_dias=fechas_domingos[1::3] 
    quince_dias= [fechas_domingos[1], fechas_domingos[-1]]  
    print("Numero de domingos",num_domingos, "Dias",quince_dias)
    
    oficio(num_dias_especificos,"SACAR BASURA",fechas_especificas*2) 
    oficio(num_domingos//2,"LIMPIEZA DE COMEDOR Y BIBLIOTECA",quince_dias*2)
    oficio(num_domingos,"REALIZACIÓN DE CENA",fechas_domingos*2)
    oficio(num_domingos,"LIMPIEZA JARDÍN",quince_dias*4)
    oficio(num_domingos//4,"LIMPIEZA BICICLETERO",[fechas_domingos[0]]*2)
    oficio(num_domingos//2,"LAVADO DE PATIO",quince_dias*2)
    oficio(num_domingos,"LIMPIEZA DE BAÑOS",fechas_domingos*2)
    oficio(num_domingos,"LIMPIEZA DE COCINA",fechas_domingos*2)
    oficio(num_domingos,"REALIZACIÓN DE ALMUERZO",fechas_domingos*2)
     
    Asociados.fillna("",inplace=True)
    fig = go.Figure(data = [go.Table(header=dict(values = list(Asociados.columns), fill_color = 'paleturquoise', align = "center"),cells = dict(values = [Asociados.CODIGO,Asociados.ASOCIADOS,Asociados.TIPO,Asociados["N OFICIOS"],Asociados["SACAR BASURA"],Asociados["LIMPIEZA DE COMEDOR Y BIBLIOTECA"],Asociados["REALIZACIÓN DE CENA"],Asociados["LIMPIEZA JARDÍN"],Asociados["LIMPIEZA BICICLETERO"],Asociados["LAVADO DE PATIO"],Asociados["LIMPIEZA DE BAÑOS"],Asociados["LIMPIEZA DE COCINA"],Asociados["REALIZACIÓN DE ALMUERZO"]],
    fill_color = 'lavender',align = "center" ))])
    fig.update_layout ( height = 1600 , width = 1250 , margin = dict( r = 20 , l=20 , t = 20 , b = 20 ))                            
    data_base.to_excel("Excel_Sample_out2.xlsx",index=False,sheet_name='Hoja1')
    Asociados.to_excel('Excel_Sample_out.xlsx',index=False,sheet_name='Hoja1')    
    fig.write_image("fig1.pdf")
    fig.show()

def login():
   
    user_id = user_entry.get()
    password = password_entry.get()
    
    
    if user_id == "admin" and password == "password":
    
        master.deiconify()  # Muestra la ventana principal de generación de oficios
    else:
        error_label.config(text="Credenciales inválidas")
        
# Crea la ventana de inicio de sesión
login_window = tk.Tk()
login_window.title("Iniciar sesión")

# Agrega la imagen
canvas = tk.Canvas(login_window, width=500, height=300)
canvas.pack()
img = tk.PhotoImage(file="AUCOL.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Agrega el label con el texto "AUCOL"
label = tk.Label(canvas, text="AUCOL")
label.place(height=100, width=200, x=200, y=20)
label.config(fg="blue", font=("Verdana", 32))
# Agrega el campo de entrada de ID de usuario
user_label = tk.Label(login_window, text="ID de usuario:")
user_label.pack(side=tk.TOP, padx=10, pady=10)
user_entry = tk.Entry(login_window, width=20)
user_entry.pack(side=tk.TOP, padx=10, pady=10)

# Agrega el campo de entrada de contraseña
password_label = tk.Label(login_window, text="Contraseña:")
password_label.pack(side=tk.TOP, padx=10, pady=10)
password_entry = tk.Entry(login_window, width=20, show="*")
password_entry.pack(side=tk.TOP, padx=10, pady=10)

# Agrega el botón "Iniciar sesión"
login_button = tk.Button(login_window, text="Iniciar sesión", command=login)
login_button.pack(side=tk.TOP, padx=10, pady=10)  
error_label = tk.Label(login_window, fg="red")
error_label.pack(side=tk.TOP, padx=10, pady=10) 

    
master = tk.Toplevel()
master.withdraw()
canvas = tk.Canvas(master, width=width, height=height)
canvas.pack()
img = tk.PhotoImage(file="AUCOL.gif")
canvas.create_image(0, 0, anchor=tk.NW, image=img)
label = tk.Label(canvas,text="AUCOL")
label.place(height= 100, width = 200, x = 200, y = 20)
label.config(fg="blue",
            font=("Verdana",32)) 
year_spinbox = tk.Spinbox(master, from_=2023, to=2100, width=4)
year_spinbox.pack(side=tk.LEFT, padx=10, pady=10)
month_spinbox = tk.Spinbox(master, values=list(range(1,13)), width=4)
month_spinbox.pack(side=tk.LEFT, padx=10, pady=10)


botton = tk.Button( canvas, text = "Generar Oficios",relief="solid", command =generar_oficios)
botton.place(height= 100, width = 100, x = 250, y = 150)


tk.mainloop()



      
    

    
        








