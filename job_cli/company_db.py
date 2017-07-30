import pandas

from job_cli.config import DB_PATH
from job_cli.company import Company
from job_cli.file_obj import FileObj
from lockfile import LockFile
import os

from IPython import embed

class CompanyDB(object):
    """
        db object for companies
        Not an actual DB - just a csv file stored in hard disk
        constructor
            fname
    """

    def __init__(self, fname):
        self.fname = fname
        self.companyDF = self.read_file()

    def read_file(self):
        #read existing db
        if(os.path.isfile(os.path.join(DB_PATH, self.fname))):
            lock = LockFile(os.path.join(DB_PATH, self.fname))
            lock.acquire()         
            frame = pandas.read_csv(os.path.join(DB_PATH, self.fname), index_col=0)         
            lock.release()
            return frame

        else:
            #empty db
            df = pandas.DataFrame(columns=("filename", "link", "business_type", "found"))
            df.index.name = 'company_name'
            return df

    def write_file(self):
        #write back
        lock = LockFile(os.path.join(DB_PATH, self.fname))
        lock.acquire()
        self.companyDF.to_csv(os.path.join(DB_PATH, self.fname))
        lock.release()

    def getCompanies(self):
        """
            returns empty list for now - eventually we want it
            to return a list of company objects
        """
        companies = []
        for compName, row in self.companyDF.iterrows():
            fileObj = FileObj(row['filename'])
            myCompany = Company(fileObj, compName, row['link'], row['business_type'], row['found'])
            companies.append(myCompany)
        
        return companies

    def getDF(self):
        return self.read_file()

    def addCompany(self, company):
        assert(company not in self.getCompanies())

        embed()

        self.companyDF.loc[company.name] = [
                                               company.myFileObj.fname,
                                               company.link,
                                               company.business_type,
                                               company.found
                                           ]
        self.write_file()

    def removeCompany(self, companyName):
        del self.companyDF[companyName]

    def removeFile(self):
        os.remove(os.path.join(DB_PATH, self.fname))
