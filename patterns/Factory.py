from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class WindowsButton(Button):
    def render(self) -> None:
        print("Рисуем кнопку Windows")


class LinuxButton(Button):
    def render(self) -> None:
        print("Рисуем кнопку Linux")


class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self) -> None:
        button = self.create_button()
        button.render()


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class LinuxDialog(Dialog):
    def create_button(self) -> Button:
        return LinuxButton()


if __name__ == "__main__":
    dialog: Dialog = WindowsDialog()
    dialog.render()

    dialog = LinuxDialog()
    dialog.render()
