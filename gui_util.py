#============================================================
# gui_util.py
# Purpose: User Interface
#============================================================
import tkinter as tk
import csv

def show_csv_in_popup(filename, title):
    """Display the content of a CSV file in a popup window."""
    popup = tk.Toplevel()
    popup.title(title)
    text_area = tk.Text(popup)
    text_area.pack(expand=True, fill='both')
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            text_area.insert(tk.END, ','.join(row) + '\n')
    text_area.config(state=tk.DISABLED)  # Make the text read-only

def show_student_record(student_record_combobox):
    filename = student_record_combobox.get()
    show_csv_in_popup(filename, "Student Record")

def show_program_catalog(program_catalog_combobox):
    filename = program_catalog_combobox.get()
    show_csv_in_popup(filename, "Program Catalog")
