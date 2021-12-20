class Window:
    nbs = [-1, -1, -1]
    internal_count = 0

    def has_3_number(self):
        return True if self.internal_count > 2 else False

    def addNb(self, nb):
        self.nbs[self.internal_count] = nb
        self.internal_count += 1

    def getSum(self):
        return self.nbs[0] + self.nbs[1] + self.nbs[2]

    def resetNbs(self):
        self.nbs = [-1, -1 ,-1]

