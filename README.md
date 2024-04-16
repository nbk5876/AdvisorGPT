# AdvisorGPT

This project is a proof of concept to determine the feasibility of using a large language model like ChatGPT together with a conventional programming language like  Python to build an application that can serve as a tool for scholastic curriculum advisors.

## Repository

The source code for the Curriculum Advisor Prototype is hosted on GitHub:

[https://github.com/nbk5876/AdvisorGPT](https://github.com/nbk5876/AdvisorGPT)

## Application Flow


In steps 1, 2, & 3, the query is created based on input data consisting of the program catalog, the student record and one or more questions from the scholastic advisor.  In step 4 the query is sent to ChatGPT-4 which evaluates the inputs and returns the resulting analysis to the advisor.

![Alt text](https://github.com/nbk5876/nbk5876.github.io/blob/main/AdvisorGPT/Advisor_VHigh_Overview.png?raw=true "Advisor Overview")

---

![Alt text](https://github.com/nbk5876/nbk5876.github.io/blob/main/AdvisorGPT/Advisor_Overview.png?raw=true "Advisor Overview")


## Description

The Curriculum Advisor Prototype is an intelligent application designed to streamline academic advising for students. This tool aids in the planning of course schedules based on a student's academic history, current enrollment, and future degree requirements. It consists of several key components:

1. **Program Catalog**: A comprehensive list of courses available for an Associate  Certificate program, including course ID, title, description, prerequisites, credits, and category. This catalog is an essential resource for both advisors and students to understand the courses offered, their content, and how they fit into the overall curriculum.

2. **Student Record**: A summary of a student's academic history, including the student's ID, courses previously taken with grades, currently enrolled courses, and cumulative GPA. This record is critical for understanding a student's academic journey and assessing their progress toward degree completion.

3. **Advisor Question**: A query entered by the academic advisor which questions the student's academic path. For example, it can generate queries about which classes a student should take to graduate within a certain timeframe.

4. **GPT Advisor**: At the core of the system is the GPT-4 powered advising engine. This advanced AI uses the student's academic record and the course catalog to provide tailored advice on course selection. It ensures that recommendations meet the degree requirements and consider the prerequisites for each course.

5. **Recommendation Output**: The advisor generates a customized recommendation in response to the advisor question. It outlines the suggested courses a student should take to meet their academic goals, complete with prerequisites and an explanation of how these courses fit into their educational plan.

Overall, the Curriculum Advisor Prototype exemplifies the integration of AI with educational planning, delivering personalized course guidance that aligns with a student's aspirations, academic standing, and the requisites of their chosen field of study.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Before you begin, ensure you have met the following requirements:

* **Operating System**: Windows 10 or higher. The application is developed for the Windows environment and leverages specific system features that are not available in other operating systems.

* **Python Version**: Ensure you have Python version 3.11.9 or higher installed on your system. 

### Dependencies

* requirements.txt has the list of Python libraries which are used by the application.

## Installation

To create a clone of the Curriculum Advisor Prototype project, run this command in a DOS window:

```bash
git clone https://github.com/nbk5876/AdvisorGPT.git

### Executing program

* python gui.py


1. Set OPENAI_API_KEY into the Environment using
   system envionment variable editor

2. Create Github folder and CD into it with:
      cd THISPC\OneDrive\Documents\Tony\Github\AdvisorGPT

3. git clone https://github.com/nbk5876/AdvisorGPT.git

4. CD into AdvisorGPT and RUN:
      python -m venv venv
         Note: This command creates a new folder named venv in the
         project directory, where all the virtual environment files
         will be stored.

5. .\venv\Scripts\activate

6. pip install -r requirements.txt

7. python gui.py

