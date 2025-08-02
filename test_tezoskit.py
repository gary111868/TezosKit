# test_tezoskit.py
"""
Tests for TezosKit module.
"""

import unittest
from tezoskit import TezosKit

class TestTezosKit(unittest.TestCase):
    """Test cases for TezosKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TezosKit()
        self.assertIsInstance(instance, TezosKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TezosKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
