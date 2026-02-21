import streamlit as st
import requests
from datetime import date
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Cosmic APOD",
    page_icon="🌌",
    layout="centered"
)

# --- CUSTOM CSS FOR COSMIC VIBE ---
st.markdown("""
<style>
    /* Import a space-age font */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Starfield background animation */
    @keyframes moveStars {
        from {background-position: 0 0;}
        to {background-position: 10000px 5000px;}
    }
    
    .stApp {
        background: radial-gradient(ellipse at bottom, #0d1d31 0%, #0c0d13 100%);
        color: #e0e0e0;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Add moving stars via pseudo-element */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><circle cx="10" cy="10" r="1" fill="white" opacity="0.8"/><circle cx="30" cy="40" r="1.5" fill="white" opacity="0.6"/><circle cx="70" cy="20" r="1" fill="white" opacity="0.9"/><circle cx="85" cy="80" r="2" fill="white" opacity="0.5"/><circle cx="45" cy="70" r="1.2" fill="white" opacity="0.7"/><circle cx="5" cy="90" r="1" fill="white" opacity="0.4"/><circle cx="95" cy="5" r="1.8" fill="white" opacity="0.3"/><circle cx="60" cy="60" r="1" fill="white" opacity="0.5"/></svg>');
        background-repeat: repeat;
        animation: moveStars 200s linear infinite;
        opacity: 0.5;
        pointer-events: none;
        z-index: -1;
    }
    
    /* Glowing text for title */
    h1, h2, h3 {
        color: #fff;
        text-shadow: 0 0 10px #00aaff, 0 0 20px #00aaff, 0 0 30px #00aaff;
        font-weight: 700;
        letter-spacing: 2px;
    }
    
    /* Card effect for the image and explanation */
    .stImage, .stMarkdown {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(5px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #444;
        box-shadow: 0 0 20px rgba(0, 170, 255, 0.3);
    }
    
    /* Style the date input and button */
    .stDateInput, .stButton>button {
        background: rgba(20, 20, 40, 0.8);
        color: white;
        border: 1px solid #00aaff;
        border-radius: 10px;
        font-family: 'Orbitron', sans-serif;
    }
    
    .stButton>button:hover {
        background: #00aaff;
        color: black;
        box-shadow: 0 0 15px #00aaff;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(10, 10, 20, 0.9);
    }
    
    /* Info and error messages */
    .stAlert {
        background: rgba(0, 0, 0, 0.7);
        border-left-color: #00aaff;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: API KEY HANDLING ---
st.sidebar.title("🌠 Configuration")
st.sidebar.markdown("Enter your NASA API key to unlock the cosmos.")

# Try to get key from environment or secrets
api_key = os.getenv("NASA_API_KEY")
if not api_key:
    try:
        api_key = st.secrets.get("NASA_API_KEY", None)
    except Exception:
        pass

# If still no key, show input field
if not api_key:
    api_key = st.sidebar.text_input("NASA API Key", type="password")
    if api_key:
        st.sidebar.success("✅ Key saved for this session")
else:
    st.sidebar.success("✅ API key loaded")

if not api_key:
    st.sidebar.error("Please enter your NASA API key to use the app.")
    st.stop()

# --- MAIN APP ---
st.title("🌌 Cosmic APOD")
st.markdown("### Astronomy Picture of the Day — reimagined")

# Date selector
col1, col2 = st.columns([3, 1])
with col1:
    selected_date = st.date_input(
        "Select a date",
        value=date.today(),
        min_value=date(1995, 6, 16),  # APOD started
        max_value=date.today()
    )
with col2:
    fetch_button = st.button("✨ Fetch", use_container_width=True)

# Caching function
@st.cache_data(ttl=86400)
def fetch_apod(api_key, date_str):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "date": date_str}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch and display
if fetch_button or 'last_date' not in st.session_state:
    with st.spinner("Reaching into the cosmos..."):
        data = fetch_apod(api_key, selected_date.strftime("%Y-%m-%d"))
        if data:
            st.session_state['last_data'] = data
            st.session_state['last_date'] = selected_date

if 'last_data' in st.session_state:
    data = st.session_state['last_data']
    
    # Title with date
    st.subheader(f"**{data['title']}** — {selected_date.strftime('%B %d, %Y')}")
    
    # Media (image or video)
    if data['media_type'] == 'image':
        st.image(data['hdurl'] if 'hdurl' in data else data['url'],
                 caption=data.get('title', ''),
                 use_container_width=True)
    else:
        st.video(data['url'])
    
    # Explanation
    st.markdown(f"**Explanation:** {data['explanation']}")
    
    # Copyright if any
    if 'copyright' in data:
        st.caption(f"📸 © {data['copyright']}")
else:
    # Placeholder with a welcoming message
    st.markdown("""
    <div style="text-align: center; padding: 50px; background: rgba(0,0,0,0.5); border-radius: 15px;">
        <h3 style="color: #aaa;">Select a date and click "Fetch" to begin your cosmic journey.</h3>
        <p style="color: #888;">The Astronomy Picture of the Day (APOD) features stunning images of our universe, accompanied by expert explanations.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>🌠 Data provided by NASA's APOD API | Explore the universe</p>",
    unsafe_allow_html=True
)