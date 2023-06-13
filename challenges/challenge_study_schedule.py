def study_schedule(permanence_period, target_time):
    # permanence_period = tuplas repesentando tempo de permanencia [(2,4)...]
    x = 0
    if target_time is None:
        return None
        # for number in target_time:
    for time_in in permanence_period:
        if not isinstance(time_in[0], int) or not isinstance(time_in[1], int):
            return None
        if target_time >= time_in[0] and target_time <= time_in[1]:
            x += 1
    return x
