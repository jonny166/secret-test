# secret-test

For a secret function, verify that secret(x) + secret(y) == secret(x+y) for all combinations of primes &lt; n

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
$ python2.7 test.py
True
False

## Installation

Just download secret_test.py.  
The only dependency is python 2.7.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

You can run the provided test file to verify it is working properly.

$ ./secret_test_unit_test.py 
.......
----------------------------------------------------------------------
Ran 7 tests in 0.021s

OK

