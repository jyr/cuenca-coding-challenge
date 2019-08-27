from sqlalchemy import literal

try:
    from db.models import SolutionModel
except ModuleNotFoundError:
    from puzzle.db.models import SolutionModel

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

                    self.row_is_free[row] = False
                    self.diagonal_desc[ diagonal_down_index ] = False
                    self.diagonal_asc[ diagonal_up_index ] = False

                    self.solve(column+1)

                    self.row_is_free[row] = True
                    self.diagonal_desc[ diagonal_down_index ] = True
                    self.diagonal_asc[ diagonal_up_index ] = True

    def threatened_cells(self):
        return [True for i in range((self.N * 2) - 1)]

    def create_positions(self):
        self.positions = ''
        for row in range(self.N):
            position = self.queens_positions[row] + 1
            self.positions = "{} {}".format(self.positions, position)

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

def main():
    puzzle = Play(N = 8, verbose = True, record=True)
    puzzle.solve()
    print("{} solutions".format(puzzle.solution_number))

if __name__ == '__main__':
    main()
