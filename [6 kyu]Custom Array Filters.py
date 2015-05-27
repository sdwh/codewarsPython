class list(object):
    def __init__(self, arg):
        self.arg = [c for c in arg if isinstance(c,int)]
    def even(self):
        return [n for n in self.arg if n % 2 == 0]
    def odd(self):
        return [n for n in self.arg if n % 2 != 0]
    def under(self,num):
        return [n for n in self.arg if n < num]
    def over(self,num):
        return [n for n in self.arg if n > num]
    def in_range(self,min,max):
        return [n for n in self.arg if n >= min and n <= max]
