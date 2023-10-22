from collections import queue

def is_step(step_q, threshV, min_count):
    count = 0
    while(not step_q.empty()):
        samp = step_q.pop()
        if abs(samp) > threshV:
            ++count
            if count > min_count:
                return True
    return False