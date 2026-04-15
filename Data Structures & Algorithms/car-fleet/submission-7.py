import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        cars = sorted(zip(position, speed), reverse=True)
        # turns_taken = (target - position) // speed
        print("Look at cars now", cars)
        car_fleet = []
        for i in range(len(cars)):
            turns_taken = (target - cars[i][0]) / cars[i][1]
            print("what is turns taken", turns_taken)
            if i == 0:
                car_fleet.append(turns_taken)
                continue
            if turns_taken > car_fleet[-1]:
                car_fleet.append(turns_taken)

        return len(car_fleet)
                
            
