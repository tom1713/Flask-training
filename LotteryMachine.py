import random

class LotteryMachines:
    def __init__(self, MaxAmountOfBalls):
        self.MaxAmountOfBalls = MaxAmountOfBalls

    def GetOneNumber(self):
        total_number = set()
        while len(total_number) < self.MaxAmountOfBalls:
            b = random.randint(1, self.MaxAmountOfBalls)
            total_number.add(b)
        return total_number

    def Shuffle(self):
        List_number = [i for i in Lottery_Machine.GetOneNumber()]
        Suffle_list = []
        for i in range(len(List_number)):
            Suffle_list.append(random.choice(List_number))
            List_number.remove(Suffle_list[i])
        return Suffle_list

Lottery_Machine = LotteryMachines(100000)
Lottery_Machine.GetOneNumber()
for value in Lottery_Machine.Shuffle():
    print (value)