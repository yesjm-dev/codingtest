def solution(players, callings):
    players_dict = {player: i for i, player in enumerate(players)}
    for i in callings:
        rank = players_dict[i]
        players_dict[i] -= 1
        players_dict[players[rank-1]] += 1
        players[rank], players[rank-1] = players[rank-1], players[rank]
    return players