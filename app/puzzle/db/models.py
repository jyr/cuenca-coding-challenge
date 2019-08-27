from sqlalchemy import Column, String, Integer, Date, literal

try:
    from db.driver import Base, Session, engine
except ModuleNotFoundError:
    from puzzle.db.driver import Base, Session, engine

class SolutionModel:

    def __init__(self, **kwargs):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.size = kwargs['N']
        self.solution_number = kwargs['solution_number']
        self.positions = kwargs['positions']

    def exists(self):
        q = self.session.query(Solution).filter(
            Solution.size == self.size,
            Solution.number == self.solution_number,
            Solution.positions == self.positions
        )

        return self.session.query(literal(True)).filter(q.exists()).scalar()

    def save(self):
        if not self.exists():
            solution = Solution(self.size, self.solution_number, self.positions)
            self.session.add(solution)
            self.session.commit()

        self.session.close()

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    number = Column(Integer)
    positions = Column(String)

    def __init__(self, size, number, positions):
        self.size = size
        self.number = number
        self.positions = positions
