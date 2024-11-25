import json

# In-memory feedback data storage
feedback_list = []  # Stores feedback data

# Save feedback to a JSON file
def save_feedback():
    with open("feedback.json", "w") as file:
        json.dump(feedback_list, file, indent=4)

# Load feedback from a JSON file
def load_feedback():
    global feedback_list
    try:
        with open("feedback.json", "r") as file:
            feedback_list = json.load(file)
    except FileNotFoundError:
        feedback_list = []

# Display feedback screen for providing feedback
def open_feedback_screen(current_user):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Provide Feedback").pack(pady=10)
    tk.Label(root, text="Rate your exchange (1 to 5):").pack()
    rating_entry = tk.Entry(root)
    rating_entry.pack(pady=5)
    tk.Label(root, text="Leave your feedback:").pack()
    feedback_entry = tk.Entry(root, width=50)
    feedback_entry.pack(pady=5)

    def submit_feedback():
        try:
            rating = int(rating_entry.get())
            if 1 <= rating <= 5:
                feedback = feedback_entry.get()
                feedback_list.append({"rating": rating, "feedback": feedback})
                save_feedback()
                messagebox.showinfo("Success", "Feedback submitted successfully")
                open_main_application(current_user)
            else:
                messagebox.showerror("Error", "Rating must be between 1 and 5")
        except ValueError:
            messagebox.showerror("Error", "Invalid rating. Please enter a number between 1 and 5.")

    tk.Button(root, text="Submit Feedback", command=submit_feedback).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

# Display feedback summary
def open_feedback_summary(current_user):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Feedback Summary").pack(pady=10)

    if feedback_list:
        for feedback in feedback_list:
            tk.Label(root, text=f"Rating: {feedback['rating']}, Feedback: {feedback['feedback']}").pack(pady=2)
    else:
        tk.Label(root, text="No feedback available yet.").pack()

    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

