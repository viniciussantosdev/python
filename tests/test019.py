import customtkinter as tk
janela = tk.CTk()
#configurando a janela principal
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(width=700, height=500)
janela.minsize(width=500,height=400)
janela.resizable(width= True,height= False)
janela.mainloop()