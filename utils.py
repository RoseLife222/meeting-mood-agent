def detect_mood(text):
    # Mocked rule-based logic
    if "behind schedule" in text or "ASAP" in text:
        print("Detected urgency: 'behind schedule' or 'ASAP' → Mood = Frustrated")
        return "Frustrated"
    elif "idea" in text or "explore" in text:
        print("Positive tone detected → Mood = Positive")
        return "Positive"
    else:
        print(" No strong sentiment detected → Mood = Neutral")
        return "Neutral"

def classify_meeting_type(text):
    if "client" in text or "update" in text:
        print("Keywords 'client' or 'update' found → Type = Status Update")
        return "Status Update"
    elif "conflict" in text or "blame" in text:
        print("Conflict-related keywords found → Type = Conflict Resolution")
        return "Conflict Resolution"
    elif "strategy" in text or "plan" in text:
        print("Planning keywords found → Type = Planning")
        return "Planning"
    else:
        print("No specific keywords found → Type = Brainstorming")
        return "Brainstorming"

def recommend_action(mood, meeting_type):
    if mood == "Frustrated" and meeting_type == "Status Update":
        print("Action: Frustrated + Status Update → Schedule a 15-min sync-up and update docs.")
        return "Schedule a 15-min sync-up to realign priorities and update the documentation."
    elif mood == "Positive" and meeting_type == "Brainstorming":
        print("Action: Positive + Brainstorming → Document new ideas and assign tasks.")
        return "Document new ideas and assign exploratory tasks."
    else:
        print("Action: Default → Send summary email and ask for feedback.")
        return "Send summary email and ask for feedback."