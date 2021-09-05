from functools import partial
import challonge
import yaml

import config
import checkin
import round_start_announcements

def initial_setup():
    # initial setup
    challonge.set_credentials(config.CONFIG['challonge']['username'], \
        config.CONFIG['challonge']['api_key'])

def input_loop():
    tournament_id = config.CONFIG['challonge']['tournament_id']
    tasks = dict({
        "0": partial(checkin.write_checkin, tournament_id),
        "1": partial(checkin.refresh_checkin, tournament_id),
        "2": checkin.list_checkin,
        "3": round_start_announcements.write_round_announcement,
        "-1": exit
    })

    while True:
        next_task = input("""Enter a number to run a new task:
        [0] Check-in: NEW (overwrites pre-existing file)
        [1] Check-in: REFRESH (adds missing users)
        [2] Check-in: LIST (get all not-checked-in users for display)
        [3] Round Start: NEW (make announcement to copy-paste to discord)
        [-1] QUIT

    selection: """)

        if next_task in tasks.keys():
            tasks[next_task]()

if __name__ == '__main__':
    initial_setup()
    input_loop()
