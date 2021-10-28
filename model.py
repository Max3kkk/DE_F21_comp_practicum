from abc import abstractmethod, ABC
from copy import deepcopy

import numpy as np


class Grid:
    def __init__(self, step_num: int, x_end: float, x_start: float = 0, y_start: float = 0):
        self.step_num = step_num
        self.x_end = x_end
        self.x_start = x_start
        self.y_start = y_start
        self.step = (x_end - x_start) / step_num
        self.x_values = [(x_start + x * self.step) for x in range(step_num)]
        self.y_values = []


class Solution(ABC):
    def __init__(self, grid: Grid):
        self._grid = deepcopy(grid)
        self._grid.y_values.clear()
        self._solve()

    @abstractmethod
    def _solve(self):
        pass

    def set_grid(self, new_grid: Grid):
        if new_grid != self._grid:
            self._grid = deepcopy(new_grid)
            self._grid.y_values.clear()
            self._solve()

    def get_grid(self) -> Grid:
        return self._grid


class ExactSolution(Solution, ABC):
    pass


class MyExactSolution(ExactSolution):
    def _solve(self):
        c = np.cbrt(self._grid.y_start) - self._grid.x_start
        for x in self._grid.x_values:
            self._grid.y_values.append((x + c) ** 3)


class Function(ABC):
    @abstractmethod
    def eval(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def check_domain(self, x: float, y: float) -> bool:
        pass


class MyFunction(Function):
    def eval(self, x: float, y: float) -> float:
        return 3 * np.cbrt(y * y)

    def check_domain(self, x: float, y: float) -> bool:
        return y > 0


class NumericalSolution(Solution, ABC):
    def __init__(self, grid: Grid, func: Function):
        self._func = func
        super().__init__(grid)


class EulerMethod(NumericalSolution):
    def _solve(self):
        h = self._grid.step
        y_prev = self._grid.y_start
        self._grid.y_values.append(y_prev)
        for i in range(1, self._grid.step_num):
            x_prev = self._grid.x_values[i - 1]
            new_y = y_prev + h * self._func.eval(x_prev, y_prev)
            y_prev = new_y
            self._grid.y_values.append(new_y)


class ImprovedEulerMethod(NumericalSolution):
    def _solve(self):
        h = self._grid.step
        y_prev = self._grid.y_start
        self._grid.y_values.append(y_prev)
        for i in range(1, self._grid.step_num):
            x_prev = self._grid.x_values[i - 1]
            k1 = self._func.eval(x_prev, y_prev)
            k2 = self._func.eval(x_prev + h, y_prev + h * k1)
            new_y = y_prev + h / 2 * (k1 + k2)
            y_prev = new_y
            self._grid.y_values.append(new_y)


class RungeKuttaMethod(NumericalSolution):
    def _solve(self):
        h = self._grid.step
        y_prev = self._grid.y_start
        self._grid.y_values.append(y_prev)
        for i in range(1, self._grid.step_num):
            x_prev = self._grid.x_values[i - 1]
            k1 = self._func.eval(x_prev, y_prev)
            k2 = self._func.eval(x_prev + h / 2, y_prev + h / 2 * k1)
            k3 = self._func.eval(x_prev + h / 2, y_prev + h / 2 * k2)
            k4 = self._func.eval(x_prev + h, y_prev + h * k3)
            new_y = y_prev + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            y_prev = new_y
            self._grid.y_values.append(new_y)


class Error(ABC):
    def __init__(self, num_solution: NumericalSolution, exact_solution: ExactSolution):
        self._exact_sol = deepcopy(exact_solution)
        self._num_sol = deepcopy(num_solution)
        self._grid = deepcopy(num_solution.get_grid())
        self._grid.y_values.clear()

    @abstractmethod
    def _calc(self):
        pass

    def get_grid(self) -> Grid:
        return self._grid

    def set_grid(self, new_grid: Grid):
        self._exact_sol.set_grid(new_grid)
        self._num_sol.set_grid(new_grid)
        self._calc()


class LocalError(Error):
    def __init__(self, num_solution: NumericalSolution, exact_solution: ExactSolution):
        super().__init__(num_solution, exact_solution)
        self._calc()

    def _calc(self):
        for i in range(self._grid.step_num):
            diff = abs(self._exact_sol.get_grid().y_values[i] - self._num_sol.get_grid().y_values[i])
            self._grid.y_values.append(diff)

    def set_grid(self, new_grid: Grid):
        self._grid = deepcopy(new_grid)
        self._grid.y_values.clear()
        super().set_grid(new_grid)


class RangeError(Error):
    def __init__(self, num_solution: NumericalSolution, exact_solution: ExactSolution,
                 n_initial: int, n_final: int):
        super().__init__(num_solution, exact_solution)
        self._n_initial = n_initial
        self._n_final = n_final
        self._grid = Grid(n_final - n_initial + 1, n_final, n_initial, 0)
        self._calc()

    def _calc(self):
        self._grid.step_num = self._n_final - self._n_initial
        self._grid.y_values = [self._calc_for_steps(step) for step in range(self._n_initial, self._n_final + 1)]

    def _calc_for_steps(self, step_num: int) -> float:
        max_error = 0.0
        new_grid = Grid(step_num, self._exact_sol.get_grid().x_end, self._exact_sol.get_grid().x_start,
                        self._exact_sol.get_grid().y_start)
        self._exact_sol.set_grid(new_grid)
        self._num_sol.set_grid(new_grid)
        for i in range(step_num):
            error = abs(self._exact_sol.get_grid().y_values[i] - self._num_sol.get_grid().y_values[i])
            max_error = max(error, max_error)
        return max_error

    def set_range(self, n_initial, n_final):
        self._n_initial = n_initial
        self._n_final = n_final
        self._grid = Grid(n_final - n_initial + 1, n_final, n_initial, 0)
        self._calc()


class Data:
    def __init__(self, main_grid: Grid = Grid(30, 10, 2, 1), rng_err_n0: int = 30, rng_err_n: int = 100):
        self.show_exact = True
        self.show_euler = True
        self.show_imp_euler = True
        self.show_runge_kutta = True
        self.show_dots = False
        self.main_grid = main_grid
        self.rng_err_n0 = rng_err_n0
        self.rng_err_n = rng_err_n
        self.max_step_size = 0.5

        # self.main_grid = Grid(30, 10, 2, 1)
        self.exact_sol = MyExactSolution(main_grid)
        self.function = MyFunction()

        self.euler_met = EulerMethod(main_grid, self.function)
        self.imp_euler_met = ImprovedEulerMethod(main_grid, self.function)
        self.runge_kutta_met = RungeKuttaMethod(main_grid, self.function)

        self.euler_err = LocalError(self.euler_met, self.exact_sol)
        self.imp_euler_err = LocalError(self.imp_euler_met, self.exact_sol)
        self.runge_kutta_err = LocalError(self.runge_kutta_met, self.exact_sol)

        self.euler_rng_err = RangeError(self.euler_met, self.exact_sol, rng_err_n0, rng_err_n)
        self.imp_euler_rng_err = RangeError(self.imp_euler_met, self.exact_sol, rng_err_n0, rng_err_n)
        self.runge_kutta_rng_err = RangeError(self.runge_kutta_met, self.exact_sol, rng_err_n0, rng_err_n)


dt = Data()
