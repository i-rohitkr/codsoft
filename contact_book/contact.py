import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    phone_number = phone_entry.get()
    if phone_number in contacts:
        messagebox.showerror("Error", "Contact with this phone number already exists.")
    else:
        full_name = name_entry.get()
        email = email_entry.get()
        contacts[phone_number] = {'Full Name': full_name, 'Email': email}
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_entries()

def view_contacts():
    if not contacts:
        messagebox.showinfo("Info", "No contacts found.")
    else:
        contact_info = ""
        for phone_number, details in contacts.items():
            contact_info += f"Phone Number: {phone_number}\nFull Name: {details['Full Name']}\nEmail: {details['Email']}\n\n"
        messagebox.showinfo("Contacts", contact_info)

def search_contact():
    phone_number = phone_entry.get()
    if phone_number in contacts:
        details = contacts[phone_number]
        info = f"Full Name: {details['Full Name']}\nEmail: {details['Email']}"
        messagebox.showinfo("Contact Info", info)
    else:
        messagebox.showinfo("Info", "Contact not found.")

def update_contact():
    phone_number = phone_entry.get()
    if phone_number in contacts:
        full_name = name_entry.get()
        email = email_entry.get()
        contacts[phone_number] = {'Full Name': full_name, 'Email': email}
        messagebox.showinfo("Success", "Contact updated successfully.")
        clear_entries()
    else:
        messagebox.showinfo("Info", "Contact not found.")

def delete_contact():
    phone_number = phone_entry.get()
    if phone_number in contacts:
        del contacts[phone_number]
        messagebox.showinfo("Success", "Contact deleted successfully.")
        clear_entries()
    else:
        messagebox.showinfo("Info", "Contact not found.")

def clear_entries():
    phone_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Book")

# Labels
tk.Label(root, text="Phone Number:").grid(row=0, column=0, sticky=tk.W)
tk.Label(root, text="Full Name:").grid(row=1, column=0, sticky=tk.W)
tk.Label(root, text="Email:").grid(row=2, column=0, sticky=tk.W)

# Entry widgets
phone_entry = tk.Entry(root)
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)

# Entry placements
phone_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()