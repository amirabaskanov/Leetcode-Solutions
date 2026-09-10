class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.priority = {}

        for eventId, priority in events:
            self.priority[eventId] = priority
            self.heap.append((-priority, eventId))

        heapq.heapify(self.heap)

        # O(n)
        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priority[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

        # O(log n)

    def pollHighest(self) -> int:
        while self.heap:
            negPriority, eventId = heapq.heappop(self.heap)
            priority = -negPriority

            if (
                eventId in self.priority
                and self.priority[eventId] == priority
            ):
                del self.priority[eventId]
                return eventId
        return -1
        # O(log n)

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
