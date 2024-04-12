#============================================================
# gui_util.py
# Purpose: User Interface
#============================================================
import tkinter as tk
from tkinter import ttk
import csv

def show_csv_in_popup(filename, title):
    """Display the content of a CSV file in a popup window with a table view."""
    popup = tk.Toplevel()
    popup.title(title)

    # Create the Treeview widget without the initial tree column
    tree = ttk.Treeview(popup, show='headings')
    
    # Open the CSV file and populate the Treeview with rows and columns
    with open(filename, newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        
        # Assuming the first row is the header
        columns = next(reader)
        tree['columns'] = columns

        # Formatting the columns
        for col in columns:
            tree.heading(col, text=col)  # Set the headings for each column
            tree.column(col, width=120, anchor=tk.W)  # Set the column properties

        # Inserting the items to the Treeview
        for row in reader:
            tree.insert("", tk.END, values=row)  # Insert row values

    # Pack the Treeview widget with scrollbars
    vsb = ttk.Scrollbar(popup, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(popup, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=hsb.set)
    
    tree.pack(expand=True, fill='both')

def show_student_record(student_record_combobox):
    filename = student_record_combobox.get()
    show_csv_in_popup(filename, "Student Record")

def show_program_catalog(program_catalog_combobox):
    filename = program_catalog_combobox.get()
    show_csv_in_popup(filename, "Program Catalog")
