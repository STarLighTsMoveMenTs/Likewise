#!/usr/bin/env python3
"""
Tests for LikewiseLightsPeaceSince
"""

import unittest
import time
from likewise_lights_peace_since import LikewiseLightsPeaceSince


class TestLikewiseLightsPeaceSince(unittest.TestCase):
    """Test cases for LikewiseLightsPeaceSince class"""
    
    def test_initialization(self):
        """Test that the class initializes correctly"""
        instance = LikewiseLightsPeaceSince()
        self.assertEqual(len(instance.get_lights()), 0)
        self.assertTrue(instance.peace_state)
        
    def test_add_light(self):
        """Test adding lights"""
        instance = LikewiseLightsPeaceSince()
        instance.add_light("Test Light")
        self.assertEqual(len(instance.get_lights()), 1)
        self.assertEqual(instance.get_lights()[0]['name'], "Test Light")
        
    def test_multiple_lights(self):
        """Test adding multiple lights"""
        instance = LikewiseLightsPeaceSince()
        instance.add_light("Light 1")
        instance.add_light("Light 2")
        instance.add_light("Light 3")
        self.assertEqual(len(instance.get_lights()), 3)
        
    def test_likewise_peace(self):
        """Test the likewise peace message"""
        instance = LikewiseLightsPeaceSince()
        message = instance.likewise_peace()
        self.assertIn("Likewise", message)
        self.assertIn("peace", message)
        
    def test_since_started(self):
        """Test time tracking"""
        instance = LikewiseLightsPeaceSince()
        time.sleep(0.1)  # Wait a bit
        result = instance.since_started()
        self.assertIn("Since started", result)
        self.assertIn("seconds ago", result)


if __name__ == "__main__":
    unittest.main()
