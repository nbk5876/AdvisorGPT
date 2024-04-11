# AdvisorGPT

This project is a proof of concept.  The intent is to prove the feasabilty of a  ciriculum advisor application which can be a tool for advisors.

## Repository

The source code for the Curriculum Advisor Prototype is hosted on GitHub:

[https://github.com/nbk5876/AdvisorGPT](https://github.com/nbk5876/AdvisorGPT)

## Application Flow

![Alt text](https://github.com/nbk5876/nbk5876.github.io/blob/main/AdvisorGPT/Advisor_VHigh_Overview.png?raw=true "Advisor High Level Overview")


![Alt text](https://github.com/nbk5876/nbk5876.github.io/blob/main/AdvisorGPT/Advisor_VHigh_Overview.png?raw=true "Advisor Overview")


## Description

The Curriculum Advisor Prototype is an intelligent system designed to streamline academic advising for students. This tool aids in the planning of course schedules based on a student's academic history, current enrollment, and future degree requirements. It consists of several key components:

1. **Course Catalog**: A comprehensive list of courses available for an Associate  Certificate program, including course ID, title, description, prerequisites, credits, and category. This catalog is an essential resource for both advisors and students to understand the courses offered, their content, and how they fit into the overall curriculum.

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

* **Python Version**: Ensure you have Python installed on your system. This application is compatible with the following Python version:

Python 3.11.9


### Dependencies

* requirements.txt has the list of Python libraries

## Installation

To clone the Curriculum Advisor Prototype project, run this command in your terminal:

```bash
git clone https://github.com/nbk5876/AdvisorGPT.git

### Executing program

* python gui.py

