# ImmutableGenerator
Immutable generator implementation via generator factories


```python

    g0 = ImmutableGenerator(lambda: (_ for _ in range(5)))

    v1, g1 = next(g0)
    assert v1 == 0
    v2, g2 = next(g1)
    assert v2 == 1
    v3, g3 = next(g2)
    assert v3 == 2

    again_v1, _ = next(g0)
    assert again_v1 == 0
    again_v1, _ = next(g0)
    assert again_v1 == 0
    again_v3, _ = next(g2)
    assert again_v3 == 2

```
