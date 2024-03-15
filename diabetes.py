import tkinter as tk
from tkinter import messagebox

def calculate_diabetes_risk():
    try:
        pregnancies = int(pregnancies_entry.get())
        glucose = float(glucose_entry.get())
        bp = float(bp_entry.get())
        skin_thickness = float(skin_thickness_entry.get())
        insulin = float(insulin_entry.get())
        bmi = float(bmi_entry.get())
        pedigree_function = float(pedigree_function_entry.get())
        age = int(age_entry.get())

        # Formula to calculate diabetes risk
        diabetes_risk = 0.021 * pregnancies + 0.332 * glucose + 0.217 * bp + \
                        0.072 * skin_thickness + 0.009 * insulin + \
                        0.226 * bmi + 0.147 * pedigree_function + 0.122 * age - 3.89

        if diabetes_risk > 0:
            messagebox.showinfo("Result", "You are at risk of diabetes!")
        else:
            messagebox.showinfo("Result", "You are not at risk of diabetes.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Diabetes Risk Calculator")

# Labels
tk.Label(root, text="Pregnancies:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Glucose (mg/dL):").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Blood Pressure (mm Hg):").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Skin Thickness (mm):").grid(row=3, column=0, sticky="w")
tk.Label(root, text="Insulin (mu U/ml):").grid(row=4, column=0, sticky="w")
tk.Label(root, text="BMI:").grid(row=5, column=0, sticky="w")
tk.Label(root, text="Pedigree Function:").grid(row=6, column=0, sticky="w")
tk.Label(root, text="Age:").grid(row=7, column=0, sticky="w")

# Entry fields
pregnancies_entry = tk.Entry(root)
pregnancies_entry.grid(row=0, column=1)
glucose_entry = tk.Entry(root)
glucose_entry.grid(row=1, column=1)
bp_entry = tk.Entry(root)
bp_entry.grid(row=2, column=1)
skin_thickness_entry = tk.Entry(root)
skin_thickness_entry.grid(row=3, column=1)
insulin_entry = tk.Entry(root)
insulin_entry.grid(row=4, column=1)
bmi_entry = tk.Entry(root)
bmi_entry.grid(row=5, column=1)
pedigree_function_entry = tk.Entry(root)
pedigree_function_entry.grid(row=6, column=1)
age_entry = tk.Entry(root)
age_entry.grid(row=7, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_diabetes_risk)
calculate_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
