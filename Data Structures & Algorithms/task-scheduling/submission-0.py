class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq
        from collections import deque

        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        cooldown = deque()
        time = 0
        while heap or cooldown:
  
            if cooldown and cooldown[0][1] <= time:
                count, available_time = cooldown.popleft()
                heapq.heappush(heap, count)

            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count < 0:
                    cooldown.append((count, time + n + 1))


            time += 1
        return time
                

            