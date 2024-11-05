import tkinter as tk
from tkinter import ttk

class ListScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightgrey")
        self.master = master
        self.create_style()  # Apply custom style for row selection color
        self.create_widgets()

    def create_style(self):
        """Create a custom style to change the selected row color."""
        style = ttk.Style()
        style.theme_use("default")
        
        # Configure Treeview selection color
        style.map("Custom.Treeview",
                  background=[("selected", "#397D49")],  # Selected row color
                  foreground=[("selected", "white")])    # Selected row text color

    def create_widgets(self):
        # Title label
        tk.Label(self, text="List Screen", font=("Arial", 16), bg="lightgrey").pack(pady=20)

        # Create a frame for the table
        table_frame = tk.Frame(self, bg="lightgrey")
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table (Treeview widget) with custom style
        self.table = ttk.Treeview(
            table_frame,
            style="Custom.Treeview",
            columns=("name", "email", "request_date", "quantity", "price", "product", "decision"),
            show="headings"
        )

        # Define headings and column widths
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("request_date", text="Request Date")
        self.table.heading("quantity", text="Quantity")
        self.table.heading("price", text="Price")
        self.table.heading("product", text="Product")
        self.table.heading("decision", text="Decision")

        self.table.column("name", width=120)
        self.table.column("email", width=180)
        self.table.column("request_date", width=100)
        self.table.column("quantity", width=70, anchor="center")
        self.table.column("price", width=80, anchor="center")
        self.table.column("product", width=120)
        self.table.column("decision", width=100, anchor="center")

        # Add sample data to the table
        self.populate_table()

        # Add vertical scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(fill="both", expand=True)

    def populate_table(self):
        """Populates the table with sample data."""
        sample_data = [
            ("Alice Johnson", "alice@example.com", "2024-01-01", 10, "$100", "Product A", "Approved"),
            ("Bob Smith", "bob@example.com", "2024-01-05", 5, "$50", "Product B", "Declined"),
            ("Carol White", "carol@example.com", "2024-01-10", 7, "$70", "Product C", "Approved"),
            ("Dave Lee", "dave@example.com", "2024-01-12", 3, "$30", "Product D", "Declined"),
            ("Eve Adams", "eve@example.com", "2024-01-15", 2, "$20", "Product E", "Approved"),
        ]

        for row in sample_data:
            self.table.insert("", "end", values=row)

# To test the ListScreen independently, you can create a root window and add it to this script.
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    app = ListScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
