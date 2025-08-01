# 🧊 Rubik's Cube Solver with GUI Visualization

This is a Python-based Rubik's Cube solver that includes:
- Step-by-step solving logic
- Tkinter-based GUI for real-time cube visualization
- Scramble, Solve, Undo, and Show Solution Steps features

---

## 📌 Features

- ✅ **Scramble the Cube** randomly  
- 🔄 **Undo** the last move  
- 🎯 **Step-by-step Solver** from White Cross to Final Orientation  
- 📺 **GUI Visualizer** using `Tkinter`  
- 📝 **Move History Tracking**  
- 👁️ **Show Solution Steps** (non-destructive preview)  
- ✨ **Cube fully visible, moves highlighted**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/rubiks-cube-solver.git
cd rubiks-cube-solver
```

### 2. Install Dependencies

Only `numpy` is required:

```bash
pip install numpy
```

### 3. Run the Solver

```bash
python main.py
```

---

## 🗂️ Project Structure

```
rubiks-cube-solver/
│
├── main.py                     # Main GUI Application
├── scramble.py                 # Random scramble logic
├── moves.py                    # All cube move logic (U, D, F, R, L, B)
├── display.py                  # print cube structure on the console
├── white_cross.py              # Step 1 - Solve white cross
├── white_corners.py            # Step 2 - Solve white corners
├── second_layer.py             # Step 3 - Solve second layer
├── yellow_cross.py             # Step 4 - Solve yellow cross
├── match_cross_colors.py       # Step 5 - Match yellow cross edge colors
├── yellow_corner_matching.py   # Step 6 - Match yellow corner positions
├── final_solve.py              # Step 7 - Final yellow corner orientation
```

---

## 🧠 Solving Steps

1. **White Cross**  
2. **White Corners**  
3. **Second Layer**  
4. **Yellow Cross**  
5. **Match Yellow Edges**  
6. **Match Yellow Corners**  
7. **Orient Bottom Corners**

---

## 🖼️ GUI Interface

- 🎨 **Tkinter Canvas** for cube drawing  
- 🔘 Buttons for each move and solving stage  
- 📋 **Move History Panel**  
- 👁️‍🗨️ Show Solution Steps below the button (doesn't alter cube)  
- ♻️ Full visibility and interactive design  

---

## 📸 Example Output

```
Scramble Moves: ["U'", "R", "F", "L'", "B", "D"]
Solution Moves: ['F', 'R', 'U', 'R’', ...]
```

✅ Cube solved with proper face orientation!

---

## 👨‍💻 Author

**Anil Sevakula**  
📧 [anilsevakula143@gmail.com](mailto:anilsevakula143@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/anil-sevakula/)  
💻 [GitHub](https://github.com/AnilSevakula)

---
