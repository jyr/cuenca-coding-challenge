from puzzle.nqueens import Play

class TestPlay:

    def test_counting_solutions(self):
        for N in range(8,15):
            puzzle = Play(N)
            puzzle.solve()

            assert puzzle.solution_number in [
                92,
                352,
                724,
                2680,
                14200,
                73712,
                365596,
                2279184
            ]
