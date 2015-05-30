#!/usr/bin/python2.7
"""Unit tests for secret_test.py

.. moduleauthoer:: Kathy Church <kathy.church@gmail.com>
"""
import unittest
import logging
import secret_test
import inspect

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)

logger = logging.getLogger(secret_test.__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler(secret_test.__name__ + ".log", "w"))
logger.propagate = False

###SOME SECRETS TO TEST###
def secret1(n):
    """This one should pass"""
    return n

def secret2(n):
    """This one should fail when n > 18"""
    if n < 36:
        return n
    else:
        return -1

def secret3(n):
    """This will fail b/c not returning an int"""
    return None

def secret4(a, b):
    """This will fail b/c wrong number of arguments"""
    return a


class SecretValidatorTests(unittest.TestCase):

    def test_success(self):
        """The secret function should pass"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        self.assertTrue(secret_test.validate_secret(secret1, 101))

    def test_bad_secret(self):
        """The secret function should fail"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        self.assertFalse(secret_test.validate_secret(secret2, 19))

    def test_boundary_bad_secret(self):
        """Bad function, but n not large enough to trigger failure"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        self.assertTrue(secret_test.validate_secret(secret2, 18))
                        
    def test_secret_bad_return(self):
        """Secret does not return an int"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        with self.assertRaises(ValueError):
            secret_test.validate_secret(secret3, 100)
                        
    def test_secret_bad_args(self):
        """Secret does not expect an int"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        with self.assertRaises(ValueError):
            secret_test.validate_secret(secret3, 100)

    def test_pass_bad_n_arg(self):
        """Pass validate_secrate invalid n"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        with self.assertRaises(TypeError):
            secret_test.validate_secret(secret1, "not a number")

    def test_pass_bad_secret_arg(self):
        """Pass validate_secrate invalid secret"""
        logger.debug("###Starting Test: " + inspect.getframeinfo(inspect.currentframe())[2])
        with self.assertRaises(ValueError):
            secret_test.validate_secret(55, 300)
        

suite = unittest.TestLoader().loadTestsFromTestCase(SecretValidatorTests)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
