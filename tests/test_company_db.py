from job_cli.company import Company
from job_cli.file_obj import FileObj
from job_cli.company_db import CompanyDB
import unittest
import mock
import os
import pandas as pd

def createCompany(fname, name, link, business_type, found):
    myFile = FileObj(fname)
    name = name
    link = link
    business_type = business_type
    found = found

    return Company(myFile, name, link, business_type, found)

class TestVim(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        f = open('facebook.txt', 'w')
        f.write('facebook is a social media platform to network with friends\n')
        f.write('This platform has been along for a long time and is popular\n')
        f.write('among teens and young people')
        f.close()
         
        #create object
        cls.comp1 = createCompany(
                                      'facebook.txt', 
                                      'Facebook',
                                      'https://www.facebook.com/pg/facebook/about',
                                      'huge company',
                                      'GOOGLE TOLD ME'
                                  )

        f = open('amazon.txt', 'w')
        f.write('Amazon is an online retail store and a tech/web servicing company.\n')
        f.write('It aims to make online sales as convenient and profitable as \n')
        f.write('possible and it provides web/tech solutions to startups much \n')
        f.write('like google.')
        f.close()

        cls.comp2 = createCompany(
                                     'amazon.txt',
                                     'Amazon',
                                     'https://www.amazon.com/p/feature/rzekmvyjojcp6uc',
                                     'huge company',
                                     'my retailer of choice'
                                 )

        cls.db = CompanyDB('CompanyDB_test.csv')

    def testAddComp(self):

        companyName = ['Facebook']

        dic = {
                  'filename': ['facebook.txt'],
                  'link': ['https://www.facebook.com/pg/facebook/about'],
                  'business_type': ['huge company'],
                  'found': ['GOOGLE TOLD ME']
              }
         
        cols = ["filename", "link", "business_type", "found"]

        df_expected = pd.DataFrame(dic)
        df_expected.index = companyName
        df_expected.index.name = 'company_name'
        df_expected = df_expected[cols] #reorder them

        companyName = ['Facebook', 'Amazon']

        dic = {
                   'filename': ['facebook.txt', 'amazon.txt'],
                   'link': [
                               'https://www.facebook.com/pg/facebook/about', 
                               'https://www.amazon.com/p/feature/rzekmvyjojcp6uc'
                           ],
                   'business_type': ['huge company', 'huge company'],
                   'found': ['GOOGLE TOLD ME', 'my retailer of choice']
               }
        

        df_expected2 = pd.DataFrame(dic)
        df_expected2.index = companyName
        df_expected2.index.name = 'company_name'
        df_expected2 = df_expected2[cols] #reorder them

        #add one company to empty file
        self.db.addCompany(self.comp1)
        self.assertTrue(self.db.getDF().equals(df_expected))
        
        #get existing file and add comapny
        self.db2 = CompanyDB('CompanyDB_test.csv')
        self.assertTrue(self.db.getDF().equals(df_expected))

        self.db2.addCompany(self.comp2)

        pd.util.testing.assert_frame_equal(df_expected2, self.db.getDF(), check_dtype=False)

        #adding a company twice should raise an error, yo
        self.assertRaises(AssertionError, self.db2.addCompany, self.comp1)

    def testRemoveComp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.db.removeFile()
        os.remove('facebook.txt')
        os.remove('amazon.txt')


if __name__ == '__main__':     
    unittest.main()
