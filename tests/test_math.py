"""
module with very basic tests
"""

import pytest

#------------------------------------------------------------------------------------------
# Basic tests
# pytest -v -s
# -v --- Verbose
# -s --- print statements
# if tagged:
#           run tagged tests with Smoke tag: pytest -sv -m Smoke
#           skip tagged tests with Smoke tag: pytest -sv -m "Not Smoke"
#           execute testcases for more than one tag: pytest -sv -m "Smoke or otherTag"
#------------------------------------------------------------------------------------------


@pytest.fixture(scope="module", autouse=True)
def before_all():
    print(" ")
    print("before all")
    print("---------------------------")
    yield
    print(" ")
    print("after all")
    print("---------------------------")

@pytest.fixture(autouse=True)
def before_after_each():
    print(" ")
    print("beforeEach")
    print("---------------------------")
    yield
    print(" ")
    print("afterEach")
    print("---------------------------")


#OK test
def test_one_plus_one():
    assert 1 + 1 == 2

#Failing test
def test_one_plus_one_wrong():
    assert 1 + 1 == 2

#Verifying an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)

#parameterized
products = [
    (2,3,6),
    (1, 3, 3),
    (0, 3, 0),
    (-1,3,-3),
    (-1,-3, 3),
    (2.5, 6.7, 16.75)
]
@pytest.mark.parametrize('a,b,product',products)
def test_multiply_two_positive_integers(a, b, product):
    assert a * b == product

#skip Test
@pytest.mark.skip('skipping test')
def test_test_skipped():
    assert 1 == 1


a = 101
@pytest.mark.skipif(a>100,reason='skipping test when a > 100')
def test_test_conditionally_skipped():
    assert 1 == 1


#tagging testcases
@pytest.mark.Smoke
def test_test_with_tag():
    print('message: smoke testcase')