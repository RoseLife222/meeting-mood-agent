from utils import detect_mood, classify_meeting_type, recommend_action

def analyze_meeting(text):
    print("[LOG] Starting meeting analysis...")
    mood = detect_mood(text)
    print(f"[LOG] Detected mood: {mood}")
    meeting_type = classify_meeting_type(text)
    print(f"[LOG] Classified meeting type: {meeting_type}")
    action = recommend_action(mood, meeting_type)
    print(f"[LOG] Recommended action: {action}")

    print(f"Meeting Mood: {mood}")
    print(f"Meeting Type: {meeting_type}")
    print(f"Suggested Action: {action}")

    return {
        "mood": mood,
        "meeting_type": meeting_type,
        "recommended_action": action
    }




if __name__ == "__main__":
    test_input = "We’re behind schedule again. The client asked for changes and no one updated the docs. We need to fix this ASAP."
    analyze_meeting(test_input)