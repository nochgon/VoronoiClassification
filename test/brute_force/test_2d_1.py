import pytest

from src import create

base_points = {
    'A': (0, 0),
    'B': (1, 1)
}
classifier = create(base_points, 'BruteForce')

@pytest.mark.parametrize(
    ('x', 'y' , 'name_group'),
    [
        (0.3, 0.3, 'A'),
        (0.7, 0.6, 'B'),
        (-1, -1, 'A'),
        (-1, 1, 'A'),
        (-1, 3, 'B'),
        (1, -1, 'A'),
        (3, -1, 'B'),
        (2, 2, 'B')
    ]
)
def test_2d(x, y, name_group):
    assert classifier.execute(x, y) == name_group
