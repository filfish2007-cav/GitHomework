from typing import List




class Project:
    def __init__(self, name: str,budget: int) -> None:
        self.name = name.lower()
        self.budget = budget

        self.expenses: int = 0
        self.is_over: bool = False
        self.duration: int = 0
        self.tasks: List[str] = []

    def show_info(self) -> None:
        print(f"--- Project: {self.name.upper()} ---")
        print(f"Budget: {self.budget}")
        print(f"Expenses: {self.expenses}")
        print(f"Project status: {self.is_over}")
        print(f"Duration: {self.duration} days")
        print(f"Tasks: {', '.join(self.tasks)}")

    def add_task(self,task: str) -> None:
        if task not in self.tasks:
            self.tasks.append(task)

    def divide_task(self,task: str,sub_tasks: List[str]) -> None:
        self.tasks.remove(task)
        self.tasks.extend(sub_tasks)

    def do_task(self,task: str, time: int,price: int) -> None:
        self.tasks.remove(task)
        self.budget += price
        self.duration += time
        self.is_over = True

    def deposit_budget(self,amount) -> None:
        if self.budget >= 0:
            self.budget += amount

project_1 = Project("new development", 30000)
project_1.show_info()

project_1.add_task("programming")
project_1.add_task("designing")
project_1.add_task("implement")
project_1.add_task("test")
project_1.add_task("posting")

project_1.show_info()

subtasks = ["idea", "variants of realisation", "conception", "resume with customer"]
project_1.divide_task("programming", subtasks)

project_1.show_info()

project_1.do_task("designing", 2, 200)
project_1.show_info()






