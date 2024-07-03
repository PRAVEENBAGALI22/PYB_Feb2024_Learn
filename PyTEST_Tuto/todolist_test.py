class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def get_tasks(self):
        return self.tasks


t1 = ToDoList()
t1.add("Work")
t1.add("cook")
t1.add("watch tv")
print(t1.get_tasks())
t1.remove(0)
print(t1.get_tasks())

import pytest


@pytest.fixture()
def todo_lst():
    return ToDoList()


def test_add_task(todo_lst):
    todo_lst.add("Task1")
    assert len(todo_lst.get_tasks()) == 1
    assert todo_lst.get_tasks()[0] == "Task1"


def test_remove_task(todo_lst):
    todo_lst.add("Task1")
    todo_lst.remove(0)
    assert len(todo_lst.get_tasks()) == 0


def test_add_empty_task(todo_lst):
    todo_lst.add(" ")
    assert len(todo_lst.get_tasks()) == 1
    assert todo_lst.get_tasks()[0] == " "
