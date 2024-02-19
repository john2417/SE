# SE
Git - I have used Git. And made three branches. https://github.com/john2417/SE.git

UML - I drew three diagrams. First is the d-Diagram about Library Management. The second is Class-diagram. I drew all the classes and functions that I used. The last one is the User information inquiry Sequence Diagram. It's a diagram of the Sequence of the user and the database. [UML](https://github.com/john2417/SE/tree/c3bb83e1190b5ce0262e4bc65d8af7e51f50f3d4/UML)

DDD - I have brainstormed with the events in the Library. And changed the events into certain domains and put them into the Core domain chart. With those domains, I have made a relationship domain diagram. [DDD](https://github.com/john2417/SE/tree/3fe00b112a58c6d70e412f7f1e74ff79206db453/DDD)

Metrics - I have used Sonarqube and Pylint. My code was written in Python so I have to use them. There is a screenshot of Sonarqube and Pylint. And project zip file of Sonarqube. [Metrics](https://github.com/john2417/SE/tree/3fe00b112a58c6d70e412f7f1e74ff79206db453/Metrics)

CCD - This is the My personal CCD cheat sheet.[Cheat sheet](https://github.com/john2417/SE/blob/3fe00b112a58c6d70e412f7f1e74ff79206db453/CCD/Personal%20CCD%20cheat%20sheet.pdf) And the five points.
1. Add a good commentary 
https://github.com/john2417/SE/blob/3fe00b112a58c6d70e412f7f1e74ff79206db453/Library_Management/Edit.py#L17-L26

3. Use a descriptive name  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/User.py#L1-L8

5. Separate singular from plural  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/Edit.py#L227-L231

7. Give each class/function only one purpose  
 https://github.com/john2417/SE/blob/9f2d80f363f9e13d9f16f9d2a502bf8bb6e08a0b/Library_Management/Edit.py#L74-L78

9. When the logic is finished, give a line  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/Edit.py#L28-L35

Build - I have tried Gradle. Gradle is more appropriate with Java so I tried Java code for Gradle. This is the screenshot that I ran the jar file that I built. [Screen shot1](https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/gradle/gradle.png) [Screen shot2](https://github.com/john2417/SE/blob/36a6208affe274c4ef56ed4dd147cc35cafe4f3b/gradle/gradle2.png)
 It shows the CSV file in the Library program. And says hello. [Gradle](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/app/build.gradle)
 
Continuous Delivery - I tried 3 whole days trying to get Jenkins to work. But when I fixed some errors different errors keep occurred. So I changed it to GitHub action. I made two GitHub actions. First one is to build [gradle](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/.github/workflows/gradle.yml), and Second one is running [python unittest](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/.github/workflows/python-application). 

Unit tests - I have made unit tests using unittests. And it was written in Python. The test was for the functions in [Edit](https://github.com/john2417/SE/blob/8885a1511aca2500ce67cb357c4c700ef24f3d8e/Library_Management/Edit.py). [Unittest](https://github.com/john2417/SE/blob/8885a1511aca2500ce67cb357c4c700ef24f3d8e/Library_Management/Edittest.py)

IDE - The IDE I used was [VScode](https://github.com/john2417/SE/blob/d60fa96c046cf632c0df0064e18c0a9ca1d37f5e/IDE/VS%20Code.png). And my favorite key shortcut is ctrl +K,ctrl+C. Which can make a lot of code into comments. I use them when I want to check something without other codes. 

DSL - I made a simple DSL with Python. I used partial. And if someone wants to print the file you can just write 
pritfile|[file_name]. 
[DSL](https://github.com/john2417/SE/blob/d60fa96c046cf632c0df0064e18c0a9ca1d37f5e/Library_Management/DSL.py)

Functional Programming - 1. Only final data structures. https://github.com/john2417/SE/blob/71358f55304abd7b044475cc90ecfdeeed137eab/Library_Management/Edit.py#L55-L60
2. (mostly) side-effect-free functions
https://github.com/john2417/SE/blob/71358f55304abd7b044475cc90ecfdeeed137eab/Library_Management/Edit.py#L177-L188
3. the use of higher-order functions
https://github.com/john2417/SE/blob/a72d15e73de1748d406cfbb21a4e1a4d97b5b838/Library_Management/Function_high.py#L1-L21
4. functions as parameters and return values
https://github.com/john2417/SE/blob/a72d15e73de1748d406cfbb21a4e1a4d97b5b838/Library_Management/Edit.py#L157-L167
5. use closures / anonymous functions
https://github.com/john2417/SE/blob/a72d15e73de1748d406cfbb21a4e1a4d97b5b838/Library_Management/Function_high.py#L24-L27
