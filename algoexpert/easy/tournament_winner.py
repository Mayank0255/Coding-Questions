def tournamentWinner(competitions, results):
	topScorer = ""
	scores = {topScorer: 0}
	length = len(results)

	for idx in range(length):
		homeTeam, awayTeam = competitions[idx]

		winningTeam = awayTeam if results[idx] == 0 else homeTeam

		updateScores(winningTeam, scores)

		if scores[winningTeam] > scores[topScorer]:
			topScorer = winningTeam

    return topScorer

def updateScores(team, scores):
	if team not in scores:
		scores[team] = 0
	scores[team] += 3
