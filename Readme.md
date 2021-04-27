# Overview
The project employs [Prof. Dana Nau's](http://www.cs.umd.edu/users/nau/) task planning algorithm Pyhop2 to perform a task of buying groceries using Turtlebot in Gazebo environment. The primary objective of the project is to provide a complete solution, starting from getting the grocery list, arranging the order of retrieving those products optimally, collecting the products and finally buying them without any contingencies. AI planning is not only used for planning all the tasks optmally but also takes failure of any task into account as well.

<p align="center">
  <img src="https://github.com/rodrigodelazcano/AI_Planning_Grocery/blob/master/Resources/Front%20View.jpg">
  <br><b>Figure - Grocery World</b><br>
</p>


## Authors

- [Aakriti Agarwal](https://www.linkedin.com/in/aakriti-agrawal05/)
- [Naman Gupta](https://www.linkedin.com/in/namangupta98/)
- [Rodrigo de Lazcano Perez-Vicente](https://www.linkedin.com/in/rodrigodelazcano/)

## Dependencies
- ROS
- Gazebo
- Turtlebot
- [Pyhop2](https://github.com/patras91/pyhop2)

## Instructions
Open a new terminal and clone the repository.
```
git clone https://github.com/rodrigodelazcano/AI_Planning_Grocery
cd AI_Planning_Grocery
```

### Build Instructions
Navigate to grocery_ai_planning_ws and build using CATKIN MAKE.
```
cd ~/AI_Planning_Grocery/grocery_ai_planning_ws
catkin_make
```

### Run Instructions
- Launch the ROS world.
```
cd ~/AI_Planning_Grocery/grocery_ai_planning_ws/
source devel/setup.bash
roslaunch grocery turtlebot.launch
```
- In the new tab, run the ROS node.
```
source devel/setup.bash
rosrun ai_planning planner.py
```
### Results
Link for the Results: [Video Link](https://drive.google.com/drive/u/0/folders/1MNGH7bco9fh1BIiopohmqfRFfh_OUMve)
Report will be uploaded soon.
