class OldPrinter:
    def print_text(self, text: str) -> None:
        print(f"Старый принтер печатает: {text}")


class NewPrinterInterface:
    def print(self, message: str) -> None:
        raise NotImplementedError


class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer: OldPrinter) -> None:
        self._old_printer = old_printer

    def print(self, message: str) -> None:
        # адаптируем новый интерфейс к старому
        self._old_printer.print_text(message)


if __name__ == "__main__":
    old = OldPrinter()
    adapter = PrinterAdapter(old)
    adapter.print("Привет через адаптер!")
