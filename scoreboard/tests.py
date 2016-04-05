# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime
from scoreboard import Result, Team


class TeamTestCase(TestCase):

    def setUp(self):
        self.team = Team()
        self.kwargs = {
            'team': '1',
            'problems': '2',
            'score': '10',
            'response': 'C',
        }

    def _create_team(self):
        return self.team.create(**self.kwargs)

    def test_check_problems_lower_value(self):
        team = self._create_team()
        kwargs = {
            'problems': '1'
        }
        problems = team.check_problems(**kwargs)

        self.assertEqual(problems, int(self.kwargs['problems']))

    def test_check_problems_highest_value(self):
        team = self._create_team()
        kwargs = {
            'problems': '4'
        }
        problems = team.check_problems(**kwargs)

        self.assertEqual(problems, int(kwargs['problems']))

    def test_check_score_response_correct(self):
        score = self.team.check_score_response(**self.kwargs)

        self.assertEqual(score, int(self.kwargs['score']))

    def test_check_score_response_incorrect(self):
        self.kwargs['response'] = 'I'
        score = self.team.check_score_response(**self.kwargs)

        self.assertEqual(score, 20)

    def test_check_score_response_request(self):
        self.kwargs['response'] = 'R'
        score = self.team.check_score_response(**self.kwargs)

        self.assertEqual(score, 0)

    def test_create(self):
        team = self._create_team()

        self.assertEqual(team.team, self.kwargs['team'])
        self.assertEqual(team.problems, int(self.kwargs['problems']))
        self.assertEqual(team.score, int(self.kwargs['score']))

    def test_update_response_correct(self):
        team = self._create_team()
        kwargs = {
            'problems': '3',
            'score': '10',
            'response': 'C',
        }
        team = team.update(**kwargs)

        self.assertEqual(team.team, self.kwargs['team'])
        self.assertEqual(team.problems, int(kwargs['problems']))

class ScoreBoard(TestCase):

    def setUp(self):
        self.pathfile = 'scoreboard/fixtures/test_file.txt'
        self.result = Result(**{'pathfile': self.pathfile})
        self.line_1 = ['1', '2', '10', 'I']
        self.line_2 = ['3', '1', '11', 'C']
        self.line_3 = ['1', '2', '19', 'R']
        self.line_4 = ['1', '2', '21', 'C']
        self.line_5 = ['1', '1', '25', 'C']
        self.line_6 = ['3', '1', '11', 'C']
        self.line_7 = ['1', '2', '66', 'C']

    def test_add_line_one_line(self):
        result = self.result.add_line(**{'line': self.line_1})

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[0].problems, 2)
        self.assertEqual(result[0].score, 20)

    def test_add_line_two_lines(self):
        result = self.result.add_line(**{'line': self.line_1})
        result = self.result.add_line(**{'line': self.line_2})

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[0].problems, 2)
        self.assertEqual(result[0].score, 20)
        self.assertEqual(result[1].team, '3')
        self.assertEqual(result[1].problems, 1)
        self.assertEqual(result[1].score, 11)

    def test_add_line_three_lines(self):
        result = self.result.add_line(**{'line': self.line_1})
        result = self.result.add_line(**{'line': self.line_2})
        result = self.result.add_line(**{'line': self.line_3})

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[0].problems, 2)
        self.assertEqual(result[0].score, 20)
        self.assertEqual(result[1].team, '3')
        self.assertEqual(result[1].problems, 1)
        self.assertEqual(result[1].score, 11)

    def test_add_line_four_lines(self):
        result = self.result.add_line(**{'line': self.line_1})
        result = self.result.add_line(**{'line': self.line_2})
        result = self.result.add_line(**{'line': self.line_3})
        result = self.result.add_line(**{'line': self.line_4})

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[0].problems, 2)
        self.assertEqual(result[0].score, 41)
        self.assertEqual(result[1].team, '3')
        self.assertEqual(result[1].problems, 1)
        self.assertEqual(result[1].score, 11)

    def test_add_line_five_lines(self):
        result = self.result.add_line(**{'line': self.line_1})
        result = self.result.add_line(**{'line': self.line_2})
        result = self.result.add_line(**{'line': self.line_3})
        result = self.result.add_line(**{'line': self.line_4})
        result = self.result.add_line(**{'line': self.line_5})

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[0].problems, 2)
        self.assertEqual(result[0].score, 66)
        self.assertEqual(result[1].team, '3')
        self.assertEqual(result[1].problems, 1)
        self.assertEqual(result[1].score, 11)

    def test_order_result_by_index(self):
        result = self.result.add_line(**{'line': self.line_6})
        result = self.result.add_line(**{'line': self.line_7})
        result = self.result._order_result_by_index(0)

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '3')

    def test_sort_result(self):
        result = self.result.add_line(**{'line': self.line_6})
        result = self.result.add_line(**{'line': self.line_7})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '3')

    def test_sort_result_tied_score_with_two_teams(self):
        result = self.result.add_line(**{'line': ['3', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['1', '2', '20', 'C']})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '3')

    def test_sort_result_tied_score_and_tied_problems_with_two_teams(self):
        result = self.result.add_line(**{'line': ['3', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['1', '1', '20', 'C']})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '3')

    def test_sort_result_tied_score_with_three_teams(self):
        result = self.result.add_line(**{'line': ['1', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['2', '2', '20', 'C']})
        result = self.result.add_line(**{'line': ['3', '3', '20', 'C']})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '3')
        self.assertEqual(result[1].team, '2')
        self.assertEqual(result[2].team, '1')

    def test_sort_result_tied_problems_with_three_teams(self):
        result = self.result.add_line(**{'line': ['1', '1', '19', 'C']})
        result = self.result.add_line(**{'line': ['2', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['3', '1', '21', 'C']})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '3')
        self.assertEqual(result[1].team, '2')
        self.assertEqual(result[2].team, '1')

    def test_sort_result_tied_score_and_tied_problems_with_three_teams(self):
        result = self.result.add_line(**{'line': ['1', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['2', '1', '20', 'C']})
        result = self.result.add_line(**{'line': ['3', '1', '20', 'C']})
        result = self.result.sort_result()

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '2')
        self.assertEqual(result[2].team, '3')

    def test_create(self):
        result = self.result.create()

        self.assertEqual(result[0].team, '1')
        self.assertEqual(result[1].team, '3')

    def test_create_raise_ioerror(self):
        def ioerror():
            pathfile = 'scoreboard/fixtures/test_file_incorrect.txt'
            result = Result(**{'pathfile': pathfile})
            result.create()

        self.assertRaises(IOError, ioerror)

    def test_create_file_result(self):
        self.result.create()
        filename = 'output_test_%s' % datetime.now().strftime('%Y%m%d')

        self.result.create_file(filename)
        fl = open('%s.txt' % filename, 'r').read()

        self.assertEqual(fl, '1 2 66\n3 1 11\n')
