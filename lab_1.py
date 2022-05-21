# A, B, C, D - number of created items

from ast import If
from ctypes import sizeof


uncontrollable_values = [
    [1000, 500, 2600, 4800],
    [10000, 6000, 4000, 5000],
    [4000, 6000, 400, 3200]
]



class solution:
    controlled_parameters = []

    def __init__(self):
        self.controlled_parameters = [0,0,0,0]

    def __init__(self, passed_parameters: list):
        self.controlled_parameters = [0,0,0,0]
        if(len(passed_parameters) != 4):
            print("ERROR creating probable_solution")
        for id in range(4):
            self.controlled_parameters[id] = passed_parameters[id]
    
    def show(self):
        print(F"X1: {self.controlled_parameters[0]}\tX2: {self.controlled_parameters[1]}\t X3: {self.controlled_parameters[2]}\t X4: {self.controlled_parameters[3]}")

    def count_profit(self):
        sum = 0
        for id in range(4):
            sum+= uncontrollable_values[0][id]-uncontrollable_values[2][id]
        return sum


def is_w2_passing(tested_solution: solution):

    id = 0
    w2 = 0
    for value in tested_solution.controlled_parameters:
        w2+=(uncontrollable_values[2][id] * value)
        id+=1
    return bool(w2 <= 1000000)

def is_w3_passing(tested_solution: solution):
    id = 0
    w2 = 0
    for value in tested_solution.controlled_parameters:
        w2+=(uncontrollable_values[0][id] * value)
        id+=1
    return bool(((w2/1800) <= 6000))

def find_parameter_bounds():
    max_bounds = [0, 0, 0, 0]
    for id in range(4):
        w2_max_bound = int(1000000/uncontrollable_values[2][id])
        w3_max_bound = int(6000*1800/uncontrollable_values[0][id])
        if(w2_max_bound < w3_max_bound):
            max_bounds[id] = w2_max_bound
        else:
            max_bounds[id] = w3_max_bound
    return solution(max_bounds)


def count_profit():

        

def main():
    all_possible_solutions = []
    max_bounds = find_parameter_bounds()
    max_bounds.show()
    for third_parameter_value in range(max_bounds.controlled_parameters[2]+1):
        for fourth_parameter_value in range(max_bounds.controlled_parameters[3]+1):
            tested_solution = solution([0, 0, third_parameter_value, fourth_parameter_value])
            if(not is_w2_passing(tested_solution)) or (not is_w3_passing(tested_solution)):
                break
            all_possible_solutions.append(tested_solution)
            tested_solution.show()
    print(F"there is a total of {len(all_possible_solutions)} possible solutions")
    max_profit = 0
    for possible_max_profit in all_possible_solutions:
        if (possible_max_profit.count_profit()):

main()
