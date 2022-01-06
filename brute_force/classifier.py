from typing import Tuple, Dict

from .. import abstract_classifier as abs_clf


class BruteForceClassifier(abs_clf.AbstractClassifier):
    def __init__(self, base_points: Dict[str, Tuple[float, ...]]) -> None:
        super().__init__(base_points)
        self.__base_points = base_points

    def execute(self, *coordinates_target: float) -> str:
        for name, coordinates in self.__base_points.items():
            pass
        return super().execute(*coordinates_target)
