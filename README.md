# SE
Git - I have used git. And made three branches. https://github.com/john2417/SE.git

UML - I drew three diagrams. First is the d-Diagram about Library Management. The second is Class-diagram. I drew all the classes and functions that I used. The last one is the User information inquiry Sequence Diagram. It's a diagram of the Sequence of the user and the database. [UML](https://github.com/john2417/SE/tree/c3bb83e1190b5ce0262e4bc65d8af7e51f50f3d4/UML)

DDD - I have brainstormed with the events in the Library. And changed the events into certain domains and put them into the Core domain chart. With those domains, I have made a relationship domain diagram. [DDD](https://github.com/john2417/SE/tree/3fe00b112a58c6d70e412f7f1e74ff79206db453/DDD)
Metrics - I have used Sonarqube and pylint. My code was written in Python so I have to use them. There is a screenshot of Sonarqube and Pylint. And project zip file of Sonarqube. [Metrics](https://github.com/john2417/SE/tree/3fe00b112a58c6d70e412f7f1e74ff79206db453/Metrics)

CCD - This is the My personal CCD cheat sheet.[Cheat sheet](https://github.com/john2417/SE/blob/3fe00b112a58c6d70e412f7f1e74ff79206db453/CCD/Personal%20CCD%20cheat%20sheet.pdf) And the five points.
1. Add a good commentary 
https://github.com/john2417/SE/blob/3fe00b112a58c6d70e412f7f1e74ff79206db453/Library_Management/Edit.py#L17C4-L26C34

3. Use a descriptive name  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/User.py#L1-L8

5. Separate singular from plural  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/Edit.py#L227C5-L231C20

7. Give each class/function only one purpose  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/Edit.py#L233-L237

9. When the logic is finished, give a line  
 https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/Library_Management/Edit.py#L28-L35

Build - I have tried Gradle. Gradle is more appropriate with Java so I tried Java code for Gradle. This is the screenshot that I ran the jar file that I built. [Screen shot1](https://github.com/john2417/SE/blob/a70841f5231c8b09abd619e6a0e13e307d4b1b96/gradle/gradle.png) [Screen shot2](https://github.com/john2417/SE/blob/36a6208affe274c4ef56ed4dd147cc35cafe4f3b/gradle/gradle2.png)
 It shows the CSV file in the Libraryprogram. And says hello. [Gradle](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/app/build.gradle)
 
Continuous Delivery - I tried 3 whole days trying to get Jenkins to work. But when I fixed some errors different errors keep occurred. So I changed it to github action. I made two github actions. First one is to build [gradle](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/.github/workflows/gradle.yml), and Second one is running [python unittest](https://github.com/john2417/SE/blob/e90a1085766810f33ee134671b956a5fb3fbd60f/.github/workflows/python-application). 
