import streamlit as st

st.title("Student Pass Percentage Calculator")

st.write("Enter your marks below:")

project = st.number_input("Project Marks (out of 70)", min_value=0, max_value=70, step=1)
internal = st.number_input("Internal Marks (out of 20)", min_value=0, max_value=20, step=1)
external = st.number_input("External Marks (out of 10)", min_value=0, max_value=10, step=1)

if st.button("Calculate Result"):
    total = project + internal + external
    project_percent = (project / 70) * 100
    internal_percent = (internal / 20) * 100
    external_percent = (external / 10) * 100
    total_percent = (total / 100) * 100
    failed_subjects = []
    if project_percent < 50:
        failed_subjects.append(f"Project ({project} marks)")
    if internal_percent < 50:
        failed_subjects.append(f"Internal ({internal} marks)")
    if external_percent < 50:
        failed_subjects.append(f"External ({external} marks)")
    st.write(f"Total Marks: {total}/100")
    st.write(f"Total Percentage: {total_percent:.2f}%")
    if failed_subjects:
        st.error(f"Failed in: {', '.join(failed_subjects)}")
    else:
        if total_percent >= 90:
            grade = "A+"
        elif total_percent >= 80:
            grade = "A"
        elif total_percent >= 70:
            grade = "B"
        elif total_percent >= 60:
            grade = "C"
        elif total_percent >= 50:
            grade = "D"
        else:
            grade = "F"
        st.success(f"Passed! Grade: {grade}")
