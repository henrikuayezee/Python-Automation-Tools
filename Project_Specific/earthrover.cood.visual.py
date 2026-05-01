"""
Script: earthrover.cood.visual.py
Description: Tool for earthrover.cood.visual
Category: Project_Specific
"""
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class AnnotationViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Annotation Viewer with Smart Zoom and Scroll")

        self.image = None
        self.original_image = None
        self.tk_img = None
        self.scale = 1.0
        self.annotations = []
        self.last_focus_coords = None

        # === Controls ===
        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(control_frame, text="Load Image", command=self.load_image).pack(side=tk.LEFT)
        self.label_entry = tk.Entry(control_frame, width=15)
        self.label_entry.insert(0, "Label")
        self.label_entry.pack(side=tk.LEFT, padx=2)

        self.coord_entry = tk.Entry(control_frame, width=30)
        self.coord_entry.insert(0, "x1,y1;x2,y2 OR x,y")
        self.coord_entry.pack(side=tk.LEFT, padx=2)

        tk.Button(control_frame, text="Add Annotation", command=self.add_annotation).pack(side=tk.LEFT, padx=2)
        tk.Button(control_frame, text="Zoom In (+)", command=lambda: self.zoom(1.2)).pack(side=tk.LEFT, padx=2)
        tk.Button(control_frame, text="Zoom Out (-)", command=lambda: self.zoom(0.8)).pack(side=tk.LEFT, padx=2)
        tk.Button(control_frame, text="Reset Annotations", command=self.reset_annotations).pack(side=tk.LEFT, padx=2)

        # === Scrollable Canvas ===
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="grey")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.hbar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.vbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)

        self.canvas.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        self.hbar.grid(row=1, column=0, sticky="ew")
        self.vbar.grid(row=0, column=1, sticky="ns")

        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)

        # === Mouse Scroll Bindings ===
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)         # Vertical scroll
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_shiftwheel)   # Horizontal scroll

    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tif")]
        )
        if not file_path:
            return

        self.original_image = Image.open(file_path)
        self.scale = 1.0
        self.annotations = []
        self.last_focus_coords = None
        self.redraw_canvas()

    def redraw_canvas(self):
        if not self.original_image:
            return

        scaled_width = int(self.original_image.width * self.scale)
        scaled_height = int(self.original_image.height * self.scale)
        self.image = self.original_image.resize((scaled_width, scaled_height), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(self.image)

        self.canvas.delete("all")
        self.canvas.config(scrollregion=(0, 0, scaled_width, scaled_height))
        self.canvas_image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

        for label, coord in self.annotations:
            self.draw_annotation(label, coord)

        # Center view on last added annotation
        if self.last_focus_coords:
            fx, fy = map(lambda v: v * self.scale, self.last_focus_coords)
            self._scroll_to_focus(fx, fy)

    def add_annotation(self):
        if not self.original_image:
            messagebox.showerror("Error", "Load an image first.")
            return

        label = self.label_entry.get().strip()
        coord_str = self.coord_entry.get().strip()

        try:
            if ";" in coord_str:
                pt1, pt2 = coord_str.split(";")
                map(float, pt1.split(","))
                map(float, pt2.split(","))
            else:
                map(float, coord_str.split(","))
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid coordinate format.\n\nError: {e}")
            return

        self.annotations.append((label, coord_str))
        self.last_focus_coords = self._get_focus_coords(coord_str)
        self.draw_annotation(label, coord_str)

    def draw_annotation(self, label, coord_str):
        if ";" in coord_str:
            pt1, pt2 = coord_str.split(";")
            x1, y1 = map(lambda v: float(v) * self.scale, pt1.split(","))
            x2, y2 = map(lambda v: float(v) * self.scale, pt2.split(","))
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="green", width=2)
            self.canvas.create_text(x1, y1 - 10, text=label, fill="green")
        else:
            x, y = map(lambda v: float(v) * self.scale, coord_str.split(","))
            self.canvas.create_oval(x-5, y-5, x+5, y+5, outline="red", width=2)
            self.canvas.create_text(x, y - 10, text=label, fill="red")

    def zoom(self, factor):
        if not self.original_image:
            return
        self.scale *= factor
        self.redraw_canvas()

    def reset_annotations(self):
        self.annotations = []
        self.last_focus_coords = None
        self.redraw_canvas()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_shiftwheel(self, event):
        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")

    def _get_focus_coords(self, coord_str):
        try:
            if ";" in coord_str:
                pt1, _ = coord_str.split(";")
                x, y = map(float, pt1.split(","))
            else:
                x, y = map(float, coord_str.split(","))
            return x, y
        except:
            return None

    def _scroll_to_focus(self, x, y):
        canvas_width = int(self.canvas.cget("width"))
        canvas_height = int(self.canvas.cget("height"))
        img_width = self.image.width
        img_height = self.image.height

        x_center = x - canvas_width / 2
        y_center = y - canvas_height / 2

        x_frac = min(max(x_center / img_width, 0), 1)
        y_frac = min(max(y_center / img_height, 0), 1)

        self.canvas.xview_moveto(x_frac)
        self.canvas.yview_moveto(y_frac)

# === Run the App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AnnotationViewer(root)
    root.mainloop()
