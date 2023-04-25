import copy
import random

class Hat:

    def __init__(self,**kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num_balls_drawn):
        balls_drawn = list()
        if num_balls_drawn > len(self.contents):
            balls_drawn = self.contents.copy()
        else:
            balls_drawn = random.sample(self.contents, num_balls_drawn)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_not_found = False
        for key, value in expected_balls.items():
            if balls_drawn.count(key) >= value:
                continue
            else:
                balls_not_found = True
                break
        if balls_not_found == False:
            m += 1
    probability = m / num_experiments
    return probability

myhat = Hat(black=6, red=4, green=3)

print(experiment(hat= myhat, expected_balls = {"red":2,"green":1}, num_balls_drawn = 5, num_experiments = 3000))