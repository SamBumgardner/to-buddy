import config

STREAM_MATCHUP_TEMPLATE = "@{0} vs @{1}\n"

ROUND_ANNOUNCEMENT_TEMPLATE = """
WINNERS BRACKET STREAMED MATCHES for round {0}:
{1}
Please join the Winner's Bracket stream room and wait for your turn to play the match (will ping in discord when it's time to start):
`{2}`

Remember:
All games use standard settings, play **best 2 out of 3 games** for each match until reaching top 4.

For the rest of us - 
All other players in winners' side can play their round {0} matches off-stream.

Losers' Bracket games should play as soon as they're ready UNTIL reaching top 8. Games can happen off-stream or in Catboy's LB stream lobby (`{3}`), see the tournament-rules thread for details on how you can get on-stream.  

Non-streamed matches should be played in the park `US West Coast #41`. 
""" #
def _get_current_round():
    return input('Please enter the current round #: ')

def _get_players_for_stream():
    streamed_matches_count = config.CONFIG['tournament']['stream_matches_per_round']
    print("Selecting {} matches to show on stream...".format(streamed_matches_count))

    streamed_matches = list()
    for i in range(streamed_matches_count):
        joined_names = input('Please enter both Discord usernames for stream match {}: '.format(i))
        streamed_matches.append(joined_names.split())
    
    return streamed_matches

def _get_round_announcement():
    round_num = _get_current_round()
    
    stream_matches = _get_players_for_stream()
    joined_matches = ''
    for match in stream_matches:
        joined_matches += STREAM_MATCHUP_TEMPLATE.format(match[0], match[1])

    wb_lobby_code = config.CONFIG['tournament']['wb_stream_lobby_code']
    lb_lobby_code = config.CONFIG['tournament']['lb_stream_lobby_code']
    
    return ROUND_ANNOUNCEMENT_TEMPLATE.format( \
        round_num, joined_matches, wb_lobby_code, lb_lobby_code)

def write_round_announcement():
    print(_get_round_announcement())