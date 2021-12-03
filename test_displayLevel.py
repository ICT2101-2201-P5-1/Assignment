import unittest
import CoolMotor
from Models.displayLevel import display, delete
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response,session


class TestDisplayLevel(unittest.TestCase):
    """
    White box testing code for code in displayLevel.py
    """
    def test_display(self):
        result = display()
        self.assertIsNotNone(result)

    def test_delete(self):
        result = delete(6)
        self.assertEqual(result, "Delete Successful")

if __name__ == '__main__':
    unittest.main()