from typing import Tuple, Dict

from .. import abstract_classifier as abs_clf


class BruteForceClassifier(abs_clf.AbstractClassifier):
    """
    すべての母点に対して距離を計算し、距離が最小の母点に属すると判断する。
    """
    def __init__(self, base_points: Dict[str, Tuple[float, ...]]) -> None:
        super().__init__(base_points)
        self.__base_points = base_points

    def execute(self, *coordinates_target: float) -> str:
        # 次元数が一致しなければエラー
        if len(coordinates_target) != self.dim:
            raise ValueError(
                f'対象の次元数と空間の次元数が一致しません。\n'
                f'対象: {len(coordinates_target)}\n'
                f'空間: {self.dim}'
            )

        # 距離は比較にしか利用しないためルートは取らない。
        name_rsl = None
        distance_rsl = None
        for name, coordinates in self.__base_points.items():
            distance = None
            for position_target, position_ref in zip(coordinates_target,
                                                     coordinates):
                if distance:
                    distance += (position_target - position_ref) ** 2
                else:
                    distance = (position_target - position_ref) ** 2
            if distance is None:
                raise NotImplementedError
            if distance_rsl is None or distance < distance_rsl:
                distance_rsl = distance
                name_rsl = name

        if name_rsl is None:
            raise NotImplementedError
        return name_rsl
