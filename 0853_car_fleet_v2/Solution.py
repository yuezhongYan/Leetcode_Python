import math


class Solution(object):
    def __radix_sort(self, position, radix=10):
        """Implement radix sort

        :param position:
        :param radix:
        :return: Nothing but position array is sorted.
        """
        # Number of digits for each number.
        K = int(math.ceil(math.log(max(position) + 1, radix)))

        for i in range(1, K + 1):
            bucket = [[] for j in range(radix)]
            for val in position:
                # Obtain kth digit in a number from least significant digit to most
                # significant digit.
                bucket[val % (radix ** i) // (radix ** (i - 1))].append(val)

            del position[:]
            for each in bucket:
                # Merge buckets
                position.extend(each)

    def carFleet(self, target, position, speed):
        """Compute the number of car fleets that will arrive at the destination using Dictionary.
        N cars are going to the same destination along a one lane road. The destination is target miles
        away.

        Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i]
        miles towards the target along the road.

        A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to
        bumper at the same speed.

        The distance between these two cars is ignored - they are assumed to have the same position.

        A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that
        a single car is also a car fleet.

        If a car catches up to a car fleet right at the destination point, it will still be considered as
        one car fleet.

        Algorithm:
        A car is a (position, speed) which implies some arrival time (target - position) / speed. Bind
        (position, arrival time) with hash map. Sort the cars by position.

        If the car behind the lead car would arrive earlier, then this car forms a fleet with the lead
        car. Otherwise, the fleet is final as no car can catch up to it.

        If the lead fleet drives away, then count it and continue. Otherwise, merge the fleets and
        continue.

        Total time complexity is O(n * k), where n is the number of cars and k is the number of digits. The
        time complexity is dominated by sorting operation.

        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        position_size = len(position)
        car_fleet_count = 0

        if position_size == 0 or len(speed) == 0:
            return car_fleet_count

        position_speed_map = {}

        for i in range(position_size):
            position_speed_map[position[i]] = float(target - position[i]) / speed[i]

        self.__radix_sort(position)

        car_fleet_count = 1
        for i in range(position_size - 1, 0, -1):
            if position_speed_map.get(position[i - 1]) > \
                    position_speed_map.get(position[i]):
                car_fleet_count += 1
            else:
                position_speed_map[position[i - 1]] = position_speed_map.get(position[i])

        return car_fleet_count


solution = Solution()
print(solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))