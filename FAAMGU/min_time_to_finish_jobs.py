  
def findMinTime(jobs, k):    
    n = len(jobs)
    start = 0
    end = sum(jobs)
    ans = end
    jobs = sorted(jobs)

    def isPossible(time, k): 
        cnt = 1
        curr_time = 0 

        i = 0
        while i < n: 
            if curr_time + jobs[i] > time:  
                curr_time = 0
                cnt += 1
            else: 
                curr_time += jobs[i]  
                i += 1

        return cnt <= k
  
    # Find the job that takes maximum time  
    job_max = max(jobs)
  
    # Do binary search for minimum feasible time  
    while start <= end:  
        mid = (start + end) // 2  
  
        if mid >= job_max and isPossible(mid, k): 
            ans = min(ans, mid) 
            end = mid - 1
        else: 
            start = mid + 1
  
    return ans


jobs = [10, 7, 8, 12, 6, 8]
k = 4
print(findMinTime(jobs, k))



def swapNodes(head, k):
    first, last_k, first_k = head, None, None
    count = 1
    while first:
        if count == k:
            if not first_k:
                first_k = first

            if not last_k:
                last_k = head
            else:
                last_k = last_k.next

            first = first.next
        else:
            count += 1
            first = first.next
    
    first_k.val, last_k.val = last_k.val, first_k.val
    return head