"""Testing my double linked list"""
import unittest
from .double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    """Test class for my double linked list"""

    def test_push(self):
        """Test pushing elements in the end"""
        push_test_list = DoubleLinkedList()
        push_test_list.push(12)
        self.assertEqual(push_test_list.get_list()[0].get_elem(), 12)

    def test_pop_empty_list(self):
        """Test delete last element when list is empty"""
        test_list = DoubleLinkedList()
        with self.assertRaises(Exception) as context:
            test_list.pop()
        self.assertTrue('Empty list' in str(context.exception))

    def test_pop(self):
        """Test delete last element"""
        test_list = DoubleLinkedList()
        test_list.push(15)
        test_list.push(150)
        test_list.push(13)
        test_list.push(155)
        test_list.push(1)
        test_list.pop()
        self.assertEqual(test_list.last().get_elem(), 155)

    def test_un_shift(self):
        """Test add element in the top of the list"""
        l_list = DoubleLinkedList()
        l_list.push(15)
        l_list.push(150)
        l_list.push(1)
        l_list.un_shift(111)
        self.assertEqual(l_list.get_list()[0].get_elem(), 111)

    def test_un_shift_when_empty(self):
        """Test add element in the top of the list, when list is empty"""
        l_list = DoubleLinkedList()
        l_list.un_shift(111)
        self.assertEqual(l_list.get_list()[0].get_elem(), 111)

    def test_shift(self):
        """Test delete element in the top of the list"""
        shift_test_list = DoubleLinkedList()
        shift_test_list.push(15)
        shift_test_list.push(154)
        shift_test_list.push(1435)
        shift_test_list.shift()
        self.assertEqual(shift_test_list.get_list()[0].get_elem(), 154)

    def test_shift_when_empty(self):
        """Test delete element in the top of the list, when list is empty"""
        l_list = DoubleLinkedList()
        with self.assertRaises(Exception) as context:
            l_list.shift()
        self.assertTrue('Empty list' in str(context.exception))

    def test_len(self):
        """Test method which return count of elements in list"""
        l_list = DoubleLinkedList()
        l_list.push(12)
        l_list.push(123)
        l_list.push(1234)
        l_list.push(1234)
        l_list.pop()
        l_list.pop()
        self.assertEqual(l_list.len(), 2)

    def test_len_when_empty(self):
        """Test method which return count of elements in list, when list is empty"""
        l_list = DoubleLinkedList()
        self.assertEqual(l_list.len(), 0)

    def test_delete(self):
        """Test method which delete element from list"""
        delete_test_list = DoubleLinkedList()
        delete_test_list.push(12)
        delete_test_list.push(123)
        delete_test_list.push(1234)
        delete_test_list.push(12345)
        delete_test_list.delete(123)
        self.assertEqual(delete_test_list.get_list()[1].get_elem(), 1234)

    def test_delete_when_empty(self):
        """Test method which delete element from list, when list is empty"""
        l_list = DoubleLinkedList()
        with self.assertRaises(Exception) as context:
            l_list.delete(123)
        self.assertTrue('Empty list' in str(context.exception))

    def test_delete_when_no_this_element(self):
        """Test method which delete element from list, when no this element in the list"""
        l_list = DoubleLinkedList()
        l_list.push(1234)
        l_list.push(12)
        l_list.push(1)
        with self.assertRaises(Exception) as context:
            l_list.delete(123)
        self.assertTrue('No this Element' in str(context.exception))

    def test_contains(self):
        """Test method which check if element contains in list"""
        l_list = DoubleLinkedList()
        l_list.push(1234)
        l_list.push(12)
        l_list.push(1)
        self.assertTrue(l_list.contains(12))
        self.assertFalse(l_list.contains(2345))

    def test_first(self):
        """Test return first Item in list"""
        l_list = DoubleLinkedList()
        l_list.push(1234)
        l_list.push(12)
        self.assertEqual(l_list.get_list()[0], l_list.first())

    def test_first_when_empty(self):
        """Test return first Item in list, when list is empty"""
        l_list = DoubleLinkedList()
        with self.assertRaises(Exception) as context:
            l_list.first()
        self.assertTrue('Empty list' in str(context.exception))

    def test_last(self):
        """Test return last Item in list"""
        l_list = DoubleLinkedList()
        l_list.push(1234)
        l_list.push(12)
        self.assertEqual(l_list.get_list()[-1], l_list.last())

    def test_last_when_empty(self):
        """Test return last Item in list, when list is empty"""
        l_list = DoubleLinkedList()
        with self.assertRaises(Exception) as context:
            l_list.last()
        self.assertTrue('Empty list' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
