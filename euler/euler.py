def multiples_of_3_or_5(limit: int = 10) -> int:
    """
    [1. Multiples of 3 or 5](https://projecteuler.net/problem=1)

    If we list all the natural numbers below 10 that
    are multiples of 3 or 5, we get 3, 5, 6 and 9. The
    sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    ```mermaid
    graph LR
      A[num] --> B{Divisible by 3 or 5?};
      B -->|Yes| C[Append to found_nums];
      C --> D[Increment num+1];
      D --> B;
      B -->|No| E[Ignore];
      E --> D;
      C --> F[sum all found_nums];
      F --> G[result];
    ```
    """
    num: int = 1
    found_nums: list[int] = []
    while num < limit:
        if num % 3 == 0 or num % 5 == 0:
            found_nums.append(num)
        num+=1
    print(sum(found_nums))
    return sum(found_nums)

def even_fibonacci_numbers(limit: int = 10) -> int:
    """
    [2. Even Fibonacci Numbers](https://projecteuler.net/problem=2)

    Each new term in the Fibonacci sequence is generated
    by adding the previous two terms. By starting with 1
    and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence
    whose values do not exceed four million, find the sum
    of the even-valued terms.
    """
    result = 0
    a = 1
    b = 2
    while result <= limit:
        if a % 2 == 0:
            result += a
        a, b = b, a + b
    return result

multiples_of_3_or_5(10)
multiples_of_3_or_5(1000)
