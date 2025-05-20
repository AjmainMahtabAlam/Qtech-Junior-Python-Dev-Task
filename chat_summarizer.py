import os
import re
from collections import Counter
import argparse
import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore

# Download stopwords
nltk.download('stopwords')


def read_chat(file_path):
    user_msgs, ai_msgs = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("User:"):
                user_msgs.append(line[5:].strip())
            elif line.startswith("AI:"):
                ai_msgs.append(line[3:].strip())
    return user_msgs, ai_msgs

# Now call the function with the actual path:
user_msgs, ai_msgs = read_chat(r"C:\Users\ajmai\Downloads\QTECH\sample_chat.txt")


def get_stats(user_msgs, ai_msgs):
    return len(user_msgs) + len(ai_msgs), len(user_msgs), len(ai_msgs)


def get_keywords(user_msgs, ai_msgs, top_n=5):
    stop_words = set(stopwords.words('english'))
    text = " ".join(user_msgs + ai_msgs).lower()
    words = re.findall(r'\b\w+\b', text)
    filtered = [w for w in words if w not in stop_words]
    most_common = Counter(filtered).most_common(top_n)
    return [word for word, _ in most_common]

def generate_summary(total, user_count, ai_count, keywords, filename=None):
    if filename:
        print(f"\n=== Summary for {filename} ===")
    print("Summary:")
    print(f"- The conversation had {total} exchanges.")
    print(f"- User sent {user_count} messages, AI sent {ai_count} messages.")
    print("- Most common keywords:", ", ".join(keywords))

def process_file(file_path):
    user_msgs, ai_msgs = read_chat(file_path)
    total, user_count, ai_count = get_stats(user_msgs, ai_msgs)
    keywords = get_keywords(user_msgs, ai_msgs)
    generate_summary(total, user_count, ai_count, keywords, os.path.basename(file_path))

def process_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            process_file(os.path.join(folder_path, file))

process_folder(r"C:\Users\ajmai\Downloads\QTECH")

