from random import randrange


class Solution(object):
    def __quick_sort(self, position, start, end):
        """Implement quick sort

        :param position: list[int]
        :param start: int
        :param end: int
        :return: Nothing but position array is sorted.
        """
        if start >= end:
            return

        pivot_index = randrange(end - start + 1) + start
        pivot = position[pivot_index]

        # Swap position[pivot_index] with position[start]. Now pivot is on the left
        position[pivot_index], position[start] = position[start], position[pivot_index]

        left = start + 1
        right = end

        # Partition
        while left <= right:
            while left <= right and position[left] <= pivot:
                left += 1

            while left <= right and position[right] > pivot:
                right -= 1

            if left < right:
                # Swap position[left] with position[right]
                position[left], position[right] = position[right], position[left]

                left += 1
                right -= 1

        # Swap position[start] with position[right]. Now pivot is at position[right].
        position[start], position[right] = position[right], position[start]

        self.__quick_sort(position, start, right - 1)
        self.__quick_sort(position, right + 1, end)

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

        Total time complexity is O(n log n) in average case and O(n^2) in the worst case, where n is the
        number of cars. The time complexity is dominated by sorting operation. The worst case happens if
        the pivot index is always picked at both ends.

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

        self.__quick_sort(position, 0, position_size - 1)

        car_fleet_count = 1
        for i in range(position_size - 1, 0, -1):
            # If the car with initial position i - 1 arrives sooner, it cannot be caught. Else, the car with
            # initial position i - 1 arrives at the same speed as the car with initial position i.
            if position_speed_map.get(position[i - 1]) > \
                    position_speed_map.get(position[i]):
                car_fleet_count += 1
            else:
                position_speed_map[position[i - 1]] = position_speed_map.get(position[i])

        return car_fleet_count


solution = Solution()
print(solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
