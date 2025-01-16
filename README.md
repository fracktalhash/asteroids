<h1 align="center">Asteroids</h1>

<p align="center">
  <img src="https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/YmSwzVB.gif" alt="Asteroids">
</p>

<p align="right"><em>A Boot.dev guided project.</em></p>  

&nbsp;  
&nbsp;  

# Learning Goals  
<font size="5">   

- Work with multi-file Python projects.  
- Real-world use case for object-oriented programming (OOP).  
- Work with the Pygame library.  

The goal of this project is to create a simple yet playable version of the popular retro game **Asteroids**.

---
&nbsp;
## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---
&nbsp;
## **Overview**
This project recreates the classic arcade game **Asteroids** using Python and the Pygame library. It is designed as a hands-on learning experience for working with multi-file Python projects, implementing object-oriented programming, and utilizing a popular game development library.

---
&nbsp;
## **Features**
- Fully functional 2D space shooter inspired by **Asteroids**.
- Object collisions.
- Smooth animations.
- Modular, object-oriented codebase for scalability.

---
&nbsp;
## **Technologies Used**
- **Python**: Core programming language.
- **Pygame**: For handling game graphics and inputs.
- **Object-Oriented Programming (OOP)**: For clean and modular code structure.

---
&nbsp;
## **Installation**  
To run the project locally, follow these steps:  

1. **Clone the Repository**  
   If you haven't already, clone the repository to your local machine:
   ```bash
   git clone https://github.com/fracktalhash/asteroids.git
   cd fracktalhash/asteroids
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**  
   It’s a good practice to create a virtual environment to keep dependencies isolated. Run the following commands:
   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   Use `pip` to install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**  
   Once the dependencies are installed, you can start the game by running:
   ```bash
   python3 main.py
   ```

---
&nbsp;
## **Usage**

↑ move up  
↓ move down  
→ move right  
← move left  
<sub>└─┘</sub> shoot  

---
&nbsp;
## **Future-enhancements**

- [X] Add "Game Over!" screen  
- [X] Add restart button for "Game Over!" screen
- [ ] Draw random smaler cirlces white fill to make asteroids look cooler

---
&nbsp;
## **License**
This is a learning project by the team at Boot.dev.  
Author: Sarah Schulte  
Maintainers: Lane, Allan, Dan, and Matt