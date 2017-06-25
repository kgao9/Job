from job_cli.description_object import DescriptionObject

class Company(DescriptionObject):
    def __init__(self, fileObj, name, link, business_type):
        DescriptionObject.__init__(self, fileObj, name)
        self.link = link
        self.business_type = business_type

    def get_link(self):
        return self.link

    def get_business_type(self):
        return self.business_type
