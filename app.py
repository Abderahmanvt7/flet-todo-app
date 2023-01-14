import flet as ft


class Task(ft.UserControl):
    def __init__(self, input_text, remove_task):
        super().__init__()
        self.input = input_text
        self.remove_task = remove_task

    def build(self):
        self.task_checkbox = ft.Checkbox(label=self.input, expand=True)
        self.task_edit = ft.TextField(value=self.input, expand=True)

        self.task_view = ft.Row(
            visible=True,
            controls=[
                self.task_checkbox,
                ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit),
                ft.IconButton(icon=ft.icons.DELETE, on_click=self.remove)
            ]
        )
        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.task_edit,
                ft.IconButton(icon=ft.icons.CHECK, on_click=self.save)

            ]
        )
        return ft.Column(controls=[self.task_view, self.edit_view])

    def edit(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save(self, e):
        self.task_checkbox.label = self.task_edit.value
        self.task_view.visible = True
        self.edit_view.visible = False
        self.update()

    def remove(self, e):
        self.remove_task(self)


class Todo(ft.UserControl):
    def build(self):
        self.input = ft.TextField(hint_text="New Task", expand=True)
        self.tasks = ft.Column()

        view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="ToDos", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Row(
                    controls=[
                        self.input,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_task)
                    ]
                ),
                self.tasks
            ]
        )
        return view

    def add_task(self, e):
        task = Task(self.input.value, self.remove_task)
        self.tasks.controls.append(task)
        self.input.value = ""
        self.update()

    def remove_task(self, task):
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "Todo App"
    page.window_width = 350
    page.window_height = 400
    page.theme_mode = ft.ThemeMode.LIGHT

    todo = Todo()
    page.add(todo)
    page.update()


ft.app(target=main)
