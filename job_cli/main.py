import argparse
from job_cli.company_db import CompanyDB
from job_cli.company import Company
from job_cli.file_obj import FileObj

comp_db = CompanyDB('companyDB.csv')


def handleAdd(args):
    assert(args.company or args.job)

    if(args.company):
        myCompany = Company(FileObj(args.company_file[0]), args.company[0], args.home_page[0], args.business_type[0], args.found[0])

        print(args)

        comp_db.addCompany(myCompany)

    if(args.job):
        print('adding jobs not handled yet')

def handle_update(args):
    print('updating not handled yet')
 
def handle_search(args):
    print('searching not handled yet')

def handleArgs(args):
    assert(args.action in ['add', 'update', 'search'])
    
    if args.action == 'add':
        handleAdd(args)

    elif args.action == 'update':
        handle_update(args)

    else:
        handle_search(args)

parser = argparse.ArgumentParser(description='A CLI to keep track of job applications')

#arguments
parser.add_argument('action', help='action to  undertake; can only be one of add, update or search')
parser.add_argument('-company', '-c', nargs=1, help='company name')
parser.add_argument('-company_file', '-cf', nargs=1, help='company file path')
parser.add_argument('-home_page', '-hp', nargs=1, help='company home page')
parser.add_argument('-business_type', '-bt', nargs=1, help='company business type')
parser.add_argument('-found', '-f', nargs=1, help='how I found the company')
parser.add_argument('-job', '-j', nargs=1, help='job title')

args = parser.parse_args()

handleArgs(args)
