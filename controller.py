import model
import view


def change_rng_err(n0: int, n: int) -> bool:
    if n0 < n and (model.dt.main_grid.x_end - model.dt.main_grid.x_start) / n0 < model.dt.max_step_size and (
            n0 != model.dt.rng_err_n0 or n != model.dt.rng_err_n):
        model.rng_err_n0 = n0
        model.rng_err_n = n
        model.dt.euler_rng_err.set_range(n0, n)
        model.dt.imp_euler_rng_err.set_range(n0, n)
        model.dt.runge_kutta_rng_err.set_range(n0, n)
        return True
    return False


def change_grid(grid: model.Grid) -> bool:
    if model.dt.main_grid != grid and grid.x_start < grid.x_end and (
            grid.x_end - grid.x_start) / grid.step_num < model.dt.max_step_size and model.dt.function.check_domain(
            grid.x_start, grid.y_start):
        model.main_grid = grid
        model.dt.exact_sol.set_grid(grid)
        model.dt.euler_met.set_grid(grid)
        model.dt.imp_euler_met.set_grid(grid)
        model.dt.runge_kutta_met.set_grid(grid)
        model.dt.euler_err.set_grid(grid)
        model.dt.imp_euler_err.set_grid(grid)
        model.dt.runge_kutta_err.set_grid(grid)
        model.dt.euler_rng_err.set_grid(grid)
        model.dt.imp_euler_rng_err.set_grid(grid)
        model.dt.runge_kutta_rng_err.set_grid(grid)
        return True
    return False


def change_checkbox(exact: bool, euler: bool, imp_euler: bool, runge_kutta: bool) -> bool:
    if model.dt.show_exact != exact or model.dt.show_euler != euler \
            or model.dt.show_imp_euler != imp_euler or model.dt.show_runge_kutta != runge_kutta:
        model.show_exact = exact
        model.show_euler = euler
        model.show_imp_euler = imp_euler
        model.show_runge_kutta = runge_kutta
        return True
    return False


if __name__ == '__main__':
    model.dt = model.Data()
    view.launch_gui()
