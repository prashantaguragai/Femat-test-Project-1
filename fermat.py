import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
   # You will need to implement this function and change the return value
    # Handling modulo-1 case
    if N == 1:
        return 0

    # Handling base case when exponent becomes zero
    if y == 0:
        return 1 % N

    # Reducing base first
    x = x % N

    # Recursively computing half exponent
    half = mod_exp(x, y // 2, N)

    # Squaring the half result modulo N
    result = (half * half) % N

    # Multiplying by x when exponent is odd
    if y % 2 == 1:
        result = (result * x) % N

    # Returning final modular result
    return result


def fprobability(k):
    # You will need to implement this function and change the return value.
    if k <= 0:
        return 0.0
    return 1.0 - (0.5 ** k)


def mprobability(k):
    # You will need to implement this function and change the return value.
    if k <= 0:
        return 0.0
    return 1.0 - (0.25 ** k)


def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    # Handling small N values
    if N <= 1:
        return 'composite'
    if N <= 3:
        return 'prime'

    # Rejecting even numbers
    if N % 2 == 0:
        return 'composite'

    # Handling non-positive k
    if k <= 0:
        return 'prime'

    # Repeating k random base tests
    for _ in range(k):
        a = random.randint(2, N - 2)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

    return 'prime'


def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    # Handling small N values
    if N <= 1:
        return 'composite'
    if N <= 3:
        return 'prime'

    # Rejecting even numbers
    if N % 2 == 0:
        return 'composite'

    # Handling non-positive k
    if k <= 0:
        return 'prime'

    # Writing N-1 as 2^s * d while keeping d odd
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Repeating k randomized tests
    for _ in range(k):
        a = random.randint(2, N - 2)
        x = mod_exp(a, d, N)

        # Passing immediately if x is 1 or -1 mod N
        if x == 1 or x == N - 1:
            continue

        # Squaring up to s-1 times while looking for N-1
        for _ in range(s - 1):
            x = (x * x) % N
            if x == N - 1:
                break
        else:
            return 'composite'

    return 'prime'
