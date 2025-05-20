import os
import re
from collections import Counter
import argparse
import nltk
from nltk.corpus import stopwords

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

