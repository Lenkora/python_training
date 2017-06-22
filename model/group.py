from sys import maxsize

class Group:
    def __init__(self,name = None,header = None,footer = None, id = None, text = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id =id
#строковое зпредставление, а не вот такое: 0x02BDAD50
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header,self.footer)

#сравнение по смыслу, а не по физическому расположению
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize