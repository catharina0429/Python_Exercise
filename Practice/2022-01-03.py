## base class
class member:
    """인스턴스 메소드: self로 인스턴스 자기자신이 자동으로 전달"""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "Member: {0.name} (#{0.number})".format(self)

    def __repr__(self):
        return "Member: {0.name} (#{0.number})".format(self)

    def display(self):
        print(self)

joe = member('joe', 123)
jane = member('jane', 456)
print([joe, jane])

# sub-class
class officer(member):
    def __init__(self, name, number, rank ):
        member.__init__(self, name, number)
        self.rank = rank

    def __str__(self):
        return "{0.rank}: {0.name} (#{0.number})".format(self)

    def __repr__(self):
        return "officer('{0.name}', {0.number}, '{0.rank}')".format(self)

jack = officer('jack', 789, 'president')

members = [joe, jane, jack]
for m in members:
    m.display()
