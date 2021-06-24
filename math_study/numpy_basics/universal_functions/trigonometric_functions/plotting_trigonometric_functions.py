import math
import numpy as np
from math_study.analysis.function_plotting.ufunc_function_plotter import UFuncFunctionPlotter


if __name__ == '__main__':
    # plotting
    plotter = UFuncFunctionPlotter(np.cos, -math.pi, math.pi, 100)
    plotter.fill_y_axis()
    plotter.plotting(-math.pi, math.pi, -1.5, 1.5)

    plotter = UFuncFunctionPlotter(np.cos, -math.pi, math.pi, 100)
    plotter.fill_y_axis()
    plotter.plotting(-math.pi, math.pi, -1.5, 1.5)