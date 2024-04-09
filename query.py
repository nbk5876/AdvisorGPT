#============================================================
# query.py
# Purpose: 
#============================================================
from openai import OpenAI
client = OpenAI()

def process_query(user_query, course_cat, stu_rec):
    print(f"\nProcessing query for user...")

    # Combining structured data with the natural language query
    prompt = f"The following is a course catalog: {course_cat}\n" \
             f"The following is the student's record: {stu_rec}\n" \
             f"Based on the above information, {user_query}"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that provides academic advising."},
            {"role": "user", "content": prompt}
        ]
    )

    print(completion.choices[0].message)

    return completion.choices[0].message

