# # task 1:

# class Project:
#     def __init__(self, name: str, budget: int) -> None:
#         self.name = name.lower()
#         self.budget = budget
#
#         self.expenses: int = 0
#         self.is_over: bool = False
#         self.duration: int = 0
#         self.tasks: list[str] = []
#
#     def show_info(self) -> None:
#         print(f"--- Project: {self.name.upper()} ---")
#         print(f"Budget: {self.budget}")
#         print(f"Expenses: {self.expenses}")
#         print(f"Project status: {self.is_over}")
#         print(f"Duration: {self.duration} days")
#         print(f"Tasks: {', '.join(self.tasks)}")
#
#     def add_task(self, task: str) -> None:
#         if task not in self.tasks:
#             self.tasks.append(task)
#
#     def divide_task(self, task: str, sub_tasks: list[str]) -> None:
#         self.tasks.remove(task)
#         self.tasks.extend(sub_tasks)
#
#     def do_task(self, task: str, time: int, price: int) -> None:
#         self.tasks.remove(task)
#         self.budget += price
#         self.duration += time
#         self.is_over = True
#
#     def deposit_budget(self, amount) -> None:
#         if self.budget >= 0:
#             self.budget += amount
#
#
# project_1 = Project("new development", 30000)
# project_1.show_info()
#
# project_1.add_task("programming")
# project_1.add_task("designing")
# project_1.add_task("implement")
# project_1.add_task("test")
# project_1.add_task("posting")
#
# project_1.show_info()
#
# subtasks = ["idea", "variants of realisation", "conception", "resume with customer"]
# project_1.divide_task("programming", subtasks)
#
# project_1.show_info()
#
# project_1.do_task("designing", 2, 200)
# project_1.show_info()

# task 2:


class Phone:
    """
    A class to simulate mobile phone memory and application management.

    Attributes:
        max_memory (float): Total storage capacity in MB.
        used_memory (float): Currently occupied storage in MB.
        if_turned_on (bool): Power status of the device.
        dodatky (Dict[str, float]): Currently installed apps and their base sizes.
        dodatky_versions (Dict[str, float]): Current version numbers of installed apps.
        updates_log (Dict[str, float]): Cumulative size of updates per application.
        downloads_log (Dict[str, float]): History of initial application sizes.
        deletes_log (Dict[str, float]): History of total memory freed per deleted app.
    """

    def __init__(self, dodatky: dict[str, float]) -> None:
        """Initializes the Phone with a set of applications."""
        self.max_memory: float = 100.0
        self.used_memory: float = 0.0
        self.if_turned_on: bool = False  # Changed to bool for better practice
        self.dodatky = dodatky
        self.dodatky_versions: dict[str, float] = {}
        self.updates_log: dict[str, float] = {}
        self.downloads_log: dict[str, float] = {}
        self.deletes_log: dict[str, float] = {}

    def turn_on(self) -> None:
        """Powers on the device."""
        self.if_turned_on = True

    def turn_off(self) -> None:
        """Powers off the device."""
        self.if_turned_on = False

    def current_version(self, name: str) -> None:
        """
        Prints the current version of an installed app.

        Args:
            name (str): The name of the application.
        """
        if not self.if_turned_on:
            print("u did not turned on your phone")
            return

        if name not in self.dodatky:
            print("you dont have such an app")
            return

        version = self.dodatky_versions.get(name)
        if version:
            print(f"dodatok {name} має версію {round(version, 1)}")

    def update_version(self, name: str, update_memory: float) -> None:
        """
        Updates an app, increasing its version and consuming memory.

        Args:
            name (str): Name of the app to update.
            update_memory (float): Memory size of the update in MB.
        """
        if not self.if_turned_on:
            print("u did not turned on your phone")
            return

        if name not in self.dodatky_versions:
            print("you dont have such an app")
            return

        if self.used_memory + update_memory > self.max_memory:
            print("not enough memory")
            return

        self.dodatky_versions[name] += 0.1
        self.used_memory += update_memory

        # Log the update memory consumption
        self.updates_log[name] = self.updates_log.get(name, 0.0) + update_memory
        print(f"You have updated an app {name} it cost you {update_memory} MB")

    def download(self, name: str, memory: float) -> None:
        """
        Downloads and installs a new application.

        Args:
            name (str): Name of the app.
            memory (float): Base size of the app in MB.
        """
        if not self.if_turned_on:
            print("u did not turned on your phone")
            return

        if self.used_memory + memory > self.max_memory:
            print("not enough memory")
            return

        self.dodatky[name] = memory
        self.used_memory += memory
        self.dodatky_versions[name] = 1.0
        self.downloads_log[name] = memory

    def delete_app(self, name: str) -> None:
        """
        Removes an app, its updates, and version info, freeing up memory.

        Args:
            name (str): Name of the app to uninstall.
        """
        if not self.if_turned_on:
            print("u did not turned on your phone")
            return

        if name not in self.dodatky:
            print("App not found")
            return

        # Pop data to clear memory and store for logging
        deleted_base = self.dodatky.pop(name, 0.0)
        deleted_updates = self.updates_log.pop(name, 0.0)
        self.dodatky_versions.pop(name, None)

        total_freed = deleted_base + deleted_updates
        self.used_memory -= total_freed
        self.deletes_log[name] = total_freed
        print(f"Deleted {name}. Freed {total_freed} MB")

    def open_app(self, name: str) -> None:
        """Simulates opening an app."""
        if self.if_turned_on and name in self.dodatky:
            print(f"You have opened an app {name}")

    def close_app(self, name: str) -> None:
        """Simulates closing an app."""
        if self.if_turned_on and name in self.dodatky:
            print(f"You have closed an app {name}")

    def show_memory_usage(self) -> None:
        """Displays a summary of memory consumption and history."""
        print(f"Memory consumed for updates: {self.updates_log}")
        print(f"Memory freed (all deletes): {self.deletes_log}")
        print(f"Memory consumed for apps: {self.downloads_log}")
        print(f"Memory used left in total: {self.used_memory}")
