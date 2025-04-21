# Import necessary libraries

import streamlit as st
from openai import AzureOpenAI

# -------------------------------------
# OpenAI Endpoint Setup
# -------------------------------------

endpoint = "https://tarzanaihub010715832120.openai.azure.com"
deployment = "gpt-4o"
api_key = "5B1zKGt43VaiGZrwPfudKIzTS47hCUn49FubkLqSP97JR1fqptsfJQQJ99BDACYeBjFXJ3w3AAAAACOGxY9o"
api_version = "2024-12-01-preview"

# Set Client

client=AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

# Sample data 

ai_assistant_data = {
    "emails": [
        {
            "subject": "Request for Weekly Sales Report",
            "from": "priya.singh@company.com",
            "to": "data.analyst@company.com",
            "date": "2025-04-07",
            "body": (
                "Hi,\n\nCould you please generate the weekly sales report for the West Region? "
                "We need breakdowns by product category, channel, and highlight any conversion anomalies.\n\n"
                "Needed by Wednesday EOD for the GTM sync.\n\nThanks,\nPriya Singh\nMarketing Lead"
            )
        },
        {
            "subject": "Data Quality Issue in Customer Table",
            "from": "it.support@company.com",
            "to": "data.analyst@company.com",
            "date": "2025-04-08",
            "body": (
                "Hello,\n\nWe’ve observed null values in the 'customer_segment' field in the production database. "
                "Can you check the ETL job logs and confirm the last update time?\n\nRegards,\nIT Support"
            )
        },
        {
            "subject": "Q2 Planning – Metrics Discussion",
            "from": "analytics.manager@company.com",
            "to": "data.analyst@company.com",
            "date": "2025-04-09",
            "body": (
                "Hi,\n\nLet’s discuss key KPIs for Q2 during tomorrow’s sync. Prepare ideas on retention metrics, "
                "churn prediction improvements, and dashboard enhancements.\n\nBest,\nRajeev"
            )
        },
        {
            "subject": "Weekly Data Team Standup Notes",
            "from": "scrum.master@company.com",
            "to": "data.team@company.com",
            "date": "2025-04-10",
            "body": (
                "Team,\n\nHere are the standup highlights:\n- ETL latency has reduced by 30% after pipeline optimization\n"
                "- Dashboard filter bug resolved\n- Sprint backlog updated in Jira\n\nCheers,\nAnanya"
            )
        },
        {
            "subject": "Planned Leave and Handover",
            "from": "data.analyst@company.com",
            "to": "data.team@company.com",
            "date": "2025-04-05",
            "body": (
                "Hi Team,\n\nI will be on leave from April 15–19. I've shared access to the job monitoring dashboard. "
                "Please review the handover document on Teams and let me know if anything is unclear.\n\nThanks,\nRavi"
            )
        }
    ],

    "call_transcripts": [
        {
            "date": "2025-04-05",
            "title": "Daily Standup – Data Team",
            "participants": ["data.analyst@company.com", "engineer1@company.com", "scrum.master@company.com"],
            "transcript": (
                "Scrum Master: Any blockers today?\n"
                "Data Analyst: Finalizing dashboard filters for Marketing. Small issue with filtering logic, will push fix by EOD.\n"
                "Engineer: ETL latency reduced after partition tuning. No blockers.\n"
                "Scrum Master: Great. Let’s catch up again tomorrow."
            )
        },
        {
            "date": "2025-04-09",
            "title": "Client Sync – Insights Walkthrough",
            "participants": ["data.analyst@company.com", "client@partner.com", "marketing.lead@company.com"],
            "transcript": (
                "Client: We loved the dashboard layout. Can we also get segmentation by city next time?\n"
                "Data Analyst: Yes, we can include geo-segmentation in the next release. Will take 2 days max.\n"
                "Marketing Lead: Perfect. We'll share this version in tomorrow’s newsletter."
            )
        },
        {
            "date": "2025-04-10",
            "title": "1:1 with Manager – H1 Performance Review",
            "participants": ["data.analyst@company.com", "analytics.manager@company.com"],
            "transcript": (
                "Manager: You've exceeded expectations in Q1, especially with churn prediction modeling.\n"
                "Data Analyst: Thank you! I've been focusing on automation and insight delivery speed.\n"
                "Manager: Keep up the momentum. For H2, let’s focus on more self-serve dashboard initiatives and mentoring new analysts."
            )
        }
    ],

    "weekly_calendar": {
        "2025-04-07": [
            {"time": "09:30", "title": "Data Team Standup"},
            {"time": "11:00", "title": "Sprint Planning"},
            {"time": "15:00", "title": "Weekly Marketing Sync"}
        ],
        "2025-04-08": [
            {"time": "10:00", "title": "ETL Review with Engineering"},
            {"time": "14:30", "title": "Customer Segmentation Deep Dive"}
        ],
        "2025-04-09": [
            {"time": "09:30", "title": "Standup"},
            {"time": "11:00", "title": "Client Dashboard Review"},
            {"time": "16:00", "title": "Analytics Community Hour"}
        ],
        "2025-04-10": [
            {"time": "09:30", "title": "Standup"},
            {"time": "13:00", "title": "1:1 with Manager"},
            {"time": "15:30", "title": "Data Governance Workshop"}
        ],
        "2025-04-11": [
            {"time": "10:00", "title": "Q2 Data Strategy Meeting"},
            {"time": "14:00", "title": "Jira Grooming & Retrospective"}
        ]
    },

    "half_yearly_goals": {
        "goal_period": "Jan 2025 – Jun 2025",
        "goals": [
            {
                "title": "Improve Dashboard Usability",
                "description": "Redesign internal dashboards with better filtering and UX. Target 95% user satisfaction.",
                "status": "In Progress"
            },
            {
                "title": "Automate Data Quality Monitoring",
                "description": "Set up alerting and anomaly detection in ETL pipelines using Azure Monitor and ML-based profiling.",
                "status": "Completed"
            },
            {
                "title": "Mentor Junior Analysts",
                "description": "Onboard and mentor two new hires, and conduct bi-weekly learning sessions on SQL and Python.",
                "status": "In Progress"
            },
            {
                "title": "Advance Predictive Analytics",
                "description": "Build models for customer churn and lead scoring to assist marketing and sales targeting.",
                "status": "Achieved"
            }
        ]
    }
}


# Streamlit App
st.set_page_config(page_title="AURA - Your Personal AI Assistant", page_icon="🤖", layout="wide")

# Design and Stye

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

st.markdown("<h2 style='text-align: center;'> 🤖 AURA - Your Personal AI Assistant</h2>",unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": (
        "You are a AI personal assistant, who will help me to be a better version of myself. "
        "You will help me track my daily workload, emails, chats, reminders, and tasks and help me stay organized. "
        "You will help me stay focused on my short and long term goals. In order to do this, you will get inputs from my emails, call transcripts, calandar, Hr feedback system"
        f"Content can be found here: {ai_assistant_data}"
    )
    }
    ]

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
    # Add new user
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

    # Rerun the script immediatly so the new response shows up
    st.rerun()