from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Cipher Regènere")
app.iconbitmap('C:\\Users\\PC\\Documents\\pythonProject\\Tkinter\\Cipher_regènere\\Images\\cipher.ico')
app.geometry("880x300")
app.config(bg="#F6F6F6")

def open_help():
    help_text = "Para cifrar entre com um texto normal no bloco da esquerda, o resultdo cifrado irá aparecer no bloco da direita.\n\n\
Para decifrar coloque o texto cifrado no bloco da esquerda e o resultado decifrado irá aparecer no bloco da direita.\n\n\
To encrypt enter normal text in the left block, the encrypted result will appear in the right block.\n\n\
To decrypt enter the cipher text in the left block and the decrypted result will appear in the right block."
    messagebox.showinfo("Help", help_text)

def text_is_alpha(text):
    if text.isalpha():
        return True
    else:
        return False

def encrypt():
    key = chave.get().upper()
    text = text_to_cipher.get("1.0", END).upper()
    key_length = len(key)
    text_length = len(text)
    encrypted = ""
    key_index = 0

    if key_length == 0:
        messagebox.showwarning("Invalid Key", "Please enter a non-empty key\nPor favor, insira uma chave não vazia")
        return

    for i in range(text_length):
        character = text[i]
        if text_is_alpha(character):
            ascii_base = ord('A')
            displacement = (ord(character) - ascii_base + (ord(key[key_index]) - ascii_base)) % 26
            encrypted += chr(ascii_base + displacement)
            key_index = (key_index + 1) % key_length
        else:
            encrypted += character

    text_encrypted.config(state=NORMAL)
    text_encrypted.delete("1.0", END)
    text_encrypted.insert("1.0", encrypted)
    text_encrypted.config(state=DISABLED)

def Decrypt():
    key = chave.get().upper()
    text = text_to_cipher.get("1.0", END).upper()
    key_length = len(key)
    text_length = len(text)
    key_index = 0
    decrypted = ""

    if key_length == 0:
        messagebox.showwarning("Invalid Key", "Please enter a non-empty key\nPor favor, insira uma chave não vazia")
        return
    
    for i in range(text_length):
        character = text[i]
        if text_is_alpha(character):
            ascii_base = ord('A')
            displacement = (ord(character) - ord(key[key_index])) % 26
            decrypted += chr(ascii_base + displacement)
            key_index = (key_index + 1) % key_length
        else:
            decrypted += character

    text_encrypted.config(state=NORMAL)
    text_encrypted.delete("1.0", END)
    text_encrypted.insert("1.0", decrypted)
    text_encrypted.config(state=DISABLED)

def clear():
    text_to_cipher.delete("1.0", END)
    text_encrypted.config(state=NORMAL)
    text_encrypted.delete("1.0", END)
    text_encrypted.config(state=DISABLED)
    chave.delete(0, END)

#Text to cipher
Label(app, text="Text to cipher/decipher: ", font=("Arial", 10), bg="#F6F6F6").grid(row=0, column=0, padx=10, pady=5)
text_to_cipher = Text(app, width=52, height=10, wrap=WORD)
text_to_cipher.config(bg="#F6F6F6", fg="#0072C6")
text_to_cipher.grid(row=1, column=0, padx=10, pady=5)

#Text encrypted
Label(app, text="Text encrypted/decrypted: ", font=("Arial", 10), bg="#F6F6F6").grid(row=0, column=1, padx=10, pady=5)
text_encrypted = Text(app, width=52, height=10, state=DISABLED, wrap=WORD)
text_encrypted.config(bg="#F6F6F6", fg="#0072C6")
text_encrypted.grid(row=1, column=1, padx=10, pady=5)

#Botao para criptografar
button = Button(app, text="Encrypt", font=("Arial", 10), command=encrypt, bg="#0072C6", fg="white")
button.grid(row=2, column=0, padx=10, pady=5)

#Botao para descriptografar
button = Button(app, text="Decrypt", font=("Arial", 10), command=Decrypt, bg="#0072C6", fg="white")
button.grid(row=2, column=1, padx=10, pady=5)

# Botao para limpar
clear_button = Button(app, text="Clear", font=("Arial", 10), command=clear, bg="#0072C6", fg="white")
clear_button.place(x=420, y=211)

#Text para chave
Label(app, text="Key: ", font=("Arial", 10), bg="#F6F6F6").place(x=10, y=245)
chave = Entry(app, width=55)
chave.config(bg="#F6F6F6", fg="#0072C6")
chave.place(x=50, y=249)

# Botao de ajuda
help_button = Button(app, text="Help", font=("Arial", 10), command=open_help, bg="#0072C6", fg="white")
help_button.place(x=800, y=211)

#copyrigth
Label(app, text="© 2023 - João Batista Andrade - Todos os direitos reservados.", font=("Arial", 10), bg="#F6F6F6").place(x=300, y=275)

app.mainloop()
