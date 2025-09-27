import sys
import os
import unittest

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.linear_list.queue import Queue


class TestQueue(unittest.TestCase):
    
    def test_init(self):
        """Test queue initialization"""
        queue = Queue(5)
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)
    
    def test_enqueue(self):
        """Test enqueue method"""
        queue = Queue(3)
        queue.enqueue(1)
        self.assertEqual(len(queue), 1)
        self.assertFalse(queue.is_empty())
        
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(len(queue), 3)
        
        with self.assertRaises(Exception):
            queue.enqueue(4)  # Queue is full
    
    def test_dequeue(self):
        """Test dequeue method"""
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue elements and check values (FIFO order)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(len(queue), 2)
        
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(len(queue), 1)
        
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())
        
        # Test dequeue from empty queue
        with self.assertRaises(Exception):
            queue.dequeue()
    
    def test_mixed_operations(self):
        """Test mixed enqueue and dequeue operations"""
        queue = Queue(10)
        
        # Enqueue some elements
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue one element
        self.assertEqual(queue.dequeue(), 1)
        
        # Enqueue another
        queue.enqueue(4)
        
        # Dequeue remaining
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()