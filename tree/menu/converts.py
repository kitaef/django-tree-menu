class ListConverter:
    #  return any combination of '/folder1/folder2'
    regex = '.*\/*'

    def to_python(self, menu_url):
        return menu_url.split('/')
        

    def to_url(self, menu_url):
        return menu_url