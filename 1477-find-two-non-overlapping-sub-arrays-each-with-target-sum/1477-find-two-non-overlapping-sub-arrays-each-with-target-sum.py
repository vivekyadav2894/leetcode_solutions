class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        
        min_len = [INF] * n
        
        l = 0
        curr_sum = 0
        min_total_len = INF
        best_so_far = INF
        
        for r in range(n):
            curr_sum += arr[r]
            
            while curr_sum > target and l <= r:
                curr_sum -= arr[l]
                l += 1
            
            if curr_sum == target:
                curr_len = r - l + 1
                
                if l > 0 and min_len[l - 1] != INF:
                    min_total_len = min(min_total_len, curr_len + min_len[l - 1])
                
                best_so_far = min(best_so_far, curr_len)
            
            min_len[r] = best_so_far
            
        return min_total_len if min_total_len != INF else -1