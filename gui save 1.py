#============================================================
# gui.py
# Purpose: User Interface
#============================================================
import tkinter as tk
from tkinter import scrolledtext, messagebox, Label, Entry, Button
#from tkinter import messagebox
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

    course_cat = get_course_cat("Course Catalog Electronics.csv")
    stu_rec = get_stu_rec("student record S001.csv") 
    
    advice = process_query(user_query, course_cat, stu_rec)
    reformatted_advice = reformat_advice(advice)

    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, reformatted_advice)
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Advisor App")

student_record_label = Label(root, text="Student Record:")
student_record_label.pack()

student_record_filename_label = Label(root, text="Student Record Filename")
student_record_filename_label.pack()

program_catalog_label = Label(root, text="Program Catalog:")
program_catalog_label.pack()

program_catalog_filename_label = Label(root, text="Program Catalog Filename")
program_catalog_filename_label.pack()

# Create and pack the widgets
query_label = tk.Label(root, text="Enter your query:")
query_label.pack()

query_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
query_text.pack()

# Insert a default question into query_text
default_question = "Student S001 is an Electronics Technician Associate degree candidate scheduled to graduate at the end of the next quarter. What classes should this student take in order to be positioned to graduate on schedule?"
query_text.insert(tk.END, default_question)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="Advice:")
result_label.pack()

result_text = scrolledtext.ScrolledText(root, height=30, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack()

# Start the GUI event loop
root.mainloop()
