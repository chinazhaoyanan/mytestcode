from sys import argv
script, time = argv


class SweetPotato():

    def __init__(self, cookedTime):
        self.cookedLevel = 0
        self.cookedStatus = "生的"
        self.cookedTime = int(cookedTime)
        self.condition = []

    def cook(self):

        self.cookedLevel += self.cookedTime

        if self.cookedLevel in range(0, 3):
            self.cookedStatus = "生的"
        elif self.cookedLevel in range(3, 5):
            self.cookedStatus = "半生不熟的"
        elif self.cookedLevel in range(5, 8):
            self.cookedStatus = "熟了"
        elif self.cookedLevel >= 8:
            self.cookedStatus = "焦了"

    def addCondition(self, addCondition):
        self.condition.append(addCondition)

    def __str__(self):
        msg = "烧烤时间为： " + str(self.cookedLevel)
        msg += "  地瓜状态为：" + self.cookedStatus
        msg += "加入佐料为："

        for i in self.condition:
            msg += i + "、"

        msg = msg.strip("、")
        return msg

digua = SweetPotato(time)
digua.cook()
digua.addCondition("酱油")
digua.addCondition("醋")
digua.addCondition("芝麻")

print(digua)
