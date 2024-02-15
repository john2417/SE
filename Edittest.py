from unittest.mock import patch
import unittest

import os
from Edit import Edit

class CustomTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.edit = Edit()
        pass
    
    def test_addgenre(self):
        user_input = [
            'novel'
        ]
        with patch('builtins.input', side_effect = user_input):
            self.edit.add_genre()
        print(self.edit.genres)
        assert self.edit.genres == ['novel']
    
    
if __name__ == '__main__':
    unittest.main