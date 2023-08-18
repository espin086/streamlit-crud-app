import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# Create table


def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS taskTable(task TEXT, task_status TEXT, task_due_date DATE)"
    )


def add_data(task, task_status, task_due_date):
    c.execute(
        "INSERT INTO taskTable(task, task_status, task_due_date) VALUES (?,?,?)",
        (task, task_status, task_due_date),
    )
    conn.commit()


def view_all_data():
    c.execute("SELECT * FROM taskTable")
    data = c.fetchall()
    return data


def view_unique_tasks():
    c.execute("SELECT DISTINCT task FROM taskTable")
    data = c.fetchall()
    return data


def get_task(task):
    c.execute("SELECT * FROM taskTable WHERE task='{}'".format(task))
    data = c.fetchall()
    return data


def update_task_data(
    new_task, new_task_status, new_task_date, task, task_status, task_date
):
    c.execute(
        "UPDATE taskTable SET task =?, task_status=?, task_due_date=? WHERE task=? and task_status=? and task_due_date=?",
        (new_task, new_task_status, new_task_date, task, task_status, task_date),
    )
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(task):
    c.execute("DELETE FROM taskTable WHERE task='{}'".format(task))
    conn.commit()
