# -*- coding: utf-8 -*-

import sys
import re

def check_scores_response(line):
    score = 0

    if line[3] == 'C':
        score = int(line[2])
    elif line[3] == 'I':
        score = 20

    return score

def add_score(line, results):
    score = check_scores_response(line)

    index = 0
    list_size = len(results)

    for result in results:
        if line[0] == result['participant']:
            result['score'] += score
            if line[1] > result['problems']:
                result['problems'] = line[1]
            break

        index += 1

    if index == list_size:
        results.append({
            'participant': line[0],
            'problems': line[1],
            'score': score,
        })

    return results

def _order_results_aux(results, index):
    result_aux = results[index+1]
    results[index+1] = results[index]
    results[index] = result_aux

    return results

def ordering_result_by_participant(results):
    for index_a in range(0, len(results)):
        for index_b in range(0, len(results)-1):
            if results[index_b]['participant'] > results[index_b+1]['participant']:
                results = _order_results_aux(results, index_b)

    return results

def ordering_result_by_score(results):
    for index_a in range(0, len(results)):
        for index_b in range(0, len(results)-1):
            if results[index_b]['score'] < results[index_b+1]['score']:
                results = _order_results_aux(results, index_b)

    return results

def ordering_result_by_problems(results):
    for index_a in range(0, len(results)):
        for index_b in range(0, len(results)-1):
            if results[index_b]['problems'] < results[index_b+1]['problems']:
                results = _order_results_aux(results, index_b)

    return results

def sort_results(results):
    results = ordering_result_by_participant(results)
    results = ordering_result_by_score(results)
    results = ordering_result_by_problems(results)

    return results

def create_file_result(results, filename='output'):
    results = sort_results(results)
    fl = open('%s.txt' % filename, 'w')

    for result in results:
        line = '%s %s %d\n' % (result['participant'], result['problems'],
            result['score'])
        fl.write(line)

    fl.close()

def main(pathfile):
    try:
        with open(pathfile, 'r') as fl:
            results = []
            lines = fl.readlines()
            lines.pop(0)
            lines = [re.sub('\n', '', line) for line in lines]

            for line in lines:
                line = line.split(' ')
                results = add_score(line, results)

            create_file_result(results)
    except IOError, e:
        raise e

if __name__ == '__main__':
    main(sys.argv[1])
