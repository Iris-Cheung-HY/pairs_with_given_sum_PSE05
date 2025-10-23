from main.main import pairs_with_given_sum

def test_pairs_with_numbers_6():
    # ^rename with meaningful test name
    # and complete test implementation below
    # arrange
    num = [1,2,3,4,5]
    target = 6

    # act
    result = pairs_with_given_sum(num, target)

    # assert
    assert result == 2

def test_pairs_with_numbers_100():
    # ^rename with meaningful test name
    # and complete test implementation below
    # arrange
    num = [97, 51, 49, 35, 3, 65]
    target = 100

    # act
    result = pairs_with_given_sum(num, target)

    # assert
    assert result == 3


def test__duplicate_numbers():
    # ^rename with meaningful test name
    # and complete test implementation below
    num = [1,2,3,2,4,5,4]
    target = 6

    # act
    result = pairs_with_given_sum(num, target)

    # assert
    assert result == 3



def test__zero():
    # ^rename with meaningful test name
    # and complete test implementation below
    num = [1,2,3,2,0,4,5,4,0]
    target = 0

    # act
    result = pairs_with_given_sum(num, target)

    # assert
    assert result == 1

def test__different_order():
    # ^rename with meaningful test name
    # and complete test implementation below
    num = [1,4,2,4,3,2,0,4,5,4,0,2]
    target = 6

    # act
    result = pairs_with_given_sum(num, target)

    # assert
    assert result == 4