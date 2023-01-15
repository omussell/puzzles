from euler import multiples_of_3_or_5
from euler import even_fibonacci_numbers

def test_multiples_of_3_or_5():
    assert multiples_of_3_or_5(10) == 23
    assert multiples_of_3_or_5(1000) == 233168

def test_even_fibonacci_numbers():
    assert even_fibonacci_numbers(10) == 44
    assert even_fibonacci_numbers(4000000) == 4613732