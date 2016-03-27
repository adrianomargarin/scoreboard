# -*- coding: utf-8 -*-

import sys
import re


class Team(object):

    def check_problems(self, **kwargs):
        problems = int(kwargs['problems'])
        return problems if problems > self.problems else self.problems

    def check_score_response(self, **kwargs):
        score = 0

        if kwargs['response'] == 'C':
            score = int(kwargs['score'])
        elif kwargs['response'] == 'I':
            score = 20

        return score

    def create(self, **kwargs):
        self.team = kwargs['team']
        self.problems = int(kwargs['problems'])
        self.score = self.check_score_response(**kwargs)

        return self

    def update(self, **kwargs):
        self.problems = self.check_problems(**kwargs)
        self.score += self.check_score_response(**kwargs)

        return self


class Result(object):

    def __init__(self, **kwargs):
        self.results = []
        self.pathfile = kwargs['pathfile']

    def create(self):
        try:
            with open(self.pathfile, 'r') as fl:
                lines = fl.readlines()
                lines.pop(0)
                lines = [re.sub('\n', '', line) for line in lines]

                for line in lines:
                    line = line.split(' ')
                    self.add_line(**{'line': line})

                return self.results
        except IOError, e:
            raise e

    def add_line(self, **kwargs):
        is_new = True
        line = {
            'team': kwargs['line'][0],
            'problems': kwargs['line'][1],
            'score': kwargs['line'][2],
            'response': kwargs['line'][3],
        }

        for result in self.results:
            if line['team'] == result.team:
                result.update(**line)
                is_new = False
                break

        if is_new:
            self.results.append(Team().create(**line))

        return self.results

    def _order_result_by_index(self, index):
        result_aux = self.results[index+1]
        self.results[index+1] = self.results[index]
        self.results[index] = result_aux

        return self.results

    def ordering_result_by_team(self):
        for index_a in range(0, len(self.results)):
            for index_b in range(0, len(self.results)-1):
                if self.results[index_b].team > self.results[index_b+1].team:
                    self.results = self._order_result_by_index(index_b)

        return self.results

    def ordering_result_by_score(self):
        for index_a in range(0, len(self.results)):
            for index_b in range(0, len(self.results)-1):
                if self.results[index_b].score < self.results[index_b+1].score:
                    self.results = self._order_result_by_index(index_b)

        return self.results

    def ordering_result_by_problems(self):
        for index_a in range(0, len(self.results)):
            for index_b in range(0, len(self.results)-1):
                if self.results[index_b].problems < self.results[index_b+1].problems:
                    self.results = self._order_result_by_index(index_b)

        return self.results

    def sort_result(self):
        self.ordering_result_by_team()
        self.ordering_result_by_score()
        self.ordering_result_by_problems()

        return self.results

    def create_file(self, filename='output'):
        result = self.sort_result()

        with open('%s.txt' % filename, 'w') as fl:
            for team in result:
                line = '%s %d %d\n' % (team.team, team.problems, team.score)
                fl.write(line)

if __name__ == '__main__':
    result = Result(**{'pathfile': sys.argv[1]})
    result.create()
    result.create_file()
