def main():
    td = {46807866: 214117714021024}
    
    final = []
    for time,record in td.items():
        hold_distance = {}
        for hold_duration in range(1, time + 1):
            distance = hold_duration * (time - hold_duration)
            if distance > record: 
                hold_distance[hold_duration] = distance
        final.append(hold_distance)
    print(len(final[0]))
    
main()