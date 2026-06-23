# Installation Guide

Follow these steps to set up the Emotion Detection System on your local machine.

## Prerequisites
- **Python 3.x**: Ensure you have Python installed. Check with `python --version`.
- **Pip**: Python package manager.

## Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API Access
The system is configured to use the IBM Skills Network Watson NLP API. Ensure you have network access to `https://sn-watson-emotion.labs.skills.network`.

### 5. Run the Application
```bash
python server.py
```

### 6. Verify Installation
Navigate to `http://127.0.0.1:5000` in your web browser. If you see the "NLP - Emotion Detection" header, the installation was successful!
