import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_random_password():
    alphabets = string.ascii_letters
    digits = string.digits
    special_characters = "!@#$%^&()"
    
    length = length_entry.get()
    alphabets_count = alphabets_count_entry.get()
    digits_count = digits_count_entry.get()
    special_characters_count = special_characters_count_entry.get()

    try:
        length = int(length)
        alphabets_count = int(alphabets_count)
        digits_count = int(digits_count)
        special_characters_count = int(special_characters_count)

        characters_count = alphabets_count + digits_count + special_characters_count

        if characters_count > length:
            messagebox.showerror("Error", "Characters total count is greater than the password length")
            return

        password = []

        for i in range(alphabets_count):
            password.append(random.choice(alphabets))

        for i in range(digits_count):
            password.append(random.choice(digits))

        for i in range(special_characters_count):
            password.append(random.choice(special_characters))

        if characters_count < length:
            characters = alphabets + digits + special_characters
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))

        random.shuffle(password)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, "".join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

alphabets_count_label = tk.Label(root, text="Alphabets count:")
alphabets_count_label.grid(row=1, column=0)
alphabets_count_entry = tk.Entry(root)
alphabets_count_entry.grid(row=1, column=1)

digits_count_label = tk.Label(root, text="Digits count:")
digits_count_label.grid(row=2, column=0)
digits_count_entry = tk.Entry(root)
digits_count_entry.grid(row=2, column=1)

special_characters_count_label = tk.Label(root, text="Special characters count:")
special_characters_count_label.grid(row=3, column=0)
special_characters_count_entry = tk.Entry(root)
special_characters_count_entry.grid(row=3, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_random_password)
generate_button.grid(row=4, columnspan=2)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=5, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1)

root.mainloop()
