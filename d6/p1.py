from functools import reduce

def main():
    td = {46:214,
          80:1177,
          78:1402,
          66:1024}

    final = []
    for time,record in td.items():
        hold_distance = {}
        for hold_duration in range(1, time + 1):
            distance = hold_duration * (time - hold_duration)
            if distance > record: 
                hold_distance[hold_duration] = distance
        final.append(len(hold_distance))
    print(reduce(lambda x, y: x*y, final))
    
main()