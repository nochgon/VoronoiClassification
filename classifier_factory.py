from typing import Dict, Tuple, Type

from . import abstract_classifier as abs_clf
from . import classifier

DICT_CLASSIFIER: Dict[str, Type[abs_clf.AbstractClassifier]] = {
    'BruteForce': classifier.BruteForceClassifier
}


def create(base_points: Dict[str, Tuple[float, ...]],
           mode: str = 'BruteForce') -> abs_clf.AbstractClassifier:
    if mode in DICT_CLASSIFIER:
        return DICT_CLASSIFIER[mode](base_points)
    else:
        raise ValueError(f'modeが不正です: {mode}')
