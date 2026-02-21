# 🌌 Cosmic APOD

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nishantdas0079-cosmic-apod-app-caol0e.streamlit.app/) 

A beautifully designed **Astronomy Picture of the Day (APOD)** viewer with a cosmic, star‑filled UI. Built with Streamlit and NASA's APOD API.

## ✨ Features

- **Stunning Cosmic UI** – Dark space background with animated stars, neon‑glowing text, and glass‑morphism cards.
- **Daily Astronomy Images** – Fetch NASA's Astronomy Picture of the Day for any date (from June 16, 1995 onward).
- **HD Support** – Automatically displays high‑resolution images when available.
- **Video Playback** – Handles video‑of‑the‑day entries seamlessly.
- **Responsive Design** – Looks great on desktop and mobile.
- **Secure API Key Handling** – Uses environment variables locally and Streamlit Secrets for deployment.

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – For the web app framework.
- **Requests** – To call the NASA API.
- **Python‑dotenv** – For local environment variable management.
- **NASA APOD API** – The data source.

## 🚀 Live Demo

Check out the live app: [Cosmic APOD](https://nishantdas0079-cosmic-apod-app-caol0e.streamlit.app/) 

## 📦 Local Installation

Follow these steps to run the app on your own machine.

### Prerequisites

- Python 3.8 or higher
- Git
- A NASA API key (get one for free at [api.nasa.gov](https://api.nasa.gov))

# Steps

# 1. Clone the repository
```bash
git clone https://github.com/NishantDas0079/Cosmic_APOD.git
cd Cosmic_APOD
```

# 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

# 3. Install dependencies
```bash
pip install -r requirements.txt
```

# 4. Set up your NASA API key

Create a file named `.env` in the project root.

Add the following line, replacing `your_key_here` with your actual API key:
```
NASA_API_KEY=your_key_here
```

# 5. Run the app
```
streamlit run app.py
```

Open your browser and go to `http://localhost:8501`

# ☁️ Deploy to Streamlit Cloud
Push your code to a GitHub repository. 

Go to share.streamlit.io and sign in with GitHub.

Click "New app" and select your repository.

In "Advanced settings", add your NASA API key as a secret:

```toml
NASA_API_KEY = "your_key_here"
```
Click "Deploy". Your app will be live in a few minutes.

# 🎨 Customization
Feel free to tweak the cosmic theme! The custom CSS is embedded in app.py – you can modify colors, animations, or fonts to suit your taste.
