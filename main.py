import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import string
import random
import secrets
import math


class Passwordgenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("550x550")
        self.root.title("Password Generator")
        self.root.resizable(False, False)
        self.strength_var  = ctk.StringVar(value="18")
        self.password_var  = ctk.StringVar()
        # call a method to build GUI elements
        self.create_widgets()
    def create_widgets(self):
        ctk.CTkLabel(self.root, text="Enter password length:", font=("Arial", 10)).pack(pady=10)
        strength_value = ctk.CTkEntry(self.root, textvariable=self.strength_var)
        strength_value.pack(pady=10)
        generate_btn = ctk.CTkButton(self.root, text="Generate Password", command=self.generate)
        generate_btn.pack(pady=10)
        ctk.CTkEntry(self.root, textvariable=self.password_var, justify="center", width=230, font=("Arial", 12), state="readonly").pack(pady=10)
        self.entropy_label = ctk.CTkLabel(self.root, text="", font=("Arial", 10))
        self.entropy_label.pack(pady=10)

    def generate(self):
        strength = self.strength_var.get()

        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        password = "".join(secrets.choice(chars) for _ in range(int(strength)))


        # calculate Entroy using the formula E = L * log2(N)
        entropy = int(strength) * math.log2(len(chars))

        if entropy < 28:
            self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits (Very Weak)", text_color="red", font=("Arial", 22, "bold"))
        elif 28 <= entropy < 36:
            self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits (Weak)", text_color="orange", font=("Arial", 22, "bold"))
        elif 36 <= entropy < 60:
            self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits (Medium)", text_color="yellow", font=("Arial", 22, "bold"))
        elif 60 <= entropy < 128:
            self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits (Strong)", text_color="green", font=("Arial", 22, "bold"))
        else:
            self.entropy_label.configure(text=f"Entropy: {entropy:.2f} bits (Very Strong)", text_color="blue", font=("Arial", 22, "bold"))

            # Display the password in the entry box
        self.password_var.set(password)





if __name__ == "__main__":
    root = ctk.CTk()
    app = Passwordgenerator(root)
    root.mainloop()