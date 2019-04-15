The code can be found at https://github.com/khushhallchandra/CS-7641 under assignment 4.

Clone the github repository using 'git clone https://github.com/khushhallchandra/CS-7641.git'

It contains two folders:

Burlap: It has all the java BUTLAP project alongwith the dependencies.

Solution: It contains the code for the assignment.

This project uses Java 1.8.0.121, Jython 2.7.0, Python 3.5.2. Other python dependencies could be found in requirements.txt. This project is based on the following repositories:
 - https://github.com/juanjose49/omscs-cs7641-machine-learning-assignment-4
 - https://github.com/JonathanTay/CS-7641-assignment-4

All the required packages are given in the requirements.txt file.

Please install it using `pip install -r requirements.txt`

To recreate the experiments, go to the solution folder and run the following commands in the below order.

jython -J-Xms6000m -J-Xmx6000m easyGW.py
jython -J-Xms6000m -J-Xmx6000m hardGW.py

The above two programs will run for easy and hard grid world problems.

Next, to generate the plots run:

python plot_easy.py

python plot_hard.py

This will generate all the results in the images folder.
