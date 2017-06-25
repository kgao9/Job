from job_cli.file_obj import FileObj
import unittest
import mock

class TestVim(unittest.TestCase):
    @mock.patch('job_cli.file_obj.call')
    def test_vim(self, call):
        myFile = FileObj('basic_file.txt')
        myFile.vim()

        assert call.called

if __name__ == '__main__':     
    unittest.main()
