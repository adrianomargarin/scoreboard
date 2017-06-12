# -*- coding: utf-8 -*-

from unittest import TestCase

from scoreboard import ScoreBoard


class ScoreBoardTestCase(TestCase):

    def setUp(self):
        self.pathfile = 'scoreboard/fixtures/test_file.txt'
        self.scoreboard = ScoreBoard(self.pathfile)

    def test_check_score_response_C(self):
        self.assertEqual(self.scoreboard.check_score_response('25', '21', 'C'), 46)

    def test_check_score_response_I(self):
        self.assertEqual(self.scoreboard.check_score_response('19', '46', 'I'), 66)

    def test_check_score_response_R(self):
        self.assertEqual(self.scoreboard.check_score_response('19', '11', 'R'), 11)

    def test_check_quantity_problems_one(self):
        self.assertEqual(self.scoreboard.check_quantity_problems(1, 1), 1)

    def test_check_quantity_problems_two(self):
        self.assertEqual(self.scoreboard.check_quantity_problems(1, 2), 2)

    def test_check_team_in_result_true(self):
        team = {
            'team': '1',
            'score': '66',
            'problems': '2',
        }
        self.assertTrue(self.scoreboard.check_team_in_result('1', [team]), team)

    def test_check_team_in_result_false(self):
        self.assertFalse(self.scoreboard.check_team_in_result('1', []), False)

    def test_team(self):
        expect_result = {
            'team': '1',
            'problems': 2,
            'score': 66
        }

        self.assertDictEqual(self.scoreboard.team('1', 2, 66, 'C'), expect_result)

    def test_add_team(self):
        result = []

        result = self.scoreboard.add_team('1', '2', '10', 'I', result)
        result = self.scoreboard.add_team('3', '1', '11', 'C', result)
        result = self.scoreboard.add_team('1', '2', '19', 'R', result)
        result = self.scoreboard.add_team('1', '2', '21', 'C', result)
        result = self.scoreboard.add_team('1', '1', '25', 'C', result)

        expect_result = [
            {
                'team': '1',
                'problems': '2',
                'score': 66
            }, {
                'team': '3',
                'problems': '1',
                'score': 11
            }
        ]

        self.assertListEqual(result, expect_result)

    def test_sort_result(self):
        result = [{
                'team': '3',
                'problems': '1',
                'score': 11
            }, {
                'team': '1',
                'problems': '2',
                'score': 66
            }
        ]

        sorted_result = self.scoreboard.sort_result(result)

        self.assertEqual(sorted_result[0]['team'], '1')
        self.assertEqual(sorted_result[1]['team'], '3')

    def test_create_file(self):
        result = [
            {
                'team': '1',
                'problems': '2',
                'score': 66
            }, {
                'team': '3',
                'problems': '1',
                'score': 11
            }
        ]

        self.scoreboard.create_file(result)

        with open('/tmp/output.txt', 'r') as output:
            self.assertEqual(output.read(), '1 2 66\n3 1 11\n')

    def test_result(self):
        self.scoreboard.create()

        with open('/tmp/output.txt', 'r') as output:
            self.assertEqual(output.read(), '1 2 66\n3 1 11\n')

    def test_create_raise_ioerror(self):
        def ioerror():
            scoreboard = ScoreBoard('scoreboard/fixtures/test_file_incorrect.txt')
            scoreboard.create()

        self.assertRaises(IOError, ioerror)
