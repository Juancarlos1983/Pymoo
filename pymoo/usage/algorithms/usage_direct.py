from pymoo.algorithms.so_direct import DIRECT
from pymoo.optimize import minimize
from pymoo.problems.single import Himmelblau

problem = Himmelblau()

algorithm = DIRECT()

ret = minimize(problem,
               algorithm,
               ("n_iter", 20),
               verbose=True)

