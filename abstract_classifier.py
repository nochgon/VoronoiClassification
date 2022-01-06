from abc import ABCMeta, abstractmethod


class AbstractClassifier(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *possition: float) -> str:
        pass
