#============================================================
# advise.py
# Purpose:  
#============================================================
import os
from files import get_course_cat
from files import get_stu_rec
from query import process_query

print("Running advise.py")

def main():

	user_query = "Student S001 is an Electronics Technician Associate degree candidate scheduled to graduate next quarter. They have completed all required courses except PHY101, which has been cancelled for the next quarter. The degree requires 3 credits of general education science. Here is the relevant course data and student record. Can you identify an alternative path to graduation for S001?"
	user_query = "Student S001 is an Electronics Technician Associate degree candidate scheduled to graduate at the end of the next quarter. What classes should this student take in order to be positioned to graduate on schedule?"
	#user_query = "Why did the fox jump over the moon?ZZZZZZZ" 
	#user_query = "Is this student missing any courses?"

	#-----------------------------------------------------------
	# Step 1 - Get the Course Catelog
	#-----------------------------------------------------------
	course_cat = get_course_cat("Course Catalog Electronics.csv")

	#-----------------------------------------------------------
	# Step 2 - Get the student's record
	#-----------------------------------------------------------
	stu_rec = get_stu_rec("Student Record S001.csv") 

	#-----------------------------------------------------------
	# Step 3 - Get final NLP text from GPT4
	#-----------------------------------------------------------
	process_query(user_query, course_cat, stu_rec)

if __name__ == "__main__":
	main()

