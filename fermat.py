# Name: Prashanta Guragai
# Project 1: Fermat and Miller-Rabin Primality Testing
# Description: Implementing modular exponentiation, Fermat test, Miller-Rabin test, and probability functions for the GUI.

import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
   # Computing (x^y) mod N using recursive repeated squaring.
    # Time:  O(log y) recursive calls (= O(n) where n is bits of N)
    # Space: O(log y) due to recursion stack
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
    # Computing Fermat correctness probability after k trials: p = 1 - (1/2)^k
    # Time:  O(1)
    # Space: O(1)
    if k <= 0:
        return 0.0
    return 1.0 - (0.5 ** k)


def mprobability(k):
    # Computing Miller-Rabin correctness probability after k trials: p = 1 - (1/4)^k
    # Time:  O(1)
    # Space: O(1)
    if k <= 0:
        return 0.0
    return 1.0 - (0.25 ** k)


def fermat(N, k):
    # Running Fermat test using k random bases a in [2, N-2].
    # Declaring composite if any a^(N-1) mod N != 1, otherwise declaring probably prime.
    # Time:  O(k * log N) calls to modular exponentiation
    # Space: O(1) (plus recursion stack inside mod_exp)
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
    # Running Miller-Rabin test using k random bases.
    # Writing N-1 = 2^s * d (d odd) and checking repeated squaring behavior.
    # Time:  O(k * log N) (mod_exp + up to s squarings per trial)
    # Space: O(1) (plus recursion stack inside mod_exp)
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
