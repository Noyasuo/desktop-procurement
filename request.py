import tkinter as tk
from tkinter import ttk

class RequestScreen(tk.Frame):
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
        tk.Label(self, text="Request Screen", font=("Arial", 16), bg="lightgrey").pack(pady=20)

        # Create a frame for the table
        table_frame = tk.Frame(self, bg="lightgrey")
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table (Treeview widget) with custom style
        self.table = ttk.Treeview(table_frame, style="Custom.Treeview",
                                  columns=("name", "email", "request_date", "quantity", "price", "product", "status"),
                                  show="headings")

        # Define headings and column widths
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("request_date", text="Request Date")
        self.table.heading("quantity", text="Quantity")
        self.table.heading("price", text="Price")
        self.table.heading("product", text="Product")
        self.table.heading("status", text="Status")

        self.table.column("name", width=150)
        self.table.column("email", width=200)
        self.table.column("request_date", width=100)
        self.table.column("quantity", width=80)
        self.table.column("price", width=80)
        self.table.column("product", width=150)
        self.table.column("status", width=100)

        # Add sample data to the table
        self.populate_table()

        # Add vertical scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(fill="both", expand=True)

        # Bind row selection to display approval/decline buttons
        self.table.bind("<ButtonRelease-1>", self.on_row_selected)

        # Action frame for the approval and decline buttons
        self.action_frame = tk.Frame(self, bg="lightgrey")
        self.action_frame.pack(pady=10)

        # Approve button
        self.approve_button = tk.Button(self.action_frame, text="Approve", command=self.approve_request, state="disabled", bg="green", fg="white")
        self.approve_button.grid(row=0, column=0, padx=10)

        # Decline button
        self.decline_button = tk.Button(self.action_frame, text="Decline", command=self.decline_request, state="disabled", bg="red", fg="white")
        self.decline_button.grid(row=0, column=1, padx=10)

    def populate_table(self):
        """Populates the table with sample data."""
        sample_data = [
            ("John Doe", "johndoe@example.com", "2023-10-01", 5, "$100", "Product A", "Pending"),
            ("Jane Smith", "janesmith@example.com", "2023-10-02", 10, "$200", "Product B", "Pending"),
            ("Sam Brown", "sambrown@example.com", "2023-10-03", 3, "$150", "Product C", "Pending"),
        ]

        for row in sample_data:
            self.table.insert("", "end", values=row)

    def on_row_selected(self, event):
        """Enables the Approve and Decline buttons when a row is selected."""
        selected_item = self.table.selection()
        if selected_item:
            self.selected_row_id = selected_item[0]
            # Enable the action buttons
            self.approve_button.config(state="normal")
            self.decline_button.config(state="normal")

    def update_status(self, status):
        """Updates the status of the selected row."""
        if hasattr(self, 'selected_row_id'):
            self.table.set(self.selected_row_id, "status", status)

    def approve_request(self):
        """Handles the approval action."""
        if hasattr(self, 'selected_row_id'):
            name = self.table.item(self.selected_row_id, 'values')[0]  # Get the name from the row
            self.update_status("Approved")
            print(f"Approved request for {name}")

    def decline_request(self):
        """Handles the decline action."""
        if hasattr(self, 'selected_row_id'):
            name = self.table.item(self.selected_row_id, 'values')[0]  # Get the name from the row
            self.update_status("Declined")
            print(f"Declined request for {name}")

# For testing independently
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    app = RequestScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
