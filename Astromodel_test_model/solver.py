import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon
from matplotlib.tri import Triangulation

class Solver:
    def __init__(self, model_data):
        visual_settings = model_data.get_visual_settings()
        self.GRAPHIC_NAME = visual_settings[0]
        self.TYPE_OF_FILE = visual_settings[1]
        self.MARKER_COLOR = visual_settings[2]
        self.LINE_COLOR = visual_settings[3]
        self.PIC_QUALITY = visual_settings[4]
        self.GRID = visual_settings[5]

        math_settings = model_data.get_math_settings()
        self.N_LAYERS = math_settings[0]
        self.N_SECTORS = math_settings[1]
        self.MIN_RAD = math_settings[2]



    def run_solve(self, output_path: str):


        def update_polygon(tri):
            if tri == -1:
                points = [0, 0, 0]
            else:
                points = triang.triangles[tri]
            xs = triang.x[points]
            ys = triang.y[points]
            polygon.set_xy(np.column_stack([xs, ys]))


        def on_mouse_move(event):
            if event.inaxes is None:
                tri = -1
            else:
                tri = trifinder(event.xdata, event.ydata)
            update_polygon(tri)
            ax.set_title(f'In triangle {tri}')
            event.canvas.draw()


        # Create a Triangulation.
        n_angles = self.N_SECTORS
        n_radii = self.N_LAYERS
        min_radius = self.MIN_RAD
        radii = np.linspace(min_radius, 0.95, n_radii)
        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
        angles[:, 1::2] += np.pi / n_angles
        x = (radii*np.cos(angles)).flatten()
        y = (radii*np.sin(angles)).flatten()
        triang = Triangulation(x, y)
        triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                                y[triang.triangles].mean(axis=1))
                        < min_radius)

        # Use the triangulation's default TriFinder object.
        trifinder = triang.get_trifinder()

        # Setup plot and callbacks.
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        ax.triplot(triang, marker='o', color=self.LINE_COLOR, markerfacecolor=self.MARKER_COLOR)
        polygon = Polygon([[0, 0], [0, 0]], facecolor='y')  # dummy data for (xs, ys)
        update_polygon(-1)
        ax.add_patch(polygon)
        fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
        if self.GRID:
            ax.grid()
            ax.axis('equal')
        plt.savefig(output_path + '/' + self.GRAPHIC_NAME + self.TYPE_OF_FILE, dpi=self.PIC_QUALITY)


