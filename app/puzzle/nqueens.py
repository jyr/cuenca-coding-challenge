from sqlalchemy import literal

try:
    from db.models import SolutionModel
except ModuleNotFoundError:
    from puzzle.db.models import SolutionModel

import timeout_decorator

class Play:

    def __init__(self, N = 8, verbose = False, record = False):
        self.N = N
        self.activate_verbose = verbose
        self.activate_record = record
        self.queens_positions = [0 for c in range(N)]
        self.row_is_free = [True for r in range(N)]
        self.diagonal_asc = self.threatened_cells()
        self.diagonal_desc = self.threatened_cells()
        self.solution_number = 0

    def solve(self, column = 0):

        if self.N < 8: return print("N must be greater than eight")

        if column == self.N:
            self.solution_number += 1
            self.create_positions()
            self.record()
            self.verbose()
        else:
            for row in range(self.N):
                diagonal_down_index = column + row
                diagonal_up_index = column+(self.N-1)-row

                if (self.row_is_free[row] and
                    self.diagonal_desc[diagonal_down_index] and
                    self.diagonal_asc[ diagonal_up_index]):
                    self.queens_positions[column] = row

                    self.flag_toggle(
                        row=row,
                        ddi=diagonal_down_index,
                        dup=diagonal_up_index,
                        bool=False
                    )
                    self.solve(column+1)
                    self.flag_toggle(
                        row=row,
                        ddi=diagonal_down_index,
                        dup=diagonal_up_index,
                        bool=True
                    )

    def threatened_cells(self):
        return [True for i in range((self.N * 2) - 1)]

    def create_positions(self):
        self.positions = ''
        for row in range(self.N):
            position = self.queens_positions[row] + 1
            self.positions = "{} {}".format(self.positions, position)

    def flag_toggle(self, **kwargs):
        row = kwargs['row']
        diagonal_down_index = kwargs['ddi']
        diagonal_up_index = kwargs['dup']
        bool = kwargs['bool']

        self.row_is_free[row] = bool
        self.diagonal_desc[ diagonal_down_index ] = bool
        self.diagonal_asc[ diagonal_up_index ] = bool

    def record(self):
        if self.activate_record == True:
            SolutionModel(
                N=self.N,
                solution_number=self.solution_number,
                positions=self.positions).save()

    def verbose(self):
        if self.activate_verbose == True:
            print(self.solution_number, end = ": ")
            for row in range(self.N):
                print(
                    self.queens_positions[row] + 1 ,
                    end = " " if row<self.N-1 else "\n"
                )

@timeout_decorator.timeout(600)
def main():
    print("Start")

    N = int(input('Enter a queens number: [default=8]') or 8)
    verbose = input('Do you want to activate the verbose? [yes | default=no] ') or 'no'
    record = input('Do you want to save the solutions? [yes | default=no] ') or 'no'
    answers = {'yes': True, 'no': False}

    puzzle = Play(N = N, verbose = answers[verbose], record=answers[record])
    puzzle.solve()

    print("{} solutions".format(puzzle.solution_number))

if __name__ == '__main__':
    try:
        main()
    except timeout_decorator.timeout_decorator.TimeoutError:
       print("Timed Out - 10 MINUTES TO EXECUTE IT")
