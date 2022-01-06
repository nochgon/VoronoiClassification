from abc import ABCMeta, abstractmethod
from typing import Dict, Tuple


class AbstractClassifier(metaclass=ABCMeta):
    def __init__(self, base_points: Dict[str, Tuple[float, ...]]) -> None:
        """
        バリデーションチェックをここでかける。\n
        ・base_pointsに登録された座標の次元が一致していること。
        　・座標の次元はメンバーに持つ。
        """
        # 座標の次元チェック
        num_dim = None
        for coordinates in base_points.values():
            if num_dim:  # 次元が0になることはないため、この判定で行う。
                if len(coordinates) != num_dim:
                    raise ValueError(
                        f'座標の次元が異なる: {len(coordinates)}\n登録座標: {num_dim}'
                    )
            else:
                num_dim = len(coordinates)
        # 母点が一つも無い場合はエラー
        if num_dim is None:
            raise ValueError('母点が一つもありません。')
        # 問題なければ次元数をメンバーに追加
        self.__num_dim = num_dim

    @abstractmethod
    def execute(self, *coordinates: float) -> str:
        pass

    @property
    def dim(self) -> int:
        return self.__num_dim
