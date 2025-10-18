import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "CGPA calculator"
)

st.title("Simple CGPA Calculator for UTM students")

grade_list = {
    "Grades" : ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'],
    "Pointer" : [4.00, 4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.67, 0.00]
}

marks = [
    '90-100', '80-89', '75-79', '70-74', '65-69', '60-64', '55-59', '50-54', '45-49', '40-44', '35-39', '30-34', '0-29'
]

gradeList = pd.DataFrame(grade_list, index = marks)

data = {
    "Subject Code": ["","","","",""],
    "Grades": ['','','','',''],
    "Credit Hours": [0,0,0,0,0]
}

courses = pd.DataFrame(data, index = [1,2,3,4,5])

def calculate_gpa(editable_dataframe, currentCGPA, creditCompleted):

    grade_pointer = {
        'A+': 4.00, 'A': 4.00, 'A-': 3.67, 'B+': 3.33, 'B': 3.00, 'B-': 2.67,
        'C+': 2.33, 'C': 2.00, 'C-': 1.67, 'D+': 1.33, 'D': 1.00, 'D-': 0.67, 'E': 0.00
    }

    mata_completed = currentCGPA * creditCompleted

    active_rows = editable_dataframe[editable_dataframe['Credit Hours'] > 0].copy()
    
    active_rows['Pointer'] = active_rows['Grades'].map(grade_pointer)
    mata = active_rows['Pointer'] * active_rows['Credit Hours']
    
    semester_credits = int(active_rows["Credit Hours"].sum())
    semester_mata = float(mata.sum())
    semester_gpa = semester_mata / semester_credits if semester_credits > 0 else 0
    total_cgpa = (semester_mata + mata_completed) / (semester_credits + creditCompleted)

    results = {
        "semester_gpa": round(semester_gpa, 2),
        "new_cgpa": round(total_cgpa, 2),
        "semester_credits": semester_credits,
        "total_credits": semester_credits + creditCompleted,
        "details": active_rows
    }
    return results


with st.form("CGPA form"):
    
    st.subheader("Grade List")
    st.table(gradeList)

    st.divider()

    # columns layout

    col1, col2 = st.columns(2)
    with col1:
        currentCGPA = st.number_input("Enter your current CGPA", min_value = 0.00, max_value = 4.00)
    with col2:
        creditCompleted = st.number_input("Enter your total Credit Completed", step = 1)

    # editable dataframe
    st.subheader("Courses in This Semester")
    editable_dataframe = st.data_editor(courses,
                                        column_config={
                                        "Grades": st.column_config.SelectboxColumn(
                                            "Grade",
                                            options=grade_list["Grades"]
                                        ),
                                        "Credit Hours": st.column_config.NumberColumn(
                                            "Credit Hours",
                                            min_value=0,
                                            max_value=6,
                                            step=1
                                        )
                                    },
                                    # add or remove rows
                                    num_rows="dynamic"
                                    )

    submit_button = st.form_submit_button(label ="Calculate")

    if submit_button:
        
        active_rows = editable_dataframe[editable_dataframe['Credit Hours'] > 0]

        if active_rows.empty:
            st.warning("Please fill in at least one course.")
        
        elif (active_rows['Subject Code'] == '').any() or (active_rows['Grades'] == '').any():
            st.warning("Please fill in all the fields for the courses you've added.")

        # All checks pass
        else:
            st.success("Your form has been submitted!")
            st.balloons()
            calculate_gpa(editable_dataframe, currentCGPA, creditCompleted)
            st.write(calculate_gpa(editable_dataframe, currentCGPA, creditCompleted))


            

