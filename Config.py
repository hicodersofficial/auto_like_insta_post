class Config:
    def __init__(self):
        self.userTime = input("What your average website loading time [second](optional): ")
        self.pages = input('Number of page to scroll [default=2](optional): ')
        self.estTime = 0

        if self.pages == "":
            self.pages = '2'

        if self.userTime != "" and self.pages != "":
            self.internetTime = float(self.userTime)
        else:
            self.internetTime = 5

    def estimated_time(self, stats_estimated_time):
        self.estTime = (int(self.pages) * 2) + self.internetTime + (self.internetTime * 1.5) + (self.internetTime * 1.3) + 1 + 2
        stats_estimated_time(self.estTime)