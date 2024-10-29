import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("1300x700")
        self.root.configure(bg="#181b3f")  # Light blue background

        self.levels = [
            [
                {"question": "Find the average of all  prime numbers between 30 and 50 ?" , "options":["40.0", " 39.8" ,"42.5"," 36.4"], "answer": "39.8"},
                {"question": "A man spends 2/5 of his salary on house rent ,\n 3/10 of his salary on food and 1/8 of his salary on conveyance.\n If he has Rs.1400 left with him,find his expenditure on food and conveyance.", "options" : ["Rs.2000,Rs.1100" ,"Rs.2400,Rs.1000" ,"Rs.2100,Rs.1150","Rs.2300,Rs.1200"], "answer" : "Rs.2400,Rs.1000" },
                {"question": "Find the average of first 40 natural numbers?" , "options": ["21.3", "29.6" ,"24 ","20.5"], "answer" : "20.5" },
                {"question": "crate of mangoes contains one bruised mango for every 30 mangoes in the crate.\n If 3 out of every 4 bruised mangoes are considered unsalable and \n there are 12 unsalable mangoes in crate ,then how many mangoes are there in the crate ?" , "options" : ["480" ,"445","540", "425"], "answer" : "480" },
                {"question": "simplify:5005-5000+10" ,"options" : ["4505", "4497","4001","4450"], "answer" : "4505" },
                {"question": "In a caravan ,in addition to 50 hens there are 45 goats and 8 camels with some keepers .\n If the total number of feet be 224 more than the number of heads ,find the number of keepers?","options":["45" ,"15", "25", "35"],"answer":"15" },
                {"question": "Which of the following will come in place of both the question marks in \n the following equation?128+16×?-7×2/7^2-8×6+?^2 =1","options":["3 ","14"," 16", "17"],"answer":"3" },
                {"question": "7 is added to a certain number ,the sum is multiplied by 5,the product is divided by \n 9 and 3 is subtracted from the quotient.The remainder left is 12.The number is","options":[ "30", "20", "40","60"],"answer":"20"},
                {"question": "A class starts at 10 am and lasts till 1.27 pm .Four periods are held during this interval. \n After every period ,5 minutes are given free to the students.The exact duration of each period is :","options":[ "42 mins", "48 mins", "51 mins", "53 mins"],"answer":"48 mins" },
                {"question": "A printer numbers the page of a book starting with 1 and uses 3189 digits in all .\n How many pages does the book have ?","options":["1000","1074","1075", "1080"],"answer":"1074" },
                {"question": "The greatest four digit perfect square number is :","options":["9000","9801","9900", "9981"],"answer":"9801"},
                {"question": "A library has an average of 500 visitors on Sundays and 240 on other days .\n The average number of visitors per day in a month of 30 days beginning with a Sunday is :","options":["250","276", "280","285"],"answer":"285" },
                {"question": "The difference between the number and it's three-fifth is 50.\n What is the number?","options":["75","100","125","None of these"],"answer":"125"},
                {"question": "A number consists of two digits .If the digits interchanges places and \n the new number is added to the original number ,then the resulting number\n will be divisible by:","options":["3","11","9","5"],"answer":"11" },
                {"question": "The ratio 5:4 expressed as a percent equals:","options":["12.5%","40%","80%","125%"],"answer":"125%" },
                {"question": "A man bus an article for rs.27.50 and sells it for rs.28.60.Find his gain percent.","options":["3%","8%","4%","9%"],"answer":"4%" },
                {"question": "If the price of 6 toys is rs.264.37 what will be the approximate price of 5 toys?","options":["rs.140","rs.100","rs.200","rs.220"],"answer":"rs.220"},
                {"question": "A athelete runs 200m race in 24 sec.His speed is :","options":["20km/hr","24km/hr","28.5km/hr","30km/hr"],"answer":"30km/hr"},
                {"question": "The value of log 16 with base 2 is :","options":["1/8","4","8","16"],"answer":"4"},
                {"question": "One side of a rectangular field is 15m and one of its diagonal is 17m.\nFind the area of the field?","options":["120 m^2","180m^2","170m^2","140m^2"],"answer":"120 m^2"  },
            ],
            [   {"question":"Samuel covers the distance from his home to his office at a \n speed of 25 km/hr and comes back at a speed of 4 km/hr.\n He completes the whole journey within 5 hours 48 minutes. \nFind out the distance from his home to office?","options": ["20" ,"18","25","15"],"answer":"20"},
                {"question":"Sum of the age of 4 children born at interval of 4 years is 36.\n What is the age of youngest child?","options":["2 years","3 years","4 years","5 years"],"answer":"3 years"},
                {"question":"How many terms are there in 3,9,27,81........531441?","options":["25","12","13","14"],"answer":"12"},
                {"question":"The difference between a two-digit number and the number obtained \nby interchanging the positions of its digits is 36. \nWhat is the difference between the two digits of that number?","options":["4","5","6","10"],"answer":"4"},
                {"question":"The value of x+1/2x is given as 2, then find the value of 8x3+1/x3?","options":["40/3","20/7","28","40"],"answer":"40"},
                {"question":"If a+b+c = 0, then the value of (a^2/bc) + (b^2/ac) + (c^2/ab) will be?","option":["3","4","2","0"],"answer":"3"},
                {"question":"The hrs hand rotates by x degrees by 600 seconds past 5.\n Find the value of x, if the clock is started at the start of day i.e.\n at time 00:00?","option":["240","175","155","180"],"answer":"155"},
                {"question":"Today is Monday. After 68 days, it will be?","option":["Monday","Saturday","Sunday","Tuesday"],"answer":"Saturday"},
                {"question":"What day on 23.04.1990?","option":["Monday","Tuesday","Wednesday","Friday"],"answer":"Monday"},
                {"question":"A box contains 6 black, 5 brown and 2 yellow balls. If 2 balls are selected at random, \nwhat is the probability that both are black?","option":["4/23","5/26","7/26","8/15"],"answer":"5/26"},
                {"question":"A five digit number is formed by using digits 1, 2, 3, 4 and 5\n  with no two digits same. What is the probability that the formed number is divisible by v4?","option":["1/5","4/5","3/5","1/4"],"answer":"1/5"},
                {"question":"(1015)2 = ?", "option":["1040125","1030225","1050225","1025125"],"answer":"1030225"},
                {"question":"(5√7 + 2√7) (6√7 + 3√7)= ?","option":["521","381","441","481"],"answer":"441"},
                {"question":"A product is sold at two consecutive discounts of 30% and\n subsequently 40%. If the product is sold for 1500,\n what is the marked price on product?","option":["3500","3600","3550","3571"],"answer":"3571"},
                {"question":"A certain quantity of water is mixed with milk priced at \nRs 12 per litre. The price of mixture is Rs 8 per litre.\n Find out the ratio of water and milk in the new mixture?","option":["3:2","1:2","4:5","2:1"],"answer":"1:2"},
                {"question":"In what ratio a vendor should mix rice at Rs.60 per kg \nwith rice at Rs. 68 per kg so that the final rice mixture\n must be of worth Rs. 63 per kg?","option":["1:3","3:1","2:3","3:2"],"answer":"3:1"},
                {"question":"At present, the ratio between ages of Ram and Shyam is 6:5 respectively.\n After 7 years, Shyam’s age will be 32 years.\n What is the present age of Ram?","option":["32","40","30","36"],"answer":"30"},
                {"question":"The ratio of the speed of two trains is 7:8. \nIf the second train\n covers 400 km in 4 h,\n find out the speed of the first train?","option":["69.4 km/h","78.6 km/h","87.5 km/h","40.5 km/h"],"answer":"87.5 km/h"},
                {"question":"Jack consumes 75% of his salary. Later his salary is increased by 20%\n and he increases his\n expenditures by 10%.\n Find the percentage increase in his savings?","option":["51%","60%","50%","55%"],"answer":"50%"},
                {"question":"Ram spends 20% of is salary on food, 15 % of remaining on cloths, \n and 400 on entertainment. If his salary is 10000,\n how much he spends on food?","option":["2000","3000","1500","2500"],"answer":"2000"}
            ],
            [
                {"question": "What is the currency of Brazil?", "options": ["Peso", "Real", "Rupee", "Yen"], "answer": "Real"},
                {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Silver", "Iron"], "answer": "Oxygen"},
            ]
        ]

        # Front screen components
        self.front_label = tk.Label(root, text="InterviewIQ", font=("cursive",60, "bold"), bg="#181b3f", fg="#F67280")
        self.front_label.pack(pady=50)

        self.start_button = tk.Button(root, text="Start", command=self.start_quiz, font=("Helvetica", 30), bg="#181b3f", fg="#F67280")  
        self.start_button.pack(pady=10)

        # Quiz screen components
        self.timer_label = tk.Label(root, text="", font=("cursive", 25 ), bg="#181b3f", fg="#DC143C")  
        self.question_label = tk.Label(root, text="", font=("cursive", 20), bg="#181b3f", fg="#F67280")  
        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value="", font=("cursive", 14), bg="#181b3f", fg="#F67280", borderwidth=0, highlightthickness=0)
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("cursive", 18), bg="#181b3f", fg="#32CD32")  

        self.current_level = -1  # Start with -1 to indicate the front screen
        self.current_question = 0
        self.scores = [0] * len(self.levels)
        self.timer_id = None  # Keep track of the timer ID

    def start_screen(self):
        self.timer_label.pack_forget()
        self.question_label.pack_forget()
        for button in self.radio_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

    def start_quiz(self):
        self.current_level = 0  # Move to the first level
        self.front_label.pack_forget()
        self.start_button.pack_forget()

        self.timer_label.pack(pady=10)  # Add space between question and timer
        self.question_label.pack()  # Show the question label

        for button in self.radio_buttons:
            button.pack(pady=5)  # Show the option buttons with a small gap

        self.next_button.pack(pady=10)  # Show the next button with space

        self.display_question()

    def toggle_maximize(self):
        if self.root.attributes('-zoomed'):
            self.root.attributes('-zoomed', False)
        else:
            self.root.attributes('-zoomed', True)

    def timer(self, seconds):
        if seconds > 0:
            self.timer_label.config(text=f"Timer: {seconds}")
            self.timer_id = self.root.after(1000, lambda: self.timer(seconds - 1))
        elif not self.root._windowingsystem:
            self.show_result()

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def next_question(self):
        self.stop_timer()  # Stop the timer before moving to the next question

        selected_option = self.radio_var.get().strip().lower()
        correct_answer = self.levels[self.current_level][self.current_question]["answer"].strip().lower()
        if selected_option == correct_answer:
            messagebox.showinfo("Well done"," Great job :) ❤❤❤❤❤❤❤❤")
           
        else:
            messagebox.showinfo("Wrong :( ",correct_answer)
       
        if selected_option == correct_answer:
            self.scores[self.current_level] += 1

        self.current_question += 1

        if self.current_question < len(self.levels[self.current_level]):
            self.display_question()
        else:
            level_number = self.current_level + 1
            level_score = self.scores[self.current_level]
            total_questions = len(self.levels[self.current_level])

            messagebox.showinfo("Level Completed", f"Level {level_number} completed!\nYour score: {level_score}/{total_questions}")

            self.current_question = 0
            self.current_level += 1

            if self.current_level < len(self.levels):
                if level_score >=15:
                    self.display_question()
                else:
                    messagebox.showinfo("Quiz  Completed",f"Your total score: {sum(self.scores)}\nSorry,You need a score of 15 or more to proceed to the next level.")
            else:
                self.show_result()

    def display_question(self):
        current_question_data = self.levels[self.current_level][self.current_question]
        self.question_label.config(text=current_question_data["question"])

        options = current_question_data["options"]
        random.shuffle(options)

        for i in range(4):
            self.radio_buttons[i].config(text=options[i], value=options[i])

        self.timer([480, 300, 150][self.current_level])

    def show_result(self):
        total_score = sum(self.scores)
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour total score: {total_score}/{sum(len(level) for level in self.levels)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
