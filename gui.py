#============================================================
# gui.py
# Purpose: User Interface
#============================================================
import tkinter as tk
from tkinter import scrolledtext, messagebox, Label, Entry, Button, ttk
import glob
import os
from query import process_query
from files import get_course_cat
from files import get_stu_rec
from util import reformat_advice

def update_filenames_display(student_record_filename, program_catalog_filename):
    student_record_label.config(text=f"Student Record: {student_record_filename}")
    program_catalog_label.config(text=f"Program Catalog: {program_catalog_filename}")

def on_submit():
    user_query = query_text.get("1.0", tk.END).strip()
    if not user_query:
        messagebox.showerror("Error", "Please enter a query.")
        return

    #--------------------------------------
    # Load names of input files and Get Contents
    #--------------------------------------
    #program_catalog_filename = program_catalog_filename_entry.get()
    #student_record_filename = student_record_filename_entry.get()

    # Fetch selected filenames from Comboboxes
    program_catalog_filename = program_catalog_combobox.get()
    student_record_filename = student_record_combobox.get()

    course_cat = get_course_cat(program_catalog_filename)
    stu_rec = get_stu_rec(student_record_filename) 
    
    #--------------------------------------------
    # Get the advice for this student by calling
    # process_query()
    #--------------------------------------------
    advice = process_query(user_query, course_cat, stu_rec)
    reformatted_advice = reformat_advice(advice) # Make Pretty Print

    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, reformatted_advice)
    result_text.config(state=tk.DISABLED)

def update_combobox(combobox, pattern):
    """Update the given combobox with files matching the pattern in the current folder."""
    files = glob.glob(pattern)
    combobox['values'] = files
    if files:
        combobox.current(0)  # Optionally, set the current selection to the first file




# Create the main window
root = tk.Tk()
root.title("Advisor App")

#-------------------------------------------
# Configure Grid Layout Manager
#-------------------------------------------
root.grid_columnconfigure(0, weight=1)  # Give weight to stretch with the window
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=3)  # Give more weight to result_text column

#----------------------------------
# File Specs 
# Student Record*.csv
# Course Catalog*.csv
#----------------------------------

# Widgets for student record 
#student_record_label = tk.Label(root, text="Student Record:")
#student_record_label.grid(row=0, column=0, sticky='e')
#student_record_filename_entry = tk.Entry(root)
#student_record_filename_entry.insert(0, "Student Record S001.csv")  # Default filename
#student_record_filename_entry.insert(0, "Student Record S002.csv")  # Default filename
#student_record_filename_entry.grid(row=0, column=1, sticky='w')

# Widgets for program catalog
#program_catalog_label = tk.Label(root, text="Program Catalog:")
#program_catalog_label.grid(row=0, column=2, sticky='e')
#program_catalog_filename_entry = tk.Entry(root)
#program_catalog_filename_entry.insert(0, "Course Catalog Electronics.csv")  # Default filename
#program_catalog_filename_entry.insert(0, "Course Catalog Business AA.csv")  # Default filename
#program_catalog_filename_entry.grid(row=0, column=3, sticky='w')

# Combobox for selecting a student record file
student_record_label = tk.Label(root, text="Student Record:")
student_record_label.grid(row=0, column=0, sticky='e')

student_record_combobox = ttk.Combobox(root)
student_record_combobox.grid(row=0, column=1, sticky='ew')

# Combobox for selecting a course catalog file
program_catalog_label = tk.Label(root, text="Program Catalog:")
program_catalog_label.grid(row=1, column=0, sticky='e')

program_catalog_combobox = ttk.Combobox(root)
program_catalog_combobox.grid(row=1, column=1, sticky='ew')

# Populate comboboxes with files
update_combobox(student_record_combobox, "Student Record*.csv")
update_combobox(program_catalog_combobox, "Course Catalog*.csv")

# Query label and text box
query_label = tk.Label(root, text="Enter your query:")
query_label.grid(row=1, column=0, sticky='w', padx=5, pady=(5, 0))

query_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
query_text.grid(row=2, column=0, columnspan=4, sticky='ew', padx=5)

# Insert a default question into query_text
default_question = "Student S001 is an Electronics Technician Associate degree candidate scheduled to graduate at the end of the next quarter. What classes should this student take in order to be positioned to graduate on schedule?"
query_text.insert(tk.END, default_question)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=4, sticky='ew', padx=5, pady=(5, 0))

# Result label and text box
result_label = tk.Label(root, text="Advice:")
result_label.grid(row=4, column=0, sticky='w', padx=5, pady=(5, 0))

result_text = scrolledtext.ScrolledText(root, height=30, wrap=tk.WORD, state=tk.DISABLED)
result_text.grid(row=5, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)

# Set grid row and column configuration for resizing behavior
root.grid_rowconfigure(3, weight=0)

#-----------------------------
# Start the GUI event loop
#-----------------------------
root.mainloop()
