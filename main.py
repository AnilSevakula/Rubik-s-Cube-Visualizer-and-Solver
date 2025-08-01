import tkinter as tk
import numpy as np
from moves import possible_moves as rotate_face
from scramble import scramble
from white_cross import white_cross_solver
from white_corners import white_corner_solver
from second_layer import solve_second_layer
from yellow_cross import solve_yellow_cross
from match_yellow_cross_edges import solve_yellow_edge_matching
from yellow_corners_matching import solve_yellow_corners_position
from orient_bottom_layer import orient_bottom_yellow_corners

FACE_COLORS = {
    'W': 'white', 'Y': 'yellow', 'G': 'green',
    'B': 'blue', 'O': 'orange', 'R': 'red'
}

FACES = ['U', 'L', 'F', 'R', 'B', 'D']

class RubiksCubeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rubik's Cube Visualizer")
        self.default_cube()

        # Canvas for Cube
        self.canvas = tk.Canvas(master, width=1000, height=650, bg='gray20')
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # Move buttons below cube
        move_frame = tk.Frame(master, bg='gray25')
        move_frame.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        tk.Label(move_frame, text="Moves:", fg='white', bg='gray25').pack()
        moves_row = tk.Frame(move_frame, bg='gray25')
        moves_row.pack()

        self.moves = ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]
        for move in self.moves:
            btn = tk.Button(moves_row, text=move, width=4, command=lambda m=move: self.apply_move(m))
            btn.pack(side='left', padx=2, pady=2)

        # Control Panel on the right
        control_frame = tk.Frame(master, bg='gray25')
        control_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

        tk.Button(control_frame, text="Scramble", width=20, command=self.scramble_cube).pack(pady=5)
        tk.Button(control_frame, text="Solve Cube", width=20, command=self.solve_cube).pack(pady=5)
        tk.Button(control_frame, text="Show Solution Steps", width=20, command=self.show_solution_steps).pack(pady=5)
        tk.Button(control_frame, text="Undo", width=20, command=self.undo_move).pack(pady=5)
        tk.Button(control_frame, text="Reset Cube", width=20, command=self.reset_cube).pack(pady=5)

        tk.Label(control_frame, text="Move History:", fg='white', bg='gray25').pack(pady=5)
        self.history_text = tk.Text(control_frame, height=12, width=40, bg='black', fg='lime', wrap=tk.WORD)
        self.history_text.pack()

        tk.Label(control_frame, text="Solution Steps:", fg='white', bg='gray25').pack(pady=5)
        self.solution_text = tk.Text(control_frame, height=6, width=40, bg='black', fg='cyan', wrap=tk.WORD)
        self.solution_text.pack()

        self.draw_cube()

    def default_cube(self):
        self.cube = {
            'U': np.full((3, 3), 'W'),
            'D': np.full((3, 3), 'Y'),
            'L': np.full((3, 3), 'O'),
            'R': np.full((3, 3), 'R'),
            'F': np.full((3, 3), 'G'),
            'B': np.full((3, 3), 'B'),
        }
        self.move_history = []
        self.cube_history = [self.copy_cube()]
        self.solution_steps = []

    def draw_cube(self):
        self.canvas.delete("all")
        size = 50
        offset_x = 100
        offset_y = 50

        positions = {
            'U': (offset_x + size * 3, offset_y),
            'L': (offset_x, offset_y + size * 3),
            'F': (offset_x + size * 3, offset_y + size * 3),
            'R': (offset_x + size * 6, offset_y + size * 3),
            'B': (offset_x + size * 9, offset_y + size * 3),
            'D': (offset_x + size * 3, offset_y + size * 6),
        }

        for face in FACES:
            x0, y0 = positions[face]
            for i in range(3):
                for j in range(3):
                    color = FACE_COLORS[self.cube[face][i][j]]
                    x = x0 + j * size
                    y = y0 + i * size
                    self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline='black', width=2)

            self.canvas.create_rectangle(
                x0, y0, x0 + size * 3, y0 + size * 3,
                outline='darkgray', width=4
            )

    def apply_move(self, move):
        rotate_face(self.cube, move)
        self.move_history.append(move)
        self.cube_history.append(self.copy_cube())
        self.draw_cube()
        self.update_history_text()
        self.update_solution_text_after_move()

    def scramble_cube(self):
        scramble(self.cube, 20)
        self.move_history = []
        self.cube_history = [self.copy_cube()]
        self.draw_cube()
        self.update_history_text()
        self.solution_text.delete('1.0', tk.END)
        self.solution_steps = []

    def solve_cube(self):
        solving_moves = []
        solving_moves += white_cross_solver(self.cube)
        solving_moves += white_corner_solver(self.cube)
        solving_moves += solve_second_layer(self.cube)
        solving_moves += solve_yellow_cross(self.cube)
        solving_moves += solve_yellow_edge_matching(self.cube)
        solving_moves += solve_yellow_corners_position(self.cube)
        solving_moves += orient_bottom_yellow_corners(self.cube)

        self.move_history += solving_moves
        self.draw_cube()
        self.update_history_text()

    def show_solution_steps(self):
        temp_cube = self.copy_cube()
        solving_moves = []
        solving_moves += white_cross_solver(temp_cube)
        solving_moves += white_corner_solver(temp_cube)
        solving_moves += solve_second_layer(temp_cube)
        solving_moves += solve_yellow_cross(temp_cube)
        solving_moves += solve_yellow_edge_matching(temp_cube)
        solving_moves += solve_yellow_corners_position(temp_cube)
        solving_moves += orient_bottom_yellow_corners(temp_cube)

        self.solution_steps = solving_moves.copy()
        self.solution_text.delete('1.0', tk.END)
        self.solution_text.insert(tk.END, ' '.join(self.solution_steps))
        self.update_solution_text_after_move()  # In case there are already moves done

    def reset_cube(self):
        self.default_cube()
        self.draw_cube()
        self.update_history_text()
        self.solution_text.delete('1.0', tk.END)
        self.solution_steps = []

    def undo_move(self):
        if len(self.move_history) == 0:
            return  # Nothing to undo
        self.move_history.pop()
        if len(self.cube_history) > 1:
            self.cube_history.pop()  # Remove latest state
            self.cube = self.copy_cube_obj(self.cube_history[-1])
        self.draw_cube()
        self.update_history_text()
        self.update_solution_text_after_move()

    def copy_cube(self):
        return {face: np.copy(self.cube[face]) for face in self.cube}

    def copy_cube_obj(self, cube_obj):
        return {face: np.copy(cube_obj[face]) for face in cube_obj}

    def update_history_text(self):
        self.history_text.delete('1.0', tk.END)
        self.history_text.insert(tk.END, ' '.join(self.move_history))

    def update_solution_text_after_move(self):
        if not hasattr(self, 'solution_steps') or not self.solution_steps:
            return
        # Remove moves from solution_steps that match moves in move_history, in order
        matched = 0
        for actual, expected in zip(self.move_history, self.solution_steps):
            if actual == expected:
                matched += 1
            else:
                break
        # Hide already executed moves in the solution panel
        self.solution_text.delete('1.0', tk.END)
        self.solution_text.insert(tk.END, ' '.join(self.solution_steps[matched:]))

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='gray25')
    app = RubiksCubeGUI(root)
    root.mainloop()
