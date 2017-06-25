from job_cli.description_object import DescriptionObject

class Company(DescriptionObject):
    def __init__(self, fileObj, name, link, business_type, found):
        DescriptionObject.__init__(self, fileObj, name)
        self.link = link
        self.business_type = business_type

        #how I heard about said company
        #should technically be in description object
        #but then I'd need to think of a better name than description
        #object and I just can't... I SUCK :'(
        self.found = found

    def get_link(self):
        return self.link

    def get_business_type(self):
        return self.business_type

    def get_found(self):
        return self.found
