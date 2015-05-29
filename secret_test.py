"""A secret function test module

This module will test a function to verify that for all primes less
than n, function(x) + function(y) == function(x + y)

.. moduleauthoer:: Kathy Church <kathy.church@gmail.com>
"""

import itertools
import logging
import traceback

logger = logging.getLogger(__name__)

def _get_primes(n):
    """Generator yielding the first n prime numbers

    Args:
      n (int): Yield all primes less than n

    Yields:
      int: The next prime number in the range of 0 to 'n'

    Note:
      Taken from the Python Cookbook
      http://archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=last
    """
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, n-2, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
#end _get_primes


def secret1(n):
    return n

def secret2(n):
    if n < 30:
        return n
    else:
        return -1

def validate_secret(secret, n):
    """Validate secret(x) + secret(y) == secret(x + y) for all combinations primes < n

    Args:
      secret (func): Function to validate. Should expect and return an int.
      n (int): Yield all primes less than n

    Returns:
      Bool: False if secret(x) + secret(y) != secret(x+y) for some primes x and y, otherwise True

    Raises:
      ValueError: If secret is not a function that takes and returns an int
      TypeError: n is not an integer
    """

    if not isinstance(n, (int, long)):
        raise TypeError("n must be an int")
        
    primes = []
    for prime in _get_primes(n):
        try:
            if not all(secret(p + prime) == secret(p) + secret(prime) for p in primes):
                logger.info("secret({0}) + secret(n) != secret({0}+n) for all primes < {0}".format(prime))
                return False
            primes.append(prime)
            
        except ValueError, e:
            logger.error(traceback.format_exc())
            raise ValueError("secret must accept and return an integer")
        except TypeError, e:
            logger.error(traceback.format_exc())
            raise ValueError("secret must accept and return an integer")

    return True
#end validate_secret
