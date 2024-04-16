#============================================================
# gui.py
# Purpose: AdvisorGPT User Interface
# Author:  Tony Byorick
# Website: https://nbk5876.wixsite.com/aife/post/advisorgpt
#============================================================
import tkinter as tk
from tkinter import scrolledtext, messagebox, Label, Entry, Button, ttk
import glob
import os
from query import process_query
from files import get_course_cat
from files import get_stu_rec
from util import reformat_advice
from gui_util import show_student_record, show_program_catalog
from mail_util import send_email

def update_filenames_display(student_record_filename, program_catalog_filename):
    student_record_label.config(text=f"Student Record: {student_record_filename}")
    program_catalog_label.config(text=f"Program Catalog: {program_catalog_filename}")

def on_save():
    return

def email_advice():
    # Get the content to be emailed
    #advice_content = result_text.get("1.0", tk.END)  # Replace with actual advice retrieval

    # Retrieve values from GUI elements
    student_record = student_record_combobox.get()
    program_catalog = program_catalog_combobox.get()
    query = query_text.get("1.0", tk.END).strip()
    result = result_text.get("1.0", tk.END).strip()

    # Format the email body
    email_body = f"""Advisor App Session Summary:

Student Transcript: {student_record}
Program Planner: {program_catalog}

Your Query:
{query}

Advice Given:
{result}
"""

    # Send the email
    subject = "AdvisorGPT Session Summary"
    to_email = os.getenv("EMAIL_TO_ACCOUNT")
    from_email = os.getenv("EMAIL_FROM_ACCOUNT")
    from_password = os.getenv("GMAIL_APP_PASSWORD")

    send_email(subject, email_body, to_email, from_email, from_password)

def on_submit():
    user_query = query_text.get("1.0", tk.END).strip()
    if not user_query:
        messagebox.showerror("Error", "Please enter a query.")
        return

    #--------------------------------------
    # Load names of input files and Get Contents
    #--------------------------------------

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

#=============================================================================
#
# Create the main window
#
#=============================================================================
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

# Combobox for selecting a student record file
student_record_label = tk.Label(root, text="Student Transcript:")
student_record_label.grid(row=0, column=1, sticky='e')

student_record_combobox = ttk.Combobox(root)
student_record_combobox.grid(row=0, column=2, sticky='ew')

# Combobox for selecting a course catalog file
program_catalog_label = tk.Label(root, text="Program Planner:")
program_catalog_label.grid(row=1, column=1, sticky='e')

program_catalog_combobox = ttk.Combobox(root)
program_catalog_combobox.grid(row=1, column=2, sticky='ew')

# Populate comboboxes with files
update_combobox(student_record_combobox, "Student Record*.csv")
update_combobox(program_catalog_combobox, "Course Catalog*.csv")

#--------------------
# SHOW Popups
#--------------------

# Create button to show the student record in a popup
btn_show_student_record = tk.Button(
    root,
    text="Show Student Transcript",
    command=lambda: show_student_record(student_record_combobox)  # Pass the combobox as an argument
)
btn_show_student_record.grid(row=0, column=3, sticky='ew', padx=5, pady=5)

# Create button to show the program catalog in a popup
btn_show_program_catalog = tk.Button(
    root,
    text="Show Program Planner",
    command=lambda: show_program_catalog(program_catalog_combobox)  # Pass the combobox as an argument
)
btn_show_program_catalog.grid(row=1, column=3, sticky='ew', padx=5, pady=5)

# Query label and text box
query_label = tk.Label(root, text="Enter your query:")
query_label.grid(row=1, column=0, sticky='w', padx=5, pady=(5, 0))

query_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
query_text.grid(row=2, column=0, columnspan=4, sticky='ew', padx=5)

# Insert a default question into query_text
default_question = "What classes should this student take in order to be positioned to graduate on schedule?  What classes are missing?"
query_text.insert(tk.END, default_question)

# Submit Button
submit_button = tk.Button(root, text="Submit Query", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=(5, 5))

# Save Button
save_button = tk.Button(root, text="Save", command=email_advice)
save_button.grid(row=3, column=3, columnspan=1, sticky='ew', padx=5, pady=(5, 5))

# Result label and text box
result_label = tk.Label(root, text="Advice:")
result_label.grid(row=4, column=0, sticky='w', padx=5, pady=(5, 0))

result_text = scrolledtext.ScrolledText(root, height=30, wrap=tk.WORD, state=tk.DISABLED)
result_text.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

# Set grid row and column configuration for resizing behavior
root.grid_rowconfigure(3, weight=0)

#-----------------------------
# Start the GUI event loop
#-----------------------------
root.mainloop()
