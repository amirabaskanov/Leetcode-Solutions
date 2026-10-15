'''
How much time have I spent, end-to-end?
About an hour brainstorming and coding + another hour reviewing after I couldn't solve it

What were the trickiest aspects? Where did you lose the most time?
Trying to get the O(1) solution for all 4. With my prior knowledge it would be either first 2 operations would be O(1) or the second 2 would be O(1), not all 4 of them

What are some lessons/insights I gained from this problem?
Using the floors approach and designing a doubly linked list to handle it. Realizing this is possible because every count increment by max 1 each time. Which allows us to do this.

What would I do differently if I had extra time? What’s remaining to improve?
I don't think extra time would have helped me figure out the doubly linked list approach on my own. Maybe if I got a hint that I HAVE to use a Doubly Linked List, I would maybe eventually arrive at this solution after numerous trial and errors, but figuring out the fundamental floors intuition needed here would probably need some genius level thinking - if the person does not have prior knowledge of this trick.

What did I do well?
Designing a regular dict solution with O(1), O(1), O(n), O(n). Realizing that it would be impossible to achieve O(1) by just using this. Thinking about using heaps. 

Eliminating heaps for the same reason that it is not possible to achieve all 4 O(1) operations using heaps either
Did you use any hints, if yes, what? (please do not give up and look up the hints quickly. if you do need to look up the hints, only use the ones given on the problem page one by one, and DON'T look at youtube videos or full solutions, until you try really hard)
I looked at the topics of this problem, which actually give away that you can use a Linked List and Doubly Linked List + Hash Table. But I didn't think much of it, cause there are always multiple ways to solve a problem. And I was not familiar with the bucket/floor intuition

How difficult was the problem (1 super trivial, 10 extremely difficult) (answer this question three times separately for a) implementing quickly b) finding the right approach c) overall)
a) Pretty lengthy to implement, not immediately intuitive so 8/10
b) Without prior knowledge: 9.5/10, with prior knowledge: 3/10
c) Overall about 7/10. If I practice it a little more, this could get much easier to 5/10

What's the time & space complexity?
Time: O(1) for all 4 operations
Space: O(k) where k is the number of keys
'''
class Node:
    # Using doubly linked list for buckets
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
    
    # Insert new node right after self and return it
    def insert_after(self, new_node):
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node
        return new_node
    
    # Unlink self from the list
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.head = Node(0) #dummy in the beginning
        self.tail = Node(0) #dummy at the end
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {} #key -> bucket it lives in

    def inc(self, key: str) -> None:
        curr = self.key_to_node.get(key)

        if curr is None:
            # new key -> goes to count 1
            target = self.head.next
            if target == self.tail or target.count > 1:
                target = self.head.insert_after(Node(1))
            target.keys.add(key)
            self.key_to_node[key] = target
        else:
            # existing key -> move to count + 1
            next_count = curr.count + 1
            target = curr.next
            if target == self.tail or target.count != next_count:
                target = curr.insert_after(Node(next_count))
            target.keys.add(key)
            self.key_to_node[key] = target

            curr.keys.remove(key)
            if not curr.keys:
                curr.remove()

    def dec(self, key: str) -> None: 
        curr = self.key_to_node.get(key)
        if curr is None:
            return

        curr.keys.remove(key)

        if curr.count == 1:
            #Count would hit 0 -> forget the key
            del self.key_to_node[key]
        else:
            # Move to count - 1
            prev_count = curr.count - 1
            target = curr.prev
            if target == self.head or target.count != prev_count:
                target = target.insert_after(Node(prev_count))
            target.keys.add(key)
            self.key_to_node[key] = target
        
        if not curr.keys:
            curr.remove()

    def getMaxKey(self) -> str:
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
