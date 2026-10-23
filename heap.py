class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    def push(self, val: int) -> None:
        """Insert a value and bubble it up to maintain heap order: O(log n)."""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Extract and return the smallest element: O(log n)."""
        if not self.heap:
            raise IndexError("pop from empty heap")

        # Swap root with the last leaf
        root = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)

        return root

    def peek(self) -> int:
        """Return the minimum element without removing it: O(1)."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _sift_up(self, index: int) -> None:
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def _sift_down(self, index: int) -> None:
        size = len(self.heap)
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def __len__(self) -> int:
        return len(self.heap)

    def __str__(self) -> str:
        return str(self.heap)


# Example usage:
if __name__ == "__main__":
    h = MinHeap()
    for num in [15, 10, 20, 8, 12]:
        h.push(num)

    print("Current Heap:", h)         # Minimum element sits at index 0
    print("Peek min:", h.peek())       # 8
    print("Popped:", h.pop())          # 8
    print("Heap after pop:", h)
