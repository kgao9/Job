from job_cli.vim import vim
import unittest
import mock

class TestVim(unittest.TestCase):
    @mock.patch('job_cli.vim.call')
    def test_vim(self, call):
        vim("basic_file.txt")

        assert call.called

if __name__ == '__main__':     
    unittest.main()
