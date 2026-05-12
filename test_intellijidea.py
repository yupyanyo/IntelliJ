# test_intellijidea.py
"""
Tests for IntelliJIdea module.
"""

import unittest
from intellijidea import IntelliJIdea

class TestIntelliJIdea(unittest.TestCase):
    """Test cases for IntelliJIdea class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IntelliJIdea()
        self.assertIsInstance(instance, IntelliJIdea)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IntelliJIdea()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
