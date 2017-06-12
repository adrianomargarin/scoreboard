# -*- coding: utf-8 -*-

import re
import sys


class ScoreBoard(object):
    """
    Class that aggregates all methods needed to generate the file with the result.
    """

    def __init__(self, pathfile):
        self.pathfile = pathfile

    def check_score_response(self, score, current_score, response):
        """
        Checks whether the answer is correct or incorrect by returning your score.
        """
        if response == 'C':
            score = int(score)
        elif response == 'I':
            score = 20
        else:
            score = 0

        score += int(current_score)

        return score

    def check_quantity_problems(self, current, new):
        """
        Checks quantity problems returning the highest value.
        """
        return new if new > current else current

    def check_team_in_result(self, team, result):
        """
        Checks if the team already has the result, if true returns the team,
        if false returns false.
        """
        for res in result:
            if team == res['team']:
                return res

        return False

    def team(self, team, problems, score, response):
        """
        Create dictionary with team information.
        """
        return {
            'team': team,
            'problems': problems,
            'score': self.check_score_response(score, 0, response)
        }

    def add_team(self, team_name, problems, score, response, result):
        """
        Adds a team to the result.
        """
        team = self.check_team_in_result(team_name, result)

        if team:
            team['score'] = self.check_score_response(score, team['score'], response)
            team['problems'] = self.check_quantity_problems(team['problems'], problems)
        else:
            result.append(self.team(team_name, problems, score, response))

        return result

    def sort_result(self, result):
        """
        Sorts the result.
        """
        result = sorted(result, key=lambda item: item['team'])
        result = sorted(result, key=lambda item: item['score'], reverse=True)
        result = sorted(result, key=lambda item: item['problems'], reverse=True)

        return result

    def create_file(self, result):
        """
        Create the file with the result already ordered.
        """
        with open('/tmp/output.txt', 'w') as fl:
            for res in result:
                line = '%s %s %d\n' % (res['team'], res['problems'], res['score'])
                fl.write(line)

    def create(self):
        """
        Main method of the program.
        """
        try:
            with open(self.pathfile, 'r') as fl:
                result = []
                lines = fl.readlines()
                lines.pop(0)
                lines = [re.sub('\n', '', line) for line in lines]

                for line in lines:
                    team, problems, score, response = line.split(' ')
                    result = self.add_team(team, problems, score, response, result)

                self.create_file(self.sort_result(result))
        except IOError as exc:
            raise exc


if __name__ == '__main__':
    ScoreBoard(sys.argv[1]).create()
