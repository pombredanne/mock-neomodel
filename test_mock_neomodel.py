from mock_neomodel import FakeNode, factory_reset


class Bird(FakeNode):
    def __init__(self, **kwargs):
        super(Bird, self).__init__(**kwargs)


class Sparrow(Bird):
    def __init__(self, **kwargs):
        super(Sparrow, self).__init__(**kwargs)


class Badger(FakeNode):
    def __init__(self, **kwargs):
        super(Badger, self).__init__(**kwargs)


class Goat(FakeNode):
    def __init__(self, **kwargs):
        super(Goat, self).__init__(**kwargs)


def test_fake_category_node():
    Badger(name='bob').save(), Badger(name='tim').save()

    assert 'bob' in [n.name for n in Badger.category().instance.all()]
    assert len(Badger.category().instance) == 2

    Goat(name='shelia').save()
    assert len(Badger.category().instance) == 2
    assert len(Goat.category().instance) == 1


def test_index():
    FakeNode(name='jim').save()
    assert FakeNode.index.get(name='jim').name == 'jim'

    Goat(name='rob').save()
    FakeNode(name='kim').save()
    assert FakeNode.index.get(name='kim').name == 'kim'


def test_reset():
    FakeNode(name='jim').save()
    Badger(name='tim').save()
    factory_reset()
    assert not FakeNode.index.search(name='jim')
    assert not Badger.index.search(name='jim')


def test_inherited_class_has_separate_index():
    factory_reset()
    Sparrow(name='borris').save(), Bird(name='trevor').save()
    assert not FakeNode.index.search(name='borris')
    assert not Bird.index.search(name='borris')
    assert Sparrow.index.search(name='borris')
    assert Bird.index.search(name='trevor')
    import ipdb; ipdb.set_trace()
