# test_vaultforge.py
"""
Tests for VaultForge module.
"""

import unittest
from vaultforge import VaultForge

class TestVaultForge(unittest.TestCase):
    """Test cases for VaultForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultForge()
        self.assertIsInstance(instance, VaultForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
