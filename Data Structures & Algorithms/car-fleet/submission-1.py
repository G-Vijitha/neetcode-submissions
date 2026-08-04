class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        # print("cars1: ", cars)
        for i in range(len(position)):
            # print("i, len(position), position[i], speed[i]: ",i, len(position), position[i], speed[i])
            time = (target - position[i]) / speed[i]
            # print("time :", time)
            # print("beforeCars: ", cars)
            cars.append((position[i], time))
            # print("fterCars: ", cars)
        # print("outCars: ", cars)
        cars.sort(reverse= True)
        # print("sortCars: ", cars)
        fleet = 0
        last_fleet_time = 0

        for position, time in cars:
            # print("position, time , last_fleet_time: ", position, time, last_fleet_time)
            if time > last_fleet_time:
                # print("fleet: ", fleet)
                fleet += 1
                # print("fleetout: ", fleet)
                # print("last_fleet_time: ", last_fleet_time)
                last_fleet_time = time
                # print("OUT last_fleet_time: ", last_fleet_time)
        return fleet
































        # for i in range(len(position)):
        #     cars.append((position[i], speed[i]))
        
        # cars.sort(reverse = True)

        # fleet = len(cars)

        # for i in range(len(cars)-1):
        #     front_pos = cars[i][0]
        #     front_speed = cars[i][1]
        #     back_pos = cars[i+1][0]
        #     back_speed = cars[i+1][1]

        #     if back_speed <= front_speed:
        #         continue
        #     distance = front_pos - back_pos
        #     relative_speed = back_speed - front_speed
        #     meeting_time = distance/relative_speed
        #     front_time = (target-front_pos)/front_speed

        #     if meeting_time <= front_time:
        #         fleet -=1
        # return fleet
        