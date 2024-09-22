import customtkinter
from tkinter import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela =customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de login")
janela.iconbitmap("Playsystem_4_icon-icons.com_66605 (1).ico")
janela.resizable(False, False)

#trabalhando com imagem da tela

img = PhotoImage(file="Acesse e seja feliz.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)
#frame wiggets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20))
label.place(x=25, y=5)

#campos de nomes e senhas do usuario

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de Usuario", width=300, font=("Roboto", 14)).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text="*O campo nome de usuario e de carater obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha de Usuario", width=300, font=("Roboto", 14)).place(x=25, y=175)
label2 = customtkinter.CTkLabel(master=frame, text="*O campo senha de usuario e de carater obrigatorio.", text_color="green", font=("Roboto", 8)). place(x=25, y=205)

#botão de confirmação e de lembrar sempre
chekbox = customtkinter.CTkCheckBox(master=frame, text="Lembra-se de mim sempre").place(x=25, y=235)
Button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=285)
janela.mainloop()