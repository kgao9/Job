import sys, tempfile, os 
from subprocess import call   

class FileObj(object):
    """
        a file object contains a path as a link to
        the file - has a method to open that path using
        vim

        Note: we want to make sure the file is file locked so nothing
        is modifying it...
    """

    def __init__(self, fname):
        self.fname = fname

    def vim(self):
        #set shell editor to be vim
        editor = os.getenv('EDITOR', 'vi')

        #open up fname with vim
        call('%s %s' % (editor, self.fname), shell=True)
