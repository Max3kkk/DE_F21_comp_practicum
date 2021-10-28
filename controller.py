import model
import view

max_step_size = 0.25


def change_rng_err(n0: int, n: int) -> bool:
    if n0 < n and (model.main_grid.x_end - model.main_grid.x_start) / n0 < max_step_size and (
            n0 != model.rng_err_n0 or n != model.rng_err_n):
        model.rng_err_n0 = n0
        model.rng_err_n = n
        model.euler_rng_err.set_range(n0, n)
        model.imp_euler_rng_err.set_range(n0, n)
        model.runge_kutta_rng_err.set_range(n0, n)
        return True
    return False


def change_grid(grid: model.Grid) -> bool:
    if model.main_grid != grid and grid.x_start < grid.x_end and (
            grid.x_end - grid.x_start) / grid.step_num < max_step_size:
        model.main_grid = grid
        model.exact_sol.set_grid(grid)
        model.euler_met.set_grid(grid)
        model.imp_euler_met.set_grid(grid)
        model.runge_kutta_met.set_grid(grid)
        model.euler_err.set_grid(grid)
        model.imp_euler_err.set_grid(grid)
        model.runge_kutta_err.set_grid(grid)
        model.euler_rng_err.set_grid(grid)
        model.imp_euler_rng_err.set_grid(grid)
        model.runge_kutta_rng_err.set_grid(grid)
        return True
    return False


def change_checkbox(exact: bool, euler: bool, imp_euler: bool, runge_kutta: bool) -> bool:
    if model.show_exact != exact or model.show_euler != euler \
            or model.show_imp_euler != imp_euler or model.show_runge_kutta != runge_kutta:
        model.show_exact = exact
        model.show_euler = euler
        model.show_imp_euler = imp_euler
        model.show_runge_kutta = runge_kutta
        return True
    return False


if __name__ == '__main__':
    view.launch_gui()
