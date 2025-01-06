def is_bulky(width, height, length):
    if width >= 150: return True
    if height >= 150: return True
    if length >= 150: return True

    if width * height * length >= 1000000: return True

    return False


def is_heavy(mass):
    return mass >= 20


def sort(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return 'REJECTED'
    if bulky or heavy:
        return 'SPECIAL'
    return 'STANDARD'


def test_sort():
    # test bulky -- volume < 1m, but one of the sides >= 150
    assert(sort(200, 10, 10, 1) == 'SPECIAL')

    # test bulky -- volume > 1m
    assert(sort(10000, 10000, 10000, 1) == 'SPECIAL')

    # test heavy
    assert(sort(1, 1, 1, 50) == 'SPECIAL')

    # test that heavy + bulky gets rejected
    assert(sort(10000, 10000, 10000, 50) == 'REJECTED')

    # test that items at the threshold get flagged
    assert(sort(100, 100, 100, 1) == 'SPECIAL')  # volume exactly 1m
    assert(sort(150, 10, 10, 1) == 'SPECIAL')    # one side exactly 150
    assert(sort(10, 10, 10, 20) == 'SPECIAL')    # weight exactly 20

    # test that normal items are standard
    assert(sort(10, 10, 10, 10) == 'STANDARD')

    print('all ok!')


test_sort()


