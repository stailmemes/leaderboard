# a121_catch_a_trtl_.py

#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
turtle_size = 2
turtle_color = "red"
turtle_shape = "turtle"
score = 0
font_setup = ("Arial", 20, "normal")
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----countdown variables-----
timer = 10
counter_interval = 1000 #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
jim = trtl.Turtle()
jim.shape(turtle_shape)
jim.shapesize(turtle_size)
jim.fillcolor(turtle_color)
jim.penup()

#-----initialize score_writer-----
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-100,100)

#-----Initialize countdown_writer-----
counter = trtl.Turtle()
counter.penup()
counter.hideturtle()



#-----game functions--------

def clicked(x,y):
 new_position()
 add_score()


def new_position():
  #randomly places jim the turtle
 global turtle_shape
 global turtle_color
 jim.shape(turtle_shape)
 jim.shapesize(turtle_size)
 jim.fillcolor(turtle_color)
 xpos = rand.randint(-100,100)
 ypos = rand.randint(-100,100)
 jim.goto(xpos, ypos)


def add_score():
  #adds 1 to score
  global score
  score +=1
  score_writer.clear()
  score_writer.goto(-100,100)
  score_writer.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.goto(80, 100)
  counter.clear()
  if timer <= 0:
   counter.write("Time's Up", font=font_setup)
   timer_up = True
   manage_leaderboard()
   jim.hideturtle()
  else:
   counter.write("Timer: " + str(timer), font=font_setup)
   timer -= 1
   counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global jim

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)



#-----events----------------
jim.onclick(clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()