class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer = [0] * n

        for first, last, seats in bookings:
            # Start adding seats from this flight
            answer[first - 1] += seats

            # Stop adding seats after the last flight
            if last < n:
                answer[last] -= seats

        # Convert differences into actual seat counts
        for i in range(1, n):
            answer[i] += answer[i - 1]

        return answer
