import tkinter as tk
from tkinter import messagebox
import mysql.connector

class WorldQuizApp:
    def __init__(self, master):
        self.master = master
        master.title("World Database Quiz")
        master.geometry("600x500")

        # Database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="world"
        )
        self.cursor = self.conn.cursor(dictionary=True)

        # Quiz variables
        self.current_question = None
        self.score = 0
        self.total_questions = 0

        # Setup UI
        self.setup_ui()

        # Prepare first question
        self.load_next_question()

    def setup_ui(self):
        # Question Label
        self.question_label = tk.Label(
            self.master, 
            text="", 
            font=("Arial", 14), 
            wraplength=500, 
            justify="center"
        )
        self.question_label.pack(pady=20)

        # Answer Entry
        self.answer_entry = tk.Entry(
            self.master, 
            font=("Arial", 12), 
            width=40
        )
        self.answer_entry.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(
            self.master, 
            text="Submit Answer", 
            command=self.check_answer
        )
        self.submit_button.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(
            self.master, 
            text="Score: 0", 
            font=("Arial", 12)
        )
        self.score_label.pack(pady=10)

    def load_next_question(self):
        try:
            # Example query - you can modify this based on your specific database schema
            self.cursor.execute("""
                SELECT 
                    city.Name as question, 
                    country.Name as correct_answer 
                FROM 
                    city 
                JOIN 
                    country ON city.CountryCode = country.Code 
                ORDER BY RAND() 
                LIMIT 1
            """)
            
            self.current_question = self.cursor.fetchone()
            
            if self.current_question:
                # Format the question
                question_text = f"Which country is the city '{self.current_question['question']}' located in?"
                self.question_label.config(text=question_text)
                self.total_questions += 1
                
                # Clear previous answer
                self.answer_entry.delete(0, tk.END)
            else:
                messagebox.showinfo("Quiz Finished", f"Quiz completed! Your final score: {self.score}/{self.total_questions}")
                self.master.quit()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        
        if self.current_question:
            correct_answer = self.current_question['correct_answer']
            
            # Case-insensitive comparison
            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                messagebox.showinfo("Correct!", "Your answer is right!")
            else:
                messagebox.showinfo("Incorrect", f"Wrong answer. The correct answer was {correct_answer}.")
            
            # Update score label
            self.score_label.config(text=f"Score: {self.score}/{self.total_questions}")
            
            # Load next question
            self.load_next_question()

    def __del__(self):
        # Close database connection
        if hasattr(self, 'conn'):
            self.conn.close()

def main():
    root = tk.Tk()
    quiz_app = WorldQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
