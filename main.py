import sys, tempfile, os 
from subprocess import call   

def vim(fname):
    #set shell editor to be vim
    editor = os.getenv('EDITOR', 'vi')

    #open up fname with vim 
    call('%s %s' % (editor, fname), shell=True)  
