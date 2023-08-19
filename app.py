import streamlit as st
import pandas as pd
import plotly.express as px
from db_fxn import (
    create_table,
    add_data,
    view_all_data,
    get_task,
    view_unique_tasks,
    update_task_data,
    delete_data,
)


def main():
    st.title("JJ's To Do App")
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        st.subheader("Add Items")

        col1, col2 = st.columns(2)
        with col1:
            task = st.text_input("Task To Do")
        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Task Added: {}".format(task))
            st.balloons()

    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        with st.expander("View All Data"):
            df = pd.DataFrame(
                result, columns=["Task", "Status", "Due Date"], index=None
            )
            df = df.sort_values(by="Due Date")
            st.dataframe(df)
        with st.expander("Task Status"):
            task_df = df["Status"].value_counts().to_frame()
            task_df = task_df.reset_index()
            df = df.sort_values(by="Due Date")
            st.dataframe(task_df)
            p1 = px.pie(task_df, names="index", values="Status")
            st.plotly_chart(p1)

    elif choice == "Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        with st.expander("Current Data"):
            df = pd.DataFrame(
                result, columns=["Task", "Status", "Due Date"], index=None
            )
            st.dataframe(df)
        list_of_tasks = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Edit", list_of_tasks)
        selected_result = get_task(selected_task)

        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]

            col1, col2 = st.columns(2)
            with col1:
                new_task = st.text_area("Task To Do", task)
            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                update_task_data(
                    new_task,
                    new_task_status,
                    new_task_due_date,
                    task,
                    task_status,
                    task_due_date,
                )
                st.success("Task Updated: {}".format(new_task))
                st.balloons()
                result = view_all_data()
                with st.expander("Current Data"):
                    df = pd.DataFrame(
                        result, columns=["Task", "Status", "Due Date"], index=None
                    )
                    st.dataframe(df)

    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_data()
        with st.expander("Current Data"):
            df = pd.DataFrame(
                result, columns=["Task", "Status", "Due Date"], index=None
            )
            st.dataframe(df)
        list_of_tasks = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Delete", list_of_tasks)
        st.warning("Do you want to delete: {}".format(selected_task))
        if st.button("Delete Task"):
            delete_data(selected_task)
            st.success("Task Deleted: {}".format(selected_task))
            result = view_all_data()
            with st.expander("Updated Data"):
                df = pd.DataFrame(
                    result, columns=["Task", "Status", "Due Date"], index=None
                )
                st.dataframe(df)
    elif choice == "About":
        st.subheader("About JJ's To Do App")
        st.write(
            """
        JJ's To Do App is a streamlined task management system designed to help you efficiently organize and manage your tasks. Whether it's a simple chore or an important deadline, this app will help you keep track of everything you need to do, categorize tasks based on their status, and even set due dates.

        Github Link: https://github.com/espin086/streamlit-crud-app

        Key Features:
        - Add new tasks along with their status and due date.
        - View all your tasks in a clear table format.
        - Update any task's information with a few clicks.
        - Delete tasks once you've completed them or if they are no longer needed.

        **About the Author**:
        JJ Espinoza is an expert AI/ML Cloud Architect with extensive experience in designing and implementing intelligent systems. His expertise in the field ensures this app is built with the latest best practices, offering users a seamless and efficient task management experience.
        """
        )

    pass


if __name__ == "__main__":
    main()
