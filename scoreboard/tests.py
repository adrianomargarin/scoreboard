# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime

import scoreboard

class ScoreBoard(TestCase):

    def test_check_scores_response_correct(self):
        score = scoreboard.check_scores_response(['1', '2', '5', 'C'])

        self.assertEqual(score, 5)

    def test_check_scores_response_incorrect(self):
        score = scoreboard.check_scores_response(['1', '2', '5', 'I'])

        self.assertEqual(score, 20)

    def test_check_scores_response_request(self):
        score = scoreboard.check_scores_response(['1', '2', '5', 'R'])

        self.assertEqual(score, 0)

    def test_add_score_one_line(self):
        results = []
        results = scoreboard.add_score(['1', '2', '5', 'C'], results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 5}])

    def test_add_score_two_lines(self):
        results = []
        results = scoreboard.add_score(['1', '2', '5', 'C'], results)
        results = scoreboard.add_score(['2', '2', '10', 'I'], results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 5},
            {'participant': '2', 'problems': '2', 'score': 20}])

    def test_add_score_three_lines(self):
        results = []
        results = scoreboard.add_score(['1', '2', '5', 'C'], results)
        results = scoreboard.add_score(['2', '2', '10', 'I'], results)
        results = scoreboard.add_score(['1', '2', '10', 'R'], results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 5},
            {'participant': '2', 'problems': '2', 'score': 20}])

    def test_add_score_four_lines(self):
        results = []
        results = scoreboard.add_score(['1', '2', '5', 'C'], results)
        results = scoreboard.add_score(['2', '2', '10', 'I'], results)
        results = scoreboard.add_score(['1', '2', '10', 'R'], results)
        results = scoreboard.add_score(['1', '2', '10', 'C'], results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 15},
            {'participant': '2', 'problems': '2', 'score': 20}])

    def test_add_score_five_lines(self):
        results = []
        results = scoreboard.add_score(['1', '1', '10', 'I'], results)
        results = scoreboard.add_score(['2', '1', '11', 'C'], results)
        results = scoreboard.add_score(['1', '2', '19', 'R'], results)
        results = scoreboard.add_score(['1', '2', '21', 'C'], results)
        results = scoreboard.add_score(['1', '1', '25', 'C'], results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_order_results_aux(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}
        ]

        results = scoreboard._order_results_aux(results, 0)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_ordering_result_by_participant(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}
        ]

        results = scoreboard.ordering_result_by_participant(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_ordering_result_by_score(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}
        ]

        results = scoreboard.ordering_result_by_score(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_ordering_result_by_problems(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}
        ]

        results = scoreboard.ordering_result_by_problems(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_order_results_1(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}
        ]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 66},
            {'participant': '2', 'problems': '1', 'score': 11}])

    def test_order_results_2(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '2', 'score': 20}
        ]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20}])

    def test_order_results_3(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '3', 'score': 20},
            {'participant': '1', 'problems': '2', 'score': 20}
        ]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '3', 'problems': '3', 'score': 20},
            {'participant': '1', 'problems': '2', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20}])

    def test_order_results_tied_1(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20}])

    def test_order_results_tied_2(self):
        results = [
            {'participant': '3', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_3(self):
        results = [
            {'participant': '3', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_4(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_5(self):
        results = [
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_6(self):
        results = [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_7(self):
        results = [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 20},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_8(self):
        results = [
            {'participant': '3', 'problems': '1', 'score': 30},
            {'participant': '2', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '2', 'score': 20}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '2', 'score': 20},
            {'participant': '3', 'problems': '1', 'score': 30},
            {'participant': '2', 'problems': '1', 'score': 20}])

    def test_order_results_tied_9(self):
        results = [
            {'participant': '2', 'problems': '3', 'score': 10},
            {'participant': '3', 'problems': '1', 'score': 20},
            {'participant': '1', 'problems': '2', 'score': 30}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '2', 'problems': '3', 'score': 10},
            {'participant': '1', 'problems': '2', 'score': 30},
            {'participant': '3', 'problems': '1', 'score': 20}])

    def test_order_results_tied_10(self):
        results = [
            {'participant': '3', 'problems': '1', 'score': 10},
            {'participant': '2', 'problems': '1', 'score': 10},
            {'participant': '1', 'problems': '1', 'score': 10}]
        results = scoreboard.sort_results(results)

        self.assertEqual(results, [
            {'participant': '1', 'problems': '1', 'score': 10},
            {'participant': '2', 'problems': '1', 'score': 10},
            {'participant': '3', 'problems': '1', 'score': 10}])

    def test_create_file_result(self):
        results = [
            {'participant': '3', 'problems': '1', 'score': 11},
            {'participant': '1', 'problems': '2', 'score': 66}]

        filename = 'output_test_%s' % datetime.now().strftime('%Y%m%d')

        scoreboard.create_file_result(results, filename)
        fl = open('%s.txt' % filename, 'r').read()

        self.assertEqual(fl, '1 2 66\n3 1 11\n')

    def test_main(self):
        scoreboard.main('scoreboard/fixtures/test_file.txt')

        fl = open('output.txt', 'r').read()
        self.assertEqual(fl, '1 2 66\n3 1 11\n')

    def test_main_ioerror(self):
        def ioerror():
            scoreboard.main('scoreboard/fixtures/test_file_incorrect.txt')

        self.assertRaises(IOError, ioerror)
