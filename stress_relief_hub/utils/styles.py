"""Custom CSS styles for the Stress Relief Hub app."""

def load_css():
    return """
    <style>
    /* Main theme */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* SOS Button */
    .sos-button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white;
        font-size: 24px;
        font-weight: bold;
        padding: 20px 40px;
        border-radius: 50px;
        border: none;
        box-shadow: 0 10px 30px rgba(255, 65, 108, 0.4);
        animation: pulse 2s infinite;
        cursor: pointer;
        width: 100%;
        margin: 10px 0;
    }

    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0.7); }
        70% { transform: scale(1.02); box-shadow: 0 0 0 20px rgba(255, 65, 108, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0); }
    }

    /* Breathing circle */
    .breathing-circle {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: radial-gradient(circle, #a8edea 0%, #fed6e3 100%);
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: bold;
        color: #333;
        box-shadow: 0 0 50px rgba(168, 237, 234, 0.5);
    }

    /* Cards */
    .wellness-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Mood buttons */
    .mood-btn {
        font-size: 40px;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid transparent;
        background: rgba(255,255,255,0.8);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .mood-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }

    /* Garden elements */
    .garden-plant {
        font-size: 60px;
        transition: all 0.5s ease;
    }

    /* Chat bubbles */
    .chat-user {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 5px 20px;
        margin: 8px 0;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .chat-bot {
        background: #f0f2f6;
        color: #333;
        padding: 12px 18px;
        border-radius: 20px 20px 20px 5px;
        margin: 8px 0;
        max-width: 80%;
        float: left;
        clear: both;
    }

    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 10px;
    }

    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }

    /* Headers */
    h1, h2, h3 {
        color: #2d3748;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    ::-webkit-scrollbar-thumb {
        background: #667eea;
        border-radius: 4px;
    }
    </style>
    """
