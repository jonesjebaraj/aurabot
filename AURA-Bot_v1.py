import streamlit as st
from openai import AzureOpenAI

# -------------------------------------
# OpenAI Endpoint Setup
# -------------------------------------

endpoint = "https://tarzanaihub010715832120.openai.azure.com"
deployment = "gpt-4o"
api_key = "5B1zKGt43VaiGZrwPfudKIzTS47hCUn49FubkLqSP97JR1fqptsfJQQJ99BDACYeBjFXJ3w3AAAAACOGxY9o"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

# Sample data 

ai_assistant_data = {
    "emails": [
        {
            "from": "project.manager@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Urgent: Revenue Forecasting Model Update",
            "criticality": "High",
            "content": (
                "Hi,\n\nWe're updating the quarterly forecast. Can you revise the revenue projection model using the latest regional sales inputs?\n"
                "Please prioritize this and share by today EOD for leadership review.\n\nThanks,\nSiddharth"
            )
        },
        {
            "from": "junior.analyst@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Help Needed: SQL Query Optimization",
            "criticality": "Medium",
            "content": (
                "Hi,\n\nI’ve been struggling with a slow-running customer query. Could you help me review the joins and indexes used?\n"
                "Appreciate your time whenever available.\n\nThanks,\nNeha"
            )
        },
        {
            "from": "hr@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Mandatory: Cybersecurity Training Reminder",
            "criticality": "Low",
            "content": (
                "Dear Team,\n\nPlease complete the mandatory cybersecurity training by April 30th. Link and login info attached.\n"
                "Let us know if you face access issues.\n\nRegards,\nHR"
            )
        },
        {
            "from": "dataops@company.com",
            "to": "senior.analyst@company.com",
            "subject": "ETL Job Alert: Job Failure Detected",
            "criticality": "High",
            "content": (
                "Hi,\n\nAn ETL job related to Customer360 failed at 02:00 AM due to a malformed JSON row.\n"
                "Please investigate and advise rerun readiness.\n\n- DataOps Team"
            )
        },
        {
            "from": "manager.analytics@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Appreciation: Q1 Dashboard Delivery",
            "criticality": "Low",
            "content": (
                "Hi,\n\nJust wanted to appreciate your work on the Q1 dashboards. Leadership was impressed with the insights clarity and visual design.\n"
                "Keep up the good work!\n\nCheers,\nLakshmi"
            )
        },
        {
            "from": "marketing.lead@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Weekly Campaign Analytics – Inputs Needed",
            "criticality": "Medium",
            "content": (
                "Hi,\n\nCan we get conversion metrics segmented by campaign source and device type?\n"
                "Would be great to get this by tomorrow’s marketing sync.\n\nThanks,\nAnita"
            )
        },
        {
            "from": "scrum.master@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Sprint Planning Prep – Data Tickets",
            "criticality": "Medium",
            "content": (
                "Hey,\n\nCould you review the pending Jira tickets related to model retraining and tag the dependencies?\n"
                "We need to finalize priorities for the next sprint tomorrow.\n\n- Rahul"
            )
        },
        {
            "from": "platform.lead@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Feedback Requested: Azure Cost Optimization",
            "criticality": "Medium",
            "content": (
                "Hi,\n\nWe're evaluating Azure usage patterns for the analytics team. Could you review the dashboard and suggest areas to optimize compute cost?\n\nThanks,\nRitika"
            )
        },
        {
            "from": "data.governance@company.com",
            "to": "senior.analyst@company.com",
            "subject": "Reminder: PII Data Audit This Week",
            "criticality": "High",
            "content": (
                "Hello,\n\nA reminder that the quarterly PII audit will begin Thursday. Please ensure tagging and lineage metadata are up to date.\n\nRegards,\nCompliance"
            )
        },
        {
            "from": "senior.analyst@company.com",
            "to": "team@company.com",
            "subject": "Planned PTO and Task Delegation",
            "criticality": "Low",
            "content": (
                "Hi Team,\n\nI'll be on PTO from April 22–24. I've assigned data review tasks to Ankit and uploaded documentation on Teams.\n"
                "Ping me before Friday if anything is unclear.\n\nRegards,\nRavi"
            )
        }
    ],

    "call_transcripts": [
        {
            "date": "2025-04-10",
            "title": "Sprint Retro – Data Team",
            "participants": ["senior.analyst@company.com", "scrum.master@company.com", "junior.analyst@company.com"],
            "transcript": (
                "Scrum Master: Let's start with what went well.\n"
                "Senior Analyst: We met our SLAs, and the new anomaly detection workflow is live.\n"
                "Junior Analyst: I liked the peer reviews this sprint. Very helpful.\n"
                "Scrum Master: Great. Anything to improve?\n"
                "Senior Analyst: We can refine ticket estimation. Some tasks took longer than expected."
            )
        },
        {
            "date": "2025-04-12",
            "title": "1:1 Career Check-in",
            "participants": ["senior.analyst@company.com", "manager.analytics@company.com"],
            "transcript": (
                "Manager: I wanted to discuss your growth goals. Any areas you want to focus on?\n"
                "Senior Analyst: I’d like to move into a more solutioning role. Maybe start mentoring more actively.\n"
                "Manager: Great. Let’s set up shadowing opportunities and expand your stakeholder interactions."
            )
        },
        {
            "date": "2025-04-15",
            "title": "DataOps Weekly Sync",
            "participants": ["senior.analyst@company.com", "dataops@company.com", "platform.lead@company.com"],
            "transcript": (
                "Platform Lead: Last week’s Azure spend increased by 12%. Investigating model run durations.\n"
                "Senior Analyst: Noted. I’ll check resource utilization in the notebooks. Might be due to the A/B testing jobs.\n"
                "DataOps: Let's also add auto-shutdown to underutilized clusters."
            )
        },
        {
            "date": "2025-04-16",
            "title": "Client Success Handoff",
            "participants": ["senior.analyst@company.com", "project.manager@company.com", "client.rep@client.com"],
            "transcript": (
                "Project Manager: Ravi will lead the analytics piece for the new product intelligence dashboard.\n"
                "Client: Looking forward to the first version next week.\n"
                "Senior Analyst: We’ll include top features and customer segments as discussed. Will send wireframes tomorrow."
            )
        },
        {
            "date": "2025-04-17",
            "title": "Manager Sync – Quarterly Priorities",
            "participants": ["senior.analyst@company.com", "manager.analytics@company.com"],
            "transcript": (
                "Manager: Let’s focus on improving dashboard adoption.\n"
                "Senior Analyst: Agreed. We could run a UX feedback session and embed micro-guides into the BI tool.\n"
                "Manager: I like that. Also, spend some cycles on enabling self-serve for business users."
            )
        },
        {
            "date": "2025-04-18",
            "title": "Daily Standup",
            "participants": ["senior.analyst@company.com", "scrum.master@company.com", "junior.analyst@company.com"],
            "transcript": (
                "Scrum Master: Any blockers today?\n"
                "Senior Analyst: Testing the sales forecasting script. One edge case failing.\n"
                "Junior Analyst: No blockers. Reviewing validation rules.\n"
                "Scrum Master: Cool. Let’s keep each other posted on Teams."
            )
        },
        {
            "date": "2025-04-19",
            "title": "Peer Knowledge Share",
            "participants": ["senior.analyst@company.com", "junior.analyst@company.com", "data.engineer@company.com"],
            "transcript": (
                "Senior Analyst: I’ll walk through the churn model improvements. We added a recency-weighted score.\n"
                "Data Engineer: That’s smart. Helps decay old activity, right?\n"
                "Junior Analyst: Can we also track model drift?\n"
                "Senior Analyst: Yes, good idea. Let’s include that in phase two."
            )
        }
    ],

    "weekly_calendar": {
        "2025-04-14": [
            {"time": "09:30", "title": "Sprint Standup"},
            {"time": "11:00", "title": "Azure Budget Review"},
            {"time": "15:00", "title": "Model Accuracy Audit"}
        ],
        "2025-04-15": [
            {"time": "10:00", "title": "Weekly DataOps Sync"},
            {"time": "13:00", "title": "Client Kickoff Call"},
            {"time": "16:00", "title": "Internal Training – Advanced SQL"}
        ],
        "2025-04-16": [
            {"time": "09:30", "title": "Standup"},
            {"time": "11:30", "title": "UX Review with Design"},
            {"time": "14:30", "title": "Client Dashboard Discussion"}
        ],
        "2025-04-17": [
            {"time": "09:30", "title": "Standup"},
            {"time": "12:00", "title": "Manager Sync"},
            {"time": "15:00", "title": "Data Office Hours"}
        ],
        "2025-04-18": [
            {"time": "10:00", "title": "Forecasting Model Review"},
            {"time": "14:00", "title": "Jira Grooming"}
        ],
        "2025-04-21": [
            {"time": "09:30", "title": "Sprint Planning"},
            {"time": "13:30", "title": "Team Collaboration Workshop"},
            {"time": "16:00", "title": "Monthly Insights Showcase"}
        ],
        "2025-04-22": [
            {"time": "09:30", "title": "Standup"},
            {"time": "11:00", "title": "ETL Monitoring Review"},
            {"time": "15:30", "title": "Campaign Analytics Review"}
        ],
        "2025-04-23": [
            {"time": "09:30", "title": "Standup"},
            {"time": "14:00", "title": "Client Feedback Loop"},
            {"time": "17:00", "title": "Mentor Check-In"}
        ],
        "2025-04-24": [
            {"time": "09:30", "title": "Standup"},
            {"time": "12:00", "title": "Product Analytics Alignment"},
            {"time": "15:00", "title": "Peer Demo – Feature Adoption Metrics"}
        ],
        "2025-04-25": [
            {"time": "10:00", "title": "BI Tooling Exploration"},
            {"time": "14:00", "title": "Quarterly Retrospective"}
        ]
    },

    "half_yearly_goals": {
        "goal_period": "Jan 2025 – Jun 2025",
        "goals": [
            {
                "title": "Increase Stakeholder Dashboard Adoption",
                "description": "Improve usage of key dashboards through embedded documentation and feedback loops.",
                "status": "In Progress"
            },
            {
                "title": "Enhance Forecasting Accuracy",
                "description": "Incorporate macroeconomic factors and historical anomalies into revenue forecasting models.",
                "status": "In Progress"
            },
            {
                "title": "Mentor Junior Data Team Members",
                "description": "Conduct weekly office hours and learning sessions on ML and analytics best practices.",
                "status": "Ongoing"
            },
            {
                "title": "Implement Cost Optimization for Azure Workloads",
                "description": "Reduce cloud spend by 20% via job-level tuning and auto-scaling policies.",
                "status": "Yet to start"
            },
            {
                "title": "Drive Analytics Governance",
                "description": "Tag 100% of datasets and dashboards with metadata, lineage, and data classifications.",
                "status": "In Progress"
            }
        ]
    }
}


# Streamlit App
st.set_page_config(page_title="AURA - Your Personal AI Assistant", page_icon="🤖", layout="wide")

# Design and Style
st.markdown("""
    <style>
    body {
        background-color: #e5ddd5;
    }
    .msg-bubble {
        max-width: 75%;
        padding: 10px 14px;
        margin: 8px 0;
        border-radius: 10px;
        font-size: 15px;
        line-height: 1.5;
        word-wrap: break-word;
        display: inline-block;
        color: black;
    }
    .user-msg {
        background-color: #dcf8c6;
        align-self: flex-end;
        text-align: right;
        margin-left: auto;
        border-bottom-right-radius: 0;
    }
    .bot-msg {
        background-color: #fa9d9d;
        align-self: flex-start;
        text-align: left;
        margin-right: auto;
        border-bottom-left-radius: 0;       
    }
    .input-container {
        background-color: blue;        
        padding: 10px;
        border-top: 1px solid #ccc;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
    }
    .input-text {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border-radius: 25px;
        border: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'> 🤖 AURA - Your Personal AI Assistant</h2>", unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": (
            "You are a AI personal assistant, who will help me to be a better version of myself. "
            "You will help me track my daily workload, emails, chats, reminders, and tasks and help me stay organized. "
            "You will help me stay focused on my short and long term goals. In order to do this, you will get inputs from my emails, call transcripts, calandar, Hr feedback system."
            "Based on the question asked answer only that answer from the data provided. For example, "
            "if the question is on what are today's deliverables then try answer that question along not all the to do list for the entire week. "
            "Sound like to give motivation when you engage with the individual and try to create excitement and engagement with your responses."
            f"Content can be found here: {ai_assistant_data}"
        )
    }]

# -----------------------------
# Proactive Stimulations (Sidebar)
# -----------------------------
with st.sidebar:
    st.markdown("### ⏰ Proactive Stimulations")
    goal_clicked = st.button("Goal Reminder")
    monday_clicked = st.button("Monday Planner")

if goal_clicked:
    # Compose prompt from goals and progress
    goals = ai_assistant_data["half_yearly_goals"]["goals"]
    progress_summary = (
        f"You are currently in the middle of your goal period ({ai_assistant_data['half_yearly_goals']['goal_period']}). "
        "Here are your goals and their statuses:\n"
    )
    for goal in goals:
        progress_summary += f"- {goal['title']}: {goal['status']}\n"
    proactive_prompt = (
        f"{progress_summary}\n"
        "Based on the above, generate a proactive, actionable reminder that nudges the user to make progress. "
        "Be specific and context-aware. For example, if a goal is to mentor juniors, suggest checking in with a mentee. "
        "Do not repeat the goals, just output a single, concise, actionable reminder."
    )
    try:
        reminder_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": (
                    "You are a AI assistant that helps users make progress on their long-term goals. "
                    "Your job is monitor the progress of long term goals and proactively keep the individual informed on the progress, "
                    "inform him on the current status, forecast if at the current rate he will be able to complete or not, "
                    "give him motivation, engage with him proactively to help me completing his goals. "
                    "Have excitement with you engage with the individual, try to make him motivated with your engagement."
                )},
                {"role": "user", "content": proactive_prompt}
            ],
            model=deployment,
            max_tokens=120,
            temperature=0.7,
        )
        reminder = reminder_response.choices[0].message.content.strip()
    except Exception as e:
        reminder = f"Error generating reminder: {e}"
    # Add reminder as assistant message in chat
    st.session_state.messages.append({"role": "assistant", "content": reminder})
    st.rerun()

if monday_clicked:
    # Compose prompt for Monday Planner
    calendar = ai_assistant_data.get("weekly_calendar", {})
    emails = ai_assistant_data.get("emails", [])
    calls = ai_assistant_data.get("call_transcripts", [])
    # Summarize week's calendar
    week_plan = "Here is your calendar for the week:\n"
    for day, events in calendar.items():
        week_plan += f"\n{day}:\n"
        for event in events:
            week_plan += f"  - {event['time']}: {event['title']}\n"
    # Summarize key emails (subjects)
    week_plan += "\nKey recent emails:\n"
    for email in emails[-5:]:
        week_plan += f"  - {email.get('subject', email.get('title', 'No Subject'))}\n"
    # Summarize key calls
    week_plan += "\nKey recent meetings/calls:\n"
    for call in calls[-3:]:
        week_plan += f"  - {call.get('date', '')}: {call.get('title', '')}\n"
    monday_prompt = (
        f"{week_plan}\n\n"
        "You are an AI assistant whose purpose is to consolidate the entire week's work and help the user plan that week better. "
        "The planning should consider enough free time to accommodate any daily urgencies, proactive self-learning schedules, time to catch up with colleagues, and balance work better. "
        "This is like a reminder when the user starts the week on Monday: summarize what is already known about this week so the user can plan incremental work better. "
        "Output a concise, motivating, actionable plan for the week ahead."
    )
    try:
        planner_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": (
                    "You are a Monday Planning assistant. Your job is to help the user plan their week effectively, "
                    "considering scheduled work, free time for urgencies, self-learning, and work-life balance. "
                    "Be concise, motivating, and practical."
                )},
                {"role": "user", "content": monday_prompt}
            ],
            model=deployment,
            max_tokens=250,
            temperature=0.7,
        )
        monday_plan = planner_response.choices[0].message.content.strip()
    except Exception as e:
        monday_plan = f"Error generating Monday Planner: {e}"
    # Add Monday Planner as assistant message in chat
    st.session_state.messages.append({"role": "assistant", "content": monday_plan})
    st.rerun()

# Render Chat UI 
with st.container():
    for msg in st.session_state.messages:
        if msg["role"] == "system":
            continue
        is_user = msg["role"] == "user"
        bubble_class = "user-msg" if is_user else "bot-msg"
        st.markdown(f'<div class="msg-bubble {bubble_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# Input Field at Bottom
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", key="chat_input", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# Handle new message
if submitted and user_input:
    # Add new user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            messages=st.session_state.messages,
            model=deployment,
            max_tokens=300,
            temperature=0.8,
        )
        assistant_reply = response.choices[0].message.content.strip()
    except Exception as e:
        assistant_reply = f"Error: {str(e)}"
    
    # Add bot Response
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    # Rerun the script immediately so the new response shows up
    st.rerun()
