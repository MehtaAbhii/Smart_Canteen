import tkinter as tk
from tkinter import messagebox
import mysql.connector

root = tk.Tk()
root.title("Data Entry Form")

# Create labels and entry widgets for each input field
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

contact_label = tk.Label(root, text="Contact:")
contact_label.pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

payment_method_label = tk.Label(root, text="Payment Method:")
payment_method_label.pack()
payment_method_entry = tk.Entry(root)
payment_method_entry.pack()

item_name_label = tk.Label(root, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(root)
item_name_entry.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

staff_id_label = tk.Label(root, text="Staff ID:")
staff_id_label.pack()
staff_id_entry = tk.Entry(root)
staff_id_entry.pack()

def submit_form():
    name = name_entry.get()
    contact = contact_entry.get()
    address = address_entry.get()
    amount = amount_entry.get()
    payment_method = payment_method_entry.get()
    item_name = item_name_entry.get()
    quantity = quantity_entry.get()
    staff_id = staff_id_entry.get()

    try:
        connection = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="384507", database="canteen_management")
        cursor = connection.cursor()
        query = "INSERT INTO employee(name, contact, address, amount, payment_method, item_name, quantity, staff_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (name, contact, address, amount, payment_method, item_name, quantity, staff_id)  # Removed type conversion
        cursor.execute(query, data)
        connection.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

display_text = tk.Text(root, height=10, width=50)
display_text.pack()

def display_data():
    try:
        connection = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="384507", database="canteen_management")
        cursor = connection.cursor()
        query = "SELECT * FROM employee"
        cursor.execute(query)
        records = cursor.fetchall()
        
        display_text.delete(1.0, tk.END)  # Clear previous content
        for record in records:
            display_text.insert(tk.END, f"Name: {record[0]}\nContact: {record[1]}\nAddress: {record[2]}\nAmount: {record[3]}\nPayment Method: {record[4]}\nItem Name: {record[5]}\nQuantity: {record[6]}\nStaff ID: {record[7]}\n\n")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
display_button = tk.Button(root, text="Display Data", command=display_data)
display_button.pack()

# Run the main loop
root.mainloop()