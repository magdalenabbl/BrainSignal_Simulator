import random

from app.neural.ann import ANN


def test_ann_xor_training():

    random.seed(42)

    data = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 0),
    ]

    ann = ANN()

    ann.train(
        data,
        epochs=10000
    )

    assert ann.predict([0, 0]) == 0
    assert ann.predict([0, 1]) == 1
    assert ann.predict([1, 0]) == 1
    assert ann.predict([1, 1]) == 0