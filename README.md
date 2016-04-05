[![Code Climate](https://codeclimate.com/github/adrianomargarin/scoreboard/badges/gpa.svg)](https://codeclimate.com/github/adrianomargarin/scoreboard)

# Contest Scoreboard

Want to compete in the ACM ICPC? Then you had better know how to keep score!
Contestants are ranked first by the number of problems solved (the more the better),
then by decreasing amounts of penalty time. If two or more contestans are tied in
both problems solved and penalty time, they are displayed in order of increasing team
numbers.

A problem is considered solved by a contestant if any of the submissions for that
problem was judged correct. Penalty time is computed as the number of minutes it
took until the first correct submission for a problem was received, plus 20 minutes for
each incorrect submission prior to the correct solution. Unsolved problems incur no
time penalties.

**Input**

The input begin with a single positive interger on a line by itself indicating the number
of case, each described as below. This line is followed by a blank line. There is also a
blank line between two consecutive inputs.
The input consists of a snapshot of the judging queue, containing entries from some
or all of contestants 1 through 100 solving problems 1 through 9. Each line of input
consists of three numbers and a letter in the format contestant problem time L, where
L can be C, I, R, U, or E. These stand for Correct, clarification Request,
Unjudged, and Erroneoues submission. The last three cases do not affect scorring.
The lines of input appear in the order in which the submission were received.

**Output**


The output for each test case will consist of a scoreboard, sorted by the criteria described
above. Each line of output will contain a contestant number, the number of problems
solved by the contestant and the total time penalty accumulated by the contestant.
Since not all contestant are actually participating, only display those contestant who
have made a submission.
The output of two consecutives cases will be separated by a blank line.

Sample Input
```shell
1
1 2 10 I
3 1 11 C
1 2 19 R
1 2 21 C
1 1 25 C
```
Sample Output
```shell
1 2 66
3 1 11
```

# Setup

```shell
git clone git@github.com:adrianomargarin/scoreboard.git
cd path/to/scoreboard
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

# Testes

```shell
cd path/to/scoreboard
source env/bin/activate
./run_tests.sh
```

# Usage

```shell
cd path/to/scoreboard
source env/bin/activate
python scoreboard/scoreboard.py "scoreboard/fixtures/test_file.txt"
```

**Results in**

```shell
cat output.txt
```
