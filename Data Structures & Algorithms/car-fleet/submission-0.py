class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        for car in cars:
            time_to_reach_target = (target - car[0]) / car[1]
            print(f"time to reach target for car {car} is", time_to_reach_target)
            
            if len(car_fleet) == 0:
                car_fleet.append(time_to_reach_target)
            print(f"current bottleneck is", car_fleet[-1])
            if time_to_reach_target <= car_fleet[-1]:
                print("car is faster than previous car, absorbed into car fleet")
            elif time_to_reach_target > car_fleet[-1]:
                print("car is slower than the previous car, it now becomes the new bottleneck")
                car_fleet.append(time_to_reach_target)
        return len(car_fleet)