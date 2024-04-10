import pandas
import turtle

# Creating window with Blank Map of Japan as bg
screen = turtle.Screen()
screen.title("Japanese Prefecture Game")
image = "blank-map-of-japan.gif"
screen.addshape(image)
turtle.shape(image)

# Read japan prefecture name and text position from csv
data = pandas.read_csv("japan_47_prefectures_list.csv")
all_prefecture = data.prefecture.to_list()

#Main game
guessed_prefecture = []

while len(guessed_prefecture) < 47:
    answer_prefecture = screen.textinput(title=f"{len(guessed_prefecture)}/47 of prefectures Correct", 
                                            prompt="Guess another prefecture's name").title()
        
    # If player give up, the missing prefecture would be wrap up on new csv
    if answer_prefecture == "Exit":
        missing_prefectures = [pref for pref in all_prefecture if pref not in guessed_prefecture]
        pref_to_learn = pandas.DataFrame(missing_prefectures)
        pref_to_learn.to_csv("pref_name_to_learn.csv")
        break
        
    # If player correctly guessed prefecture, guessed prefecture count+1 
    if answer_prefecture in all_prefecture:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        input_pref_data = data[data.prefecture == answer_prefecture]
        t.goto(int(input_pref_data.x), int(input_pref_data.y))
        t.write(input_pref_data.prefecture.item()) #item() get only the first index
        guessed_prefecture.append(answer_prefecture)

turtle.mainloop()