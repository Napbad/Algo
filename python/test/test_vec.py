import sys
import os
import unittest

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.linear_list.vec import Vec


class TestVec(unittest.TestCase):
    
    def test_init(self):
        """Test vector initialization"""
        vec = Vec(5)
        self.assertEqual(vec.capacity, 5)
        self.assertEqual(vec.size, 0)
        self.assertEqual(len(vec.vals), 5)
    
    def test_len(self):
        """Test __len__ method"""
        vec = Vec(3)
        self.assertEqual(len(vec), 0)
        
        vec.push(1)
        vec.push(2)
        self.assertEqual(len(vec), 2)
    
    def test_getitem(self):
        """Test __getitem__ method"""
        vec = Vec(3)
        vec.push(10)
        vec.push(20)
        
        self.assertEqual(vec[0], 10)
        self.assertEqual(vec[1], 20)
        
        with self.assertRaises(IndexError):
            _ = vec[2]  # Index out of range
            
        with self.assertRaises(IndexError):
            _ = vec[-1]  # Negative index
    
    def test_setitem(self):
        """Test __setitem__ method"""
        vec = Vec(3)
        vec.push(10)
        vec.push(20)
        
        vec[0] = 15
        self.assertEqual(vec[0], 15)
        
        with self.assertRaises(IndexError):
            vec[2] = 30  # Index out of range
            
        with self.assertRaises(IndexError):
            vec[-1] = 5  # Negative index
    
    def test_push(self):
        """Test push method"""
        vec = Vec(2)
        vec.push(1)
        vec.push(2)
        
        self.assertEqual(vec.size, 2)
        self.assertEqual(vec[0], 1)
        self.assertEqual(vec[1], 2)
        
        # Test resize when capacity is full
        vec.push(3)
        self.assertEqual(vec.size, 3)
        self.assertEqual(vec.capacity, 4)  # Capacity should double
        self.assertEqual(vec[2], 3)
    
    def test_pop(self):
        """Test pop method"""
        vec = Vec(3)
        vec.push(1)
        vec.push(2)
        vec.push(3)
        
        # Pop elements and check values
        self.assertEqual(vec.pop(), 3)
        self.assertEqual(vec.size, 2)
        
        self.assertEqual(vec.pop(), 2)
        self.assertEqual(vec.size, 1)
        
        self.assertEqual(vec.pop(), 1)
        self.assertEqual(vec.size, 0)
        
        # Test popping from empty vector
        with self.assertRaises(IndexError):
            vec.pop()
    
    def test_resize(self):
        """Test resize method"""
        vec = Vec(2)
        vec.push(1)
        vec.push(2)
        
        # This should trigger resize
        vec.push(3)
        self.assertEqual(vec.capacity, 4)
        
        # Fill up to capacity 4
        vec.push(4)
        vec.push(5)  # This should trigger another resize
        self.assertEqual(vec.capacity, 8)
        
        # Test max capacity limit
        # Create a vector with capacity exactly at MAX_CAPACITY so resize() will raise MemoryError
        vec = Vec(Vec.MAX_CAPACITY)
        # Fill it up to MAX_CAPACITY
        for i in range(Vec.MAX_CAPACITY):
            vec.push(i)

        # At this point, size equals capacity, so next push should trigger resize and raise MemoryError
        with self.assertRaises(MemoryError):
            vec.push(Vec.MAX_CAPACITY)
    
    def test_insert(self):
        """Test insert method"""
        vec = Vec(10)
        vec.push(1)
        vec.push(3)
        
        # Insert in the middle
        vec.insert(1, 2)
        self.assertEqual(vec.size, 3)
        self.assertEqual(vec[0], 1)
        self.assertEqual(vec[1], 2)
        self.assertEqual(vec[2], 3)
        
        # Insert at the end with index beyond current size
        vec.insert(10, 4)
        self.assertEqual(vec.size, 4)
        self.assertEqual(vec[3], 4)
        
        # Insert at the beginning
        vec.insert(0, 0)
        self.assertEqual(vec.size, 5)
        self.assertEqual(vec[0], 0)
        self.assertEqual(vec[1], 1)
        self.assertEqual(vec[4], 4)
        
        # Test with negative index
        with self.assertRaises(IndexError):
            vec.insert(-1, -1)
    
    def test_remove(self):
        """Test remove method"""
        vec = Vec(10)
        for i in range(5):
            vec.push(i)
        
        # Remove from middle
        vec.remove(2)  # Remove element at index 2 (value 2)
        self.assertEqual(vec.size, 4)
        self.assertEqual(vec[0], 0)
        self.assertEqual(vec[1], 1)
        self.assertEqual(vec[2], 3)
        self.assertEqual(vec[3], 4)
        
        # Remove from beginning
        vec.remove(0)
        self.assertEqual(vec.size, 3)
        self.assertEqual(vec[0], 1)
        self.assertEqual(vec[1], 3)
        self.assertEqual(vec[2], 4)
        
        # Test invalid indices
        vec.remove(10)  # Index beyond size, should do nothing
        vec.remove(-1)  # Negative index, should do nothing
        self.assertEqual(vec.size, 3)


if __name__ == '__main__':
    unittest.main()