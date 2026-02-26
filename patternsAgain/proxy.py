from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: выполняю реальный запрос")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self._check_access():
            self._real_subject.request()
            self._log_access()

    def _check_access(self) -> bool:
        print("Proxy: проверка доступа перед реальным запросом")
        return True

    def _log_access(self) -> None:
        print("Proxy: логирование запроса")


if __name__ == "__main__":
    real = RealSubject()
    proxy = Proxy(real)
    proxy.request()
