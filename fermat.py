import random


def prime_test(N, k):
    # Main function connected to the GUI button. Do not change.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    """
    Modular exponentiation using repeated squaring (square-and-multiply).
    Computes (x^y) mod N efficiently.

    Time:  O(log y) modular multiplications
    Space: O(1)
    """
    if N == 1:
        return 0

    x = x % N
    result = 1

    while y > 0:
        if (y % 2) == 1:
            result = (result * x) % N
        x = (x * x) % N
        y //= 2

    return result


def fprobability(k):
    """
    Probability that Fermat test answer is correct after k trials.
    Common bound (for non-Carmichael composites):
        P(correct) >= 1 - (1/2)^k

    Time:  O(1)
    Space: O(1)
    """
    if k <= 0:
        return 0.0
    return 1.0 - (0.5 ** k)


def mprobability(k):
    """
    Probability that Miller-Rabin test answer is correct after k trials.
    For composite N, at most 1/4 of bases are strong liars:
        P(correct) >= 1 - (1/4)^k

    Time:  O(1)
    Space: O(1)
    """
    if k <= 0:
        return 0.0
    return 1.0 - (0.25 ** k)


def fermat(N, k):
    """
    Fermat primality test.
    Returns 'prime' or 'composite'.

    For each trial pick random a in [2, N-2] and check:
        a^(N-1) mod N == 1
    If any trial fails -> composite, else probably prime.

    Time:  O(k * log N * M(n))   (M(n) is cost of n-bit multiplication)
    Space: O(1)
    """
    if N <= 1:
        return 'composite'
    if N <= 3:
        return 'prime'
    if N % 2 == 0:
        return 'composite'
    if k <= 0:
        return 'prime'

    for _ in range(k):
        a = random.randint(2, N - 2)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

    return 'prime'


def miller_rabin(N, k):
    """
    Miller-Rabin primality test.
    Returns 'prime' or 'composite'.

    Write N-1 = 2^s * d with d odd.
    For each trial:
      pick a in [2, N-2]
      x = a^d mod N
      if x in {1, N-1}: pass trial
      else repeat s-1 times:
          x = x^2 mod N
          if x == N-1: pass trial
      if never hit N-1: composite

    Time:  O(k * log N * M(n))
    Space: O(1)
    """
    if N <= 1:
        return 'composite'
    if N <= 3:
        return 'prime'
    if N % 2 == 0:
        return 'composite'
    if k <= 0:
        return 'prime'

    # Factor N-1 into 2^s * d (d odd)
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, N - 2)
        x = mod_exp(a, d, N)

        if x == 1 or x == N - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % N
            if x == N - 1:
                break
        else:
            return 'composite'

    return 'prime'