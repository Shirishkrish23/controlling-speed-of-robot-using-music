# Controlling-the-speed-of-the-robot-using-music

Step 1:

Here, what we do is that we, create a package in our ROS2 workspace in the name of ```articubot_one```. Why this name you mght ask, a YouTuber who runs the channel Articulated Robotics has already created the Gazebo file which we will be working on, as we don't tinker on any of the mechanics of the robot except speeed, we decided to use his model. Now we just go to his GitHub repository which has all the codes and use that.

Step 2:

Now, that we have the Gazebo model of our robot ready, now is the time for the software part. Our aim here is to control the speed of the robot with respect to the frequency of the givne audio signal. We use Fast Fourier Transform(FFT) here to separate out all the the frequency values out of the audio signal. The ```audio_processing_node``` does the job for us here. Now, we create a subscriber for this node which is ```robot_speed_subscriber``` node. Now what this node does is that it shows us all the speed values which is being published in the ```robot_speed``` topic by the ```audio_processing_node``` so that we can see the change in speed for the change in the frequency values

Step 3:

Now, we create another ROS2 node to make the audio play in the background, becuase we couldn't find any plugin that could simulate audio signals inside Gazebo and our attempts in creating a custom plugin has failed multiple times, so we thought of just creating a ```audio_playback_node``` that plays the audio signal in the background. We have created a launch file in the name of ```audio.launch.py``` which launches the ```audio_playback_node``` and the ```audio_processing_node``` simultaneously so that it creates the effect of finding out the frequency values sequentially with respect to the audio signal

Step 4:

After creating the nodes that give us all the desired values, we now try to integrate it with Gazebo, for that we create a node in the name of ```robot_controller``` which takes in all the values and converts that to the corresponding ```Twist``` message and publishes it into another topic called ```cmd_vel```, this is where Gazebo reads the velocity values from, we just do that by making a small change in our ```Gazebo_control.xacro``` file by adding,
```
<command_topic>cmd_vel</command_topic>
```
now, we have got a way to change the velocity of our robot and successfully linked it to Gazebo.

Step 5:

We now just launch the Gazebo file by opening our ROS2 workspace directory and entering,
```
ros2 launch articubot_one launch_sim.launch.py
```
this launches our Gazebo model. Now for running the nodes, we do,
```
ros2 launch articubot_one audio.launch.py
```
this runs our nodes and you can see the robot move, to see the velocity values you can open another terminal with the ROS2 directory and type,
```
ros2 run articubot_one robot_speed_subscriber
```
and now, we can see the speed of the robot for every second. With this the project is done!
