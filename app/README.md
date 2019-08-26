# Cuenca - coding challenge


### Description

Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

These are the different aspect of the project you can work on (in order):
1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
2. iterate over N and store the solutions in postgres using SQLAlchemy
3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.

Please commit everything in a public GitHub repo and use python3.

You can borrow from an existing solution—except for Google's. If you borrow from someone else's code, please cite where you got the code and be ready to explain how the code works.

## Basis Usage

**Run the puzzle.**

```docker-compose exec app /bin/sh -c -l "python puzzle/nqueens.py"```
