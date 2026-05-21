import streamlit as st
import pandas as pd

# Title
st.title("Student Marks Analyzer with Visualization")

# Student Name Input
name = st.text_input("Enter Student Name")

# Marks Input
m1 = st.number_input("Enter marks for Subject 1", min_value=0, max_value=100, step=1)
m2 = st.number_input("Enter marks for Subject 2", min_value=0, max_value=100, step=1)
m3 = st.number_input("Enter marks for Subject 3", min_value=0, max_value=100, step=1)

# Button
if st.button("Calculate"):

    # Validation
    if name == "":
        st.warning("Please enter student name")

    else:
        # Calculate Total and Average
        total = m1 + m2 + m3
        average = total / 3

        # Grade Calculation
        if average >= 90:
            grade = "A"

        elif average >= 75:
            grade = "B"

        elif average >= 50:
            grade = "C"

        else:
            grade = "Fail"

        # Display Results
        st.subheader("Results")

        st.write("Student Name:", name)
        st.write("Total Marks:", total)
        st.write("Average Marks:", round(average, 2))
        st.write("Grade:", grade)

        # Create DataFrame
        data = {
            "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
            "Marks": [m1, m2, m3]
        }

        df = pd.DataFrame(data)

        # Display Table
        st.subheader("Marks Table")
        st.dataframe(df)

        # Bar Chart
        st.subheader("Marks Comparison (Bar Chart)")
        st.bar_chart(df.set_index("Subjects"))

        # Line Chart
        st.subheader("Marks Trend (Line Chart)")
        st.line_chart(df.set_index("Subjects"))