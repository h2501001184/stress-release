"""SQLite database manager for local data persistence."""
import sqlite3
import json
import os
from datetime import datetime, timedelta
import streamlit as st

DB_PATH = "data/wellness.db"

def init_db():
    """Initialize the database with all required tables."""
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Mood check-ins
    c.execute("""
        CREATE TABLE IF NOT EXISTS mood_checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            mood TEXT,
            intensity INTEGER,
            trigger TEXT,
            notes TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Meditation sessions
    c.execute("""
        CREATE TABLE IF NOT EXISTS meditation_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            type TEXT,
            duration INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Worry time entries
    c.execute("""
        CREATE TABLE IF NOT EXISTS worry_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            worry TEXT,
            scheduled_time TEXT,
            status TEXT DEFAULT 'pending',
            reflection TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Thought jar (brain dump)
    c.execute("""
        CREATE TABLE IF NOT EXISTS thought_jar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thought TEXT,
            category TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # CBT journal entries
    c.execute("""
        CREATE TABLE IF NOT EXISTS cbt_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            situation TEXT,
            automatic_thought TEXT,
            distortion TEXT,
            balanced_thought TEXT,
            mood_before INTEGER,
            mood_after INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # User streaks and gamification
    c.execute("""
        CREATE TABLE IF NOT EXISTS user_stats (
            id INTEGER PRIMARY KEY,
            current_streak INTEGER DEFAULT 0,
            longest_streak INTEGER DEFAULT 0,
            total_minutes INTEGER DEFAULT 0,
            total_sessions INTEGER DEFAULT 0,
            garden_level INTEGER DEFAULT 1,
            last_checkin TEXT
        )
    """)

    # Community posts
    c.execute("""
        CREATE TABLE IF NOT EXISTS community_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            anonymous_id TEXT,
            category TEXT,
            content TEXT,
            support_count INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # AI chat history
    c.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

        # Gratitude journal
    c.execute('''
        CREATE TABLE IF NOT EXISTS gratitude_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            entry TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Calm plans

    c.execute("""
        CREATE TABLE IF NOT EXISTS calm_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            morning TEXT,
            midday TEXT,
            evening TEXT,
            completed TEXT DEFAULT '[]',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert default user stats if not exists
    c.execute("INSERT OR IGNORE INTO user_stats (id) VALUES (1)")

    conn.commit()
    conn.close()

def add_mood_checkin(mood, intensity, trigger, notes=""):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute(
        "INSERT INTO mood_checkins (date, mood, intensity, trigger, notes) VALUES (?, ?, ?, ?, ?)",
        (today, mood, intensity, trigger, notes)
    )
    conn.commit()
    conn.close()
    update_streak()

def get_mood_history(days=30):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute(
        "SELECT date, mood, intensity, trigger FROM mood_checkins WHERE date >= ? ORDER BY date",
        (since,)
    )
    data = c.fetchall()
    conn.close()
    return data

def add_meditation_session(med_type, duration):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute(
        "INSERT INTO meditation_sessions (date, type, duration) VALUES (?, ?, ?)",
        (today, med_type, duration)
    )
    c.execute("UPDATE user_stats SET total_minutes = total_minutes + ?, total_sessions = total_sessions + 1 WHERE id = 1",
              (duration,))
    conn.commit()
    conn.close()

def get_meditation_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT total_minutes, total_sessions, current_streak, longest_streak, garden_level FROM user_stats WHERE id = 1")
    stats = c.fetchone()
    conn.close()
    return stats or (0, 0, 0, 0, 1)

def update_streak():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT last_checkin FROM user_stats WHERE id = 1")
    result = c.fetchone()
    last = result[0] if result else None

    if last is None:
        c.execute("UPDATE user_stats SET current_streak = 1, last_checkin = ? WHERE id = 1", (today,))
    elif last == today:
        pass  # Already checked in today
    elif (datetime.strptime(today, "%Y-%m-%d") - datetime.strptime(last, "%Y-%m-%d")).days == 1:
        c.execute("UPDATE user_stats SET current_streak = current_streak + 1, last_checkin = ? WHERE id = 1", (today,))
    else:
        c.execute("UPDATE user_stats SET current_streak = 1, last_checkin = ? WHERE id = 1", (today,))

    c.execute("UPDATE user_stats SET longest_streak = MAX(current_streak, longest_streak) WHERE id = 1")
    conn.commit()
    conn.close()

def add_worry_entry(worry, scheduled_time):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO worry_entries (worry, scheduled_time) VALUES (?, ?)",
        (worry, scheduled_time)
    )
    conn.commit()
    conn.close()

def get_worry_entries():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, worry, scheduled_time, status, reflection FROM worry_entries ORDER BY created_at DESC")
    data = c.fetchall()
    conn.close()
    return data

def complete_worry_entry(entry_id, reflection):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE worry_entries SET status = 'completed', reflection = ? WHERE id = ?", (reflection, entry_id))
    conn.commit()
    conn.close()

def add_thought_jar(thought, category="General"):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO thought_jar (thought, category) VALUES (?, ?)", (thought, category))
    conn.commit()
    conn.close()

def get_thought_jar():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, thought, category, created_at FROM thought_jar ORDER BY created_at DESC LIMIT 50")
    data = c.fetchall()
    conn.close()
    return data

def delete_thought_jar(thought_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM thought_jar WHERE id = ?", (thought_id,))
    conn.commit()
    conn.close()

def add_cbt_entry(situation, automatic_thought, distortion, balanced_thought, mood_before, mood_after):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute(
        "INSERT INTO cbt_journal (date, situation, automatic_thought, distortion, balanced_thought, mood_before, mood_after) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (today, situation, automatic_thought, distortion, balanced_thought, mood_before, mood_after)
    )
    conn.commit()
    conn.close()

def get_cbt_entries():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM cbt_journal ORDER BY timestamp DESC LIMIT 20")
    data = c.fetchall()
    conn.close()
    return data

def add_community_post(anonymous_id, category, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO community_posts (anonymous_id, category, content) VALUES (?, ?, ?)",
              (anonymous_id, category, content))
    conn.commit()
    conn.close()

def get_community_posts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM community_posts ORDER BY created_at DESC LIMIT 50")
    data = c.fetchall()
    conn.close()
    return data

def add_chat_message(role, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_chat_history(limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT role, content FROM chat_history ORDER BY timestamp DESC LIMIT ?", (limit,))
    data = c.fetchall()
    conn.close()
    return list(reversed(data))

def clear_chat_history():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM chat_history")
    conn.commit()
    conn.close()

def get_garden_level():
    stats = get_meditation_stats()
    minutes = stats[0]
    if minutes < 30:
        return 1
    elif minutes < 120:
        return 2
    elif minutes < 300:
        return 3
    elif minutes < 600:
        return 4
    else:
        return 5

def get_affirmation():
    """Get daily affirmation based on date."""
    affirmations = [
        "You are stronger than you know. Every breath is a fresh start.",
        "This moment is enough. You are enough, exactly as you are.",
        "Your thoughts are clouds passing through the sky of your mind.",
        "Peace begins with a single conscious breath.",
        "You have survived 100% of your bad days. This too shall pass.",
        "Courage is not the absence of fear, but moving forward despite it.",
        "Your worth is not measured by your productivity.",
        "Breathe in calm, breathe out tension. You are safe right now.",
        "Every small step forward is still progress. Be proud.",
        "You are allowed to rest. You are allowed to just be.",
        "The present moment is the only moment where life truly exists.",
        "Your feelings are valid, and they are temporary visitors.",
        "You don't have to have it all figured out today.",
        "Kindness to yourself is the foundation of all healing.",
        "Within you is a stillness and a sanctuary to which you can retreat.",
    ]
    day_of_year = datetime.now().timetuple().tm_yday
    return affirmations[day_of_year % len(affirmations)]


def add_gratitude_entry(entry):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO gratitude_journal (date, entry) VALUES (?, ?)", (today, entry))
    conn.commit()
    conn.close()

def get_gratitude_entries(days=30):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    c.execute("SELECT date, entry FROM gratitude_journal WHERE date >= ? ORDER BY date DESC", (since,))
    data = c.fetchall()
    conn.close()
    return data

def get_today_calm_plan():
    day_name = datetime.now().strftime("%A")
    from utils.cbt_tools import DAILY_CALM_PLANS
    return DAILY_CALM_PLANS.get(day_name, DAILY_CALM_PLANS["Monday"])
