
# 🧠 Meeting Mood Analyzer & Recommendation Agent

This project is a rule-based AI agent that analyzes short meeting transcripts to detect:

- The overall **mood** of the conversation
- The **type** of meeting (e.g., Status Update, Brainstorming)
- A suitable **next-step action**

Designed as part of an internship task at a startup, this mini-agent simulates real-world emotional and contextual understanding using lightweight logic — with mockable, extensible modules.

---

## ✅ How It Works

Given a line of text such as:

<pre>
“We’re behind schedule again. The client asked for changes and no one updated the docs. We need to fix this ASAP.”
</pre>

The agent will output:

<pre>
Mood: Frustrated
Type: Status Update
Next Step: Schedule a 15-min sync-up to realign priorities and update the documentation.
</pre>


---


## 🔄 Workflow Breakdown

1. <code>detect_mood(text)</code> → Checks for urgency or emotional keywords to classify as:
   - "Frustrated", "Positive", or "Neutral"
2. <code>classify_meeting_type(text)</code> → Matches key terms to identify:
   - "Status Update", "Planning", "Conflict Resolution", or "Brainstorming"
3. <code>recommend_action(mood, type)</code> → Uses conditional logic to map a response:
   - "Schedule follow-up", "Send summary email", etc.

All decisions are <strong>logged</strong> for traceability and clarity.

---


## 📁 Project Structure

```text
├── mood_agent.py        # Main script to analyze input
├── utils.py             # Contains logic for mood/type/action
├── test_inputs.json     # Sample meeting transcripts
├── outputs.json         # Expected output responses
├── requirements.txt     # Python version requirements
└── README.md            # You're here!
```


---


## 🔍 Bonus Features Included

✅ **Logged decision process**  
Each step prints context-aware logs like:

<pre>
Detected urgency: 'ASAP' → Mood = Frustrated
Keywords 'client' or 'update' found → Type = Status Update
</pre>

✅ **Test input/output examples**  
Try out <code>test_inputs.json</code> and view expected responses in <code>outputs.json</code>.

✅ **Modular structure**  
Each logic block is isolated and easy to extend later (e.g., adding LLMs or classifiers).

---


## 🧪 How to Run

In any terminal or GitHub Codespace:

```bash
python mood_agent.py
```

To try it with other inputs, modify the test string inside <code>mood_agent.py</code> or loop through <code>test_inputs.json</code>.

**Output Example:**

<pre>
[LOG] Starting meeting analysis...
Detected urgency: 'ASAP' → Mood = Frustrated
Keywords 'client' or 'update' found → Type = Status Update
Action: Frustrated + Status Update → Schedule a 15-min sync-up and update docs.

Meeting Mood: Frustrated
Meeting Type: Status Update
Suggested Action: Schedule a 15-min sync-up to realign priorities and update the documentation.
</pre>


---

## 🧠 Future Ideas (If Extended)

- Replace stubs with LLM-based classifiers
- Memory log across multiple meetings
- Tag names dynamically
- Deploy with a minimal UI or API

---

👩‍💻 **Author**
Raunak Lakhmani  
AI/ML Intern Task Submission  
For: Ooumph (Startup Internship)