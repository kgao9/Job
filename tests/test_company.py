from job_cli.company import Company
from job_cli.file_obj import FileObj
import unittest
import mock

class TestVim(unittest.TestCase):
    def test_vim(self):
        myFile = FileObj('facebook.txt')
        name = "Facebook"
        link = 'https://www.facebook.com/pg/facebook/about/'
        business_type = 'huge company'
        found = 'GOOGLE TOLD ME'
       
        #create object
        facebook = Company(myFile, name, link, business_type, found)

        self.assertEqual(facebook.get_link(), link)
        self.assertEqual(facebook.get_business_type(), 'huge company')
        self.assertEqual(facebook.get_found(), 'GOOGLE TOLD ME')

if __name__ == '__main__':     
    unittest.main()
