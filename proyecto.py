import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk


def abrir_imagen():
    global imagen
    archivo= filedialog.askopenfilename(filetypes=[("Image", ("*.jpg"))])
    img=Image.open("C:\\Users\\marif\\Downloads\\flores-bonitas.jpg")
    img.thumbnail((300,300))
    img= ImageTk.PhotoImage(img)
    imagen=tk.Label(ventana,image=img)
    imagen.image=img
    imagen.pack(pady=30)
    
    
ventana = tk.Tk ()
ventana.geometry ("600x600")
ventana.resizable(0,0)
ventana.title ("Mi Proyecto")
ventana.configure (bg= "black")

frame_azul = tk.Frame (ventana, width=100, height=200)
frame_azul.configure(background= "blue")
frame_azul.pack()

img2=Image.open("C:\\Users\\marif\\Downloads\\abrir_img.jpg")
img2.thumbnail((50,50))
img2= ImageTk.PhotoImage(img2)

img3=Image.open("C:\\Users\\marif\\Downloads\\rotar_imagen.jpg")
img3.thumbnail((50,50))
img3= ImageTk.PhotoImage(img3)


texto=tk.Label(master=frame_azul,text="Mi Proyecto")
texto.pack()

def girar_imagen():
    img4=Image.open("C:\\Users\\marif\\Downloads\\flores-bonitas.jpg")
    img4=img4.rotate(45)
    imgtk=ImageTk.PhotoImage(img4)
    imagen.image=imgtk
    imagen.configure(image=imgtk)


btn= tk.Button(frame_azul, image=img2, command=abrir_imagen)
btn.pack(pady=40)


btn2= tk.Button(frame_azul, image=img3, command=girar_imagen)
btn2.pack()


ventana.mainloop()