# Project Demo

This document showcases the Emotion Detection System in action with sample inputs and expected outputs.

## 🌟 Features Demo

### 1. User Interface
The application features a clean, responsive UI where users can input text and see emotional scores immediately.

### 2. Sample Inputs and Outputs

#### Case 1: Joyful Statement
- **Input**: "I am moving to a new house and I am so excited!"
- **Expected Outcome**: High `joy` score.
- **System Response**: `For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.99 and 'sadness': 0.01. The dominant emotion is joy.`

#### Case 2: Frustrated Statement
- **Input**: "The service was terrible and I am very disappointed."
- **Expected Outcome**: High `anger` or `sadness` score.
- **System Response**: `For the given statement, the system response is 'anger': 0.85, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.0 and 'sadness': 0.08. The dominant emotion is anger.`

#### Case 3: Invalid Input
- **Input**: (Empty string)
- **Expected Outcome**: Error message.
- **System Response**: `Invalid text! Please try again!`

## 📸 Visuals

### Main Interface
When the user arrives at the home page, they see an input area and a button.

---
*Note: As this is a terminal-based setup, actual screenshots would be added here in a real repository. For now, the sample outputs above serve as proof of functionality.*
