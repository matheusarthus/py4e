import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kargs):
        self.contents = []
        self.copyContents = []

        for key,value in kargs.items():
            for n in range(value):
                self.contents.append(key)
                self.copyContents.append(key)

    def draw(self, numberOfBalls):
        self.contents = copy.copy(self.copyContents)

        if numberOfBalls > len(self.contents):
            return self.contents

        chosenBalls = []
        
        for n in range(numberOfBalls):
            choice = random.choice(self.contents)

            self.contents.remove(choice)
            chosenBalls.append(choice)

        return chosenBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for n in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        auxM = 0

        for key, value in expected_balls.items():
            count = result.count(key)

            if count >= value:
                auxM += 1

        if auxM >= len(expected_balls):
            M += 1

    return M / num_experiments