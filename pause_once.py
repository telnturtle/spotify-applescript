import time
import datetime
import os
import sys


# aux

def cur_isostring() -> str:
    return datetime.datetime.now().isoformat()[:19]


def run_if_the_time(hour: int, minute: int):
    current_time = datetime.datetime.now()
    cur_hour, cur_minute = current_time.hour, current_time.minute

    if (cur_hour, cur_minute) == (hour, minute):
        ret = os.system('osascript ~/git/spotify-applescript/pauseVivaldi.scpt')
        return (True, ret)
    else:
        return (False, 0)


if __name__ == '__main__':
    print(f'{cur_isostring()} : Run after 2 seconds...')
    time.sleep(2)

    goal_hour, goal_minute = 0, 0
    if len(sys.argv) < 3 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
        print(f'{cur_isostring()} : Less than 3 argv.')
        exit()
    else:
        goal_hour, goal_minute = int(sys.argv[1]), int(sys.argv[2])

    touched_day = 0
    touched_day_log = 0
    while True:
        current_day = datetime.datetime.now().day
        if touched_day != current_day:
            executed, ret = run_if_the_time(goal_hour, goal_minute)
            if executed:
                print(f'{cur_isostring()} : {ret}')
                touched_day = current_day
                break
            elif touched_day_log != current_day:
                print(f'{cur_isostring()} : Not this time')
            touched_day_log = current_day
        time.sleep(30)
