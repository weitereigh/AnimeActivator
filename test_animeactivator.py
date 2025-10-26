# test_animeactivator.py
"""
Tests for AnimeActivator module.
"""

import unittest
from animeactivator import AnimeActivator

class TestAnimeActivator(unittest.TestCase):
    """Test cases for AnimeActivator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeActivator()
        self.assertIsInstance(instance, AnimeActivator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeActivator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
