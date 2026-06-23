# Emotion Detection System

An AI-powered web application that identifies emotions from text inputs using IBM Watson NLP. This project is a complete sentiment analysis solution that categorizes text into five primary emotions: Anger, Disgust, Fear, Joy, and Sadness.

## 🚀 Features
- **Real-time Emotion Analysis**: Instantly analyze text sentences for emotional content.
- **Watson NLP Integration**: Leverages IBM's powerful Natural Language Processing libraries.
- **Dominant Emotion Identification**: Automatically highlights the strongest emotion in the provided text.
- **User-friendly Interface**: Simple web frontend for easy interaction.
- **RESTful API**: Exposes detection functionality via a Flask-based web server.

## 🏗️ Architecture
The system consists of three main components:
1.  **Logic Layer (`emotion_detection`)**: Handles API calls to Watson NLP and formats the response.
2.  **Web Server (`server.py`)**: A Flask application that serves the UI and handles detection requests.
3.  **Frontend**: A responsive web interface built with HTML, CSS (Bootstrap), and JavaScript.

## 🛠️ Technologies Used
- **Language**: Python 3.x
- **Framework**: Flask
- **API**: IBM Watson NLP (Emotion Analysis)
- **Frontend**: HTML5, Bootstrap, JavaScript
- **Testing**: Unittest with Mocking

## 📦 Installation
```bash
git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection
pip install -r requirements.txt
```

## 🚀 Usage
1.  Start the Flask server:
    ```bash
    python server.py
    ```
2.  Open your browser and navigate to `http://127.0.0.1:5000`.
3.  Enter text in the provided field and click **Run Sentiment Analysis**.

## 📊 Example Output
**Input**: "I am so happy to have completed this project!"
**Output**: `For the given statement, the system response is 'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.98 and 'sadness': 0.01. The dominant emotion is joy.`

## 📂 Project Structure
```text
.
├── emotion_detection/       # Core logic package
│   ├── __init__.py          # Package initializer
│   └── emotion_detection.py # Watson NLP integration
├── static/                  # Frontend assets (JS, CSS)
├── templates/               # HTML templates
├── server.py                # Flask server
├── test_emotion_detection.py # Unit tests
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## 🔮 Future Improvements
- [ ] Add support for batch text processing.
- [ ] Integrate a database to store and visualize historical analysis.
- [ ] Implement a more advanced UI using React or Vue.

## 👤 Author
**Stina** - *MSc Artificial Intelligence Student*

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
