from main import vim
import unittest

class TestVim(unittest.TestCase):
    def test_vim(self):
        vim("basic_file.txt")

    if __name__ == '__main__':     
        unittest.main()

