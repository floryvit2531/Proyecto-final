import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk


def abrir_imagen():
    global imagen, img
    archivo= filedialog.askopenfilename(filetypes=[("Image", ("*.jpg"))])
    img=Image.open(archivo)
    img_tk = img
    img_tk.thumbnail((300,300))
    img_tk= ImageTk.PhotoImage(img_tk)
    imagen=tk.Label(ventana,image=img_tk)
    imagen.image=img_tk
    imagen.pack(pady=30)
    
    
ventana = tk.Tk ()
ventana.geometry ("600x600")
ventana.resizable(0,0)
ventana.title ("Mi Proyecto")
ventana.configure (bg= "black")

frame_azul = tk.Frame (ventana, width=100, height=200)
frame_azul.configure(background= "blue")
frame_azul.pack()

img2=Image.open("abrir_img.png")
img2.thumbnail((50,50))
img2= ImageTk.PhotoImage(img2)

img3=Image.open("rotar_imagen.png")
img3.thumbnail((50,50))
img3= ImageTk.PhotoImage(img3)


texto=tk.Label(master=frame_azul,text="Mi Proyecto")
texto.pack()

def girar_imagen():
    global img
    img = img.rotate(45)
    img4 = img
    imgtk=ImageTk.PhotoImage(img4)
    imagen.image=imgtk
    imagen.configure(image=imgtk)


btn= tk.Button(frame_azul, image=img2, command=abrir_imagen)
btn.pack(pady=40)


btn2= tk.Button(frame_azul, image=img3, command=girar_imagen)
btn2.pack()


ventana.mainloop()