# test_meldshard.py
"""
Tests for MeldShard module.
"""

import unittest
from meldshard import MeldShard

class TestMeldShard(unittest.TestCase):
    """Test cases for MeldShard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MeldShard()
        self.assertIsInstance(instance, MeldShard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MeldShard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
