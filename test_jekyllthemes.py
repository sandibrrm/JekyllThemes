# test_jekyllthemes.py
"""
Tests for JekyllThemes module.
"""

import unittest
from jekyllthemes import JekyllThemes

class TestJekyllThemes(unittest.TestCase):
    """Test cases for JekyllThemes class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JekyllThemes()
        self.assertIsInstance(instance, JekyllThemes)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JekyllThemes()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
