# Insert, max, min , mean, mode

class TempTracker:

    def __init__(self):
        self.max = float('-inf')
        self.min = float('inf')
        self.sum = 0
        self.count = 0
        self.mode = None
        self.mean = None
        self.temperatures = [0] * 111

    def show_list(self):
        print "%s" % self.temperatures

    def insert(self, x):
        if x < 0 or x > 110:
            raise Exception("Out of temperature range!")
        if self.max < x:
            self.max = x
        if self.min > x:
            self.min = x
        self.sum += x
        self.count += 1
        self.mean = self.sum/self.count
        self.temperatures[x] += 1
        if self.mode != x:
            if self.temperatures[x] > self.temperatures[self.mode]:
                self.mode = x

    def get_max(self):
        print self.max

    def get_min(self):
        print self.min

    def get_mean(self):
        print self.mean

    def get_mode(self):
        print self.mode

temp_tracker = TempTracker()
while(1):
    print ("""\n1. insert \n
2. min \n
3. max \n
4. mean \n
5. mode \n
6. show list\n
7. exit \n\n
           """)
    choice = input("Enter Choice: ")
    if choice is 1:
        x = input("Enter number to be inserted: ")
        assert x > 0 and x <= 110
        temp_tracker.insert(x)
    elif choice is 7:
        exit(0)
    else:
        switcher = {
        2: temp_tracker.get_min,
        3: temp_tracker.get_max,
        4: temp_tracker.get_mean,
        5: temp_tracker.get_mode,
        6: temp_tracker.show_list
        }
        switcher.get(choice)()
