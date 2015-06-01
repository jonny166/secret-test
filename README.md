# secret-test

For a secret function, verify that secret(x) + secret(y) == secret(x+y) for all combinations of primes &lt; n
This program makes the assumption that n is small enough that the list of primes less than it will fit in a list in memory.

## Usage
```python
# test.py
import secret_test

def good_secret(n): 
    return n

def bad_secret(n): 
    return n-1

print secret_test.validate_secret(good_secret, 99)
print secret_test.validate_secret(bad_secret, 99)
```
> $ python2.7 test.py 

> True 

> False

## Installation

Just download secret_test.py.  
The only dependency is python 2.7.

## Tests

You can run the provided test file to verify it is working properly.

> $ ./secret_test_unit_test.py 
> .......
> ----------------------------------------------------------------------
> Ran 7 tests in 0.021s
> 
> OK

## Language Choice

Python is a performant language that is widely used in the backend of many systems.  Its syntax is easy to understand.  In addition, my most recent coding experience has been with Python, making it the most expedient choice for a representative sample. 
