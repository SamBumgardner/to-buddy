import challonge
import yaml

def write_checkin(tournament_id, player_info = dict()):
    print("Preparing to write to the checkin file...")
    # Retrieve participant list from challonge
    participants = challonge.participants.index(tournament_id)

    # Basic checkin dict setup if totally empty.
    if 'players' not in player_info.keys():
        player_info['players'] = dict()
    if 'summary' not in player_info.keys():
        player_info['summary'] = dict()

    # Add players to checkin from challonge
    for player in participants:
        player_info_key = player["name"]
        
        if (player_info_key not in player_info.keys()):
            player_info['players'][player_info_key] \
                = {'username': player['username'], 'display_name': player['display_name'],
                'checked_in': 0}

    # Remove players that are no longer listed in challonge
    challonge_players = set([participant['name'] for participant in participants])
    local_players = set(player_info['players'].keys())
    dropped_players = local_players.difference(challonge_players)
    [player_info['players'].pop(dropped_player) for dropped_player in dropped_players]
    print("Dropped:", dropped_players)

    # Update total player count
    player_info['summary']['player_count'] = len(participants)

    print("Writing to checkin file...")
    # Actually write to file
    with open('output/checkin.yml', 'w') as checkin:
        yaml.dump(player_info, checkin)
    

def refresh_checkin(tournament_id):
    print("loading previous checkin file...")
    players = None
    with open('output/checkin.yml', 'r') as checkin:
        players = yaml.safe_load(checkin)
    
    write_checkin(tournament_id, players)

def list_checkin():
    print("loading checkin file...")
    players = None
    with open('output/checkin.yml', 'r') as checkin:
        players = yaml.safe_load(checkin)['players']
    
    not_checked_in = list()
    for player in players:
        if players[player]['checked_in'] == 0:
            not_checked_in.append(players[player]['display_name'])
    
    with open('output/missing_checkin.txt', 'w') as out:
        print('\nThese players have still not checked in: ', file=out)
        for name in not_checked_in:
            print('\t@{}'.format(name), file=out)
        print()