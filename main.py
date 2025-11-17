# notes version 0.1.0
import datetime
import time

command_table = {}

def run_command(command, values):
    match(command):
        case "print":
            print(values)

def check_time(hours, minutes):
    if not hours in command_table.keys():
        return False
    if not minutes in command_table[hours].keys():
        return False
    return True

if __name__ == "__main__":
    with open("data.txt", "r") as data_file:
        for line in data_file:
            splitted_line = line.split(":")
            if not splitted_line[0] in command_table.keys():
                command_table[splitted_line[0]] = {}
            if not splitted_line[1] in command_table[splitted_line[0]].keys():
                command_table[splitted_line[0]][splitted_line[1]] = []
            command_table[splitted_line[0]][splitted_line[1]].append({splitted_line[2]: splitted_line[3]})
    print(command_table)

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    with open("time.txt", "a") as time_file:
        time_file.write(current_time+"\n")
    splitted_time = current_time.split(":")
    if check_time(splitted_time[0],splitted_time[1]):
        print(command_table[splitted_time[0]][splitted_time[1]])
        for line in command_table[splitted_time[0]][splitted_time[1]]:
            print(line)
            for key, value in line.items():
                run_command(key, value)

    time.sleep(60)
