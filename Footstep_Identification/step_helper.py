from collections import deque

def is_step(step_q_, threshV, min_count):
    step_q = step_q_.copy()
    count = 0
    while(not (len(step_q) == 0 )):
        #print(len(step_q))
        samp = step_q.popleft()
        if abs(samp) > threshV:
            count += 1
            if count > min_count:
                return True
    return False