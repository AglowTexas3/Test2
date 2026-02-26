from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class TV(Device):
    def turn_on(self) -> None:
        print("TV включен")

    def turn_off(self) -> None:
        print("TV выключен")


class Radio(Device):
    def turn_on(self) -> None:
        print("Радио включено")

    def turn_off(self) -> None:
        print("Радио выключено")


class Remote:
    def __init__(self, device: Device) -> None:
        self._device = device

    def press_on(self) -> None:
        self._device.turn_on()

    def press_off(self) -> None:
        self._device.turn_off()


if __name__ == "__main__":
    remote = Remote(TV())
    remote.press_on()
    remote.press_off()

    remote = Remote(Radio())
    remote.press_on()
    remote.press_off()
