from job_cli.file_obj import FileObj
from job_cli.description_object import DescriptionObject
import unittest
import mock

class TestVim(unittest.TestCase):
    def test_vim(self):
        myFile = FileObj('basic_file.txt')
        myObj = DescriptionObject(myFile, "testName")

        self.assertEqual("testName", myObj.get_name())

if __name__ == '__main__':     
    unittest.main()
