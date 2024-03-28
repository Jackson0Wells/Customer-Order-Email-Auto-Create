
import tkinter as tk
from tkinter import messagebox, scrolledtext

def generate_email():
    # Gather data from inputs
    customer_name = customer_name_var.get()
    order_number = order_number_var.get()
    street_address = street_address_var.get()
    city_state_zip = city_state_zip_var.get()
    item_list = item_list_text.get("1.0", tk.END).strip()
    your_name = your_name_var.get()
    
    # Generate the subject and email body
    subject = f"Your Order #{order_number} is Being Processed"
    subject_var.set(subject)  # Update the subject variable which is connected to the subject_label

    email_body = (
        f"Dear {customer_name},\n\n"
        "Thank you for your order. We're currently processing the following items:\n\n"
        f"Order Number: #{order_number}\n"
        f"Shipping Address:\n{customer_name}\n{street_address}\n{city_state_zip}\n\n"
        "Items Ordered:\n"
        f"{item_list}\n\n"
        "We will ensure to notify you should there be any updates regarding your order status or shipping details.\n\n"
        "If you require any assistance, please contact us at support@placeholder.co.za.\n\n"
        "Kind regards,\n"
        f"{your_name}\n"
    )
    
    # Update the email body text in the GUI
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", email_body)

def copy_subject():
    # Copy the subject to the clipboard
    root.clipboard_clear()
    root.clipboard_append(subject_var.get())
    messagebox.showinfo("Success", "Subject copied to clipboard!")

def copy_email():
    # Copy the email body to the clipboard
    email_text_to_copy = output_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(email_text_to_copy)
    messagebox.showinfo("Success", "Email copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Email Template Generator")
root.geometry('600x700')

# Define variables
customer_name_var = tk.StringVar()
order_number_var = tk.StringVar()
street_address_var = tk.StringVar()
city_state_zip_var = tk.StringVar()
your_name_var = tk.StringVar()
subject_var = tk.StringVar()  # Variable to hold the subject

# Use frames to organize widgets
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(padx=10, pady=5, fill='x', expand=True)

output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack(padx=10, pady=5, fill='both', expand=True)

# Input widgets with labels
labels = ["Customer Name", "Order Number", "Street Address", "City, State, ZIP", "Your Name"]
variables = [customer_name_var, order_number_var, street_address_var, city_state_zip_var, your_name_var]
for i, (label, var) in enumerate(zip(labels, variables)):
    tk.Label(input_frame, text=label).grid(row=i, column=0, sticky='w')
    entry = tk.Entry(input_frame, textvariable=var, width=40)
    entry.grid(row=i, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Items Ordered (one per line)").grid(row=5, column=0, sticky='nw')
item_list_text = scrolledtext.ScrolledText(input_frame, height=5)
item_list_text.grid(row=5, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(input_frame)
button_frame.grid(row=6, columnspan=2, pady=5)
tk.Button(button_frame, text="Generate Email", command=generate_email).pack(side='left', padx=5)
tk.Button(button_frame, text="Copy Email", command=copy_email).pack(side='left', padx=5)

# Subject label to display the generated subject
tk.Label(root, text="Subject:").pack()
subject_label = tk.Label(root, textvariable=subject_var, relief="sunken", anchor="w", bd=1)
subject_label.pack(fill='x', padx=10, pady=5)

# Button to copy the subject
tk.Button(root, text="Copy Subject", command=copy_subject).pack()

# Output area for email
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack(padx=10, pady=5, fill='both', expand=True)

tk.Label(output_frame, text="Email Body:").pack(anchor='w')
output_text = scrolledtext.ScrolledText(output_frame, height=15)
output_text.pack(fill='both', expand=True)

# Run the application
root.mainloop()
