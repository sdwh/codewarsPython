class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return self.draft - 1.5 * self.crew >= 20

boat = Ship(21,0)
print(boat.is_worth_it())
