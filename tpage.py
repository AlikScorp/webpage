
class TPage:

    cTitle = ''
    aContent = []
    aMeta = []
    aLink = []

    def __init__(self):
        self.set_meta("charset", 0, "utf-8")
        self.set_meta('name', "viewport", "width=device-width, initial-scale=1")

    def header(self):
        s = '<!DOCTYPE html><html lang="en">'
        return s

    def head(self):
        s = '<head>'+self.cTitle+self.get_meta()+self.get_link()+'</head>'
        return s

    def set_title(self, title):
        self.cTitle = '<title>'+title+'</title>'
        return 1

    def render(self):
        return self.header()+self.head()+self.get_body()+'</html>'

    def get_body(self):
        return '<body>'+self.get_content()+'</body>'

    def set_meta(self, type, name, value):
        if type == 'charset':
            self.aMeta.extend('<meta charset="{0}">'.format(value))
        elif type == 'name':
            self.aMeta.extend('<meta name="{0}" content="{1}">'.format(name, value))
        elif type == 'http-equiv':
            self.aMeta.extend('<meta http-equiv="{0}" content="{1}">'.format(name, value))

    def set_link(self, name, value):
        if name == 'stylesheet':
            self.aLink.extend('<link rel="{0}" href="{1}">'.format(name, value))

    def get_link(self):
        str=''
        for i in self.aLink:
            str=str+i

        return str

    def get_meta(self):
        str=''
        for i in self.aMeta:
            str = str+i

        return str

    def add_to_content(self, content):
        self.aContent.extend(content)

    def get_content(self):
        str = ''

        for i in self.aContent:
            str = str+i

        return str