#============================================================
# files.py
# Purpose: Read data course data from local drive
#============================================================
import csv

#-----------------------------------------------------------
# get_course_cat
#-----------------------------------------------------------
def get_course_cat(cat_filename):
    print(f"\nIn get_course_cat with '{cat_filename}':")

    course_cat = []
    try:
        with open(cat_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course_cat.append(row)
        print("Course catalog loaded successfully.")
        print(f"{course_cat}")
        return course_cat  # The catalog as a list of dictionaries
    except FileNotFoundError:
        print(f"File not found: {cat_filename}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

#-----------------------------------------------------------
# get_stu_rec
#-----------------------------------------------------------
def get_stu_rec(stu_filename):
    print(f"\nIn get_stu_rec with '{stu_filename}'':")

    stu_rec = []
    try:
        with open(stu_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stu_rec.append(row)
        print("Course catalog loaded successfully.")
        print(f"{stu_rec}")
        return stu_rec  # The catalog as a list of dictionaries
    except FileNotFoundError:
        print(f"File not found: {stu_filename}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

