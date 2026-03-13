class Solution:
  def carFleet(self, target: int, position: List[int), speed: List[int]) -> int:
    cars = []
    for i in range(len(position)):
      cars.append((position [i], speed [i]))
      fleets = []
    for i in sorted (cars) [::-1]:
      fleets.append((target1[0]) / 1[1])
      if len(fleets) >= 2 and fleets [-1] <= fleets [-2]:
        fleets.pop()
    return len(fleets)
