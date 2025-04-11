# World Database Quiz Application

A Python-based interactive quiz application that uses MySQL's "world" database to generate geography questions and test users' knowledge.

## Description

This application connects to the standard MySQL "world" database and generates quiz questions about countries and cities. Users are presented with questions like "Which country is the city 'Paris' located in?" and must provide the correct answer. The application tracks scores and provides immediate feedback on answers.

## Features

- Connects to MySQL's "world" database
- Generates random geography questions
- User-friendly Tkinter GUI interface
- Score tracking and feedback
- Clean three-tier architecture

## Architecture

The application follows a three-tier architecture:
- **UI Layer**: Tkinter-based graphical user interface
- **Application Layer**: Quiz logic and database connectivity
- **Data Layer**: MySQL "world" database

## Prerequisites

- Python 3.6+
- MySQL Server with the "world" database installed
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/world-database-quiz.git
   cd world-database-quiz
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Make sure MySQL is running with the "world" database imported
   - If you don't have the "world" database, you can download it from [MySQL's website](https://dev.mysql.com/doc/index-other.html)

4. Update the database connection details in `quiz_app.py`:
   ```python
   self.conn = mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="world"
   )
   ```

## Usage

Run the application:
```
python quiz_app.py
```

Answer the geography questions by typing in the country name and clicking "Submit Answer". Your score will be tracked as you progress through the quiz.

## Project Structure

```
world-database-quiz/
├── quiz_app.py        # Main application file
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Future Improvements

- Add more question types (capitals, populations, etc.)
- Implement difficulty levels
- Add persistent user accounts and high scores
- Include visual elements like maps
- Add multiplayer functionality

## License

MIT License - See LICENSE file for details

## Acknowledgments

- MySQL for providing the "world" sample database
- The Tkinter documentation and community
