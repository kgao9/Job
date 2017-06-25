from job_cli.file_obj import FileObj

class DescriptionObject(object):
    """
        Just a name and a fileobj with object's description
    """

    def __init__(self, myFileObj, name):
         self.myFileObj = myFileObj
         self.name = name

    def read_file(self):
        self.myFileObj.vim()

    def get_name(self):
        return self.name
