from mock_neomodel import FakeNode


class Badger(FakeNode):

    def __init__(self, **kwargs):
        super(Badger, self).__init__(**kwargs)


class Goat(FakeNode):

    def __init__(self, **kwargs):
        super(Goat, self).__init__(**kwargs)


def test_fake_category_node():
    bob, tim = Badger(name='bob').save(), Badger(name='tim').save()

    assert 'bob' in [n.name for n in Badger.category().instance.all()]
    assert len(Badger.category().instance) == 2

    Goat(name='shelia').save()
    assert len(Badger.category().instance) == 2
    assert len(Goat.category().instance) == 1
