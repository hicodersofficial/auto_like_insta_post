from modules.Display import Display
class Config(Display):
    def __init__(self, args):
        self.pages = '2'
        self.internetTime = 5

        try:
            if '-lt' in args:
                self.internetTime = float(args[args.index('-lt') + 1])
        except Exception as e:
            super().exit("Invalid Arguments. -lt <loading time (sec)>")

        try:
            if '-sp' in args:
                self.pages = args[args.index('-sp') + 1]
        except Exception as e:
            super().exit("Invalid Arguments. -sp <scroll pages>")

        self.estTime = 0

    def estimated_time(self, stats_estimated_time):
        self.estTime = (int(self.pages) * 2) + self.internetTime + (self.internetTime * 1.5) + (self.internetTime * 1.3) + 1 + 2
        stats_estimated_time(self.estTime)