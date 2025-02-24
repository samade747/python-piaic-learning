import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time
import random

# Page configuration
st.set_page_config(
    page_title="AgentAI - Intelligent Assistance",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for responsive design
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #1E88E5 !important;
        margin-bottom: 1rem !important;
    }
    
    .sub-header {
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        color: #424242 !important;
        margin-bottom: 2rem !important;
    }
    
    .section-header {
        font-size: 2rem !important;
        font-weight: 600 !important;
        color: #0D47A1 !important;
        margin: 1.5rem 0 !important;
    }
    
    .card {
        border-radius: 10px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        background-color: #f8f9fa !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        transition: transform 0.3s ease !important;
    }
    
    .card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15) !important;
    }
    
    .feature-icon {
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
        color: #1E88E5 !important;
    }
    
    .feature-title {
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stButton>button {
        width: 100% !important;
        background-color: #1E88E5 !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px 15px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background-color: #0D47A1 !important;
        transform: scale(1.03) !important;
    }
    
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem !important;
        }
        
        .sub-header {
            font-size: 1.2rem !important;
        }
        
        .section-header {
            font-size: 1.5rem !important;
        }
        
        .card {
            padding: 15px !important;
        }
    }
    
    .testimonial {
        padding: 15px !important;
        border-left: 4px solid #1E88E5 !important;
        background-color: #E3F2FD !important;
        margin-bottom: 15px !important;
    }
    
    .stProgress > div > div {
        background-color: #1E88E5 !important;
    }
    
    div.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem !important;
    }
    
    div.stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
    }
    
    div.stTabs [data-baseweb="tab"] {
        height: 50px !important;
        background-color: #F5F5F5 !important;
        border-radius: 5px 5px 0 0 !important;
        padding: 10px 16px !important;
        gap: 1px !important;
    }
    
    div.stTabs [aria-selected="true"] {
        background-color: #1E88E5 !important;
        color: white !important;
    }
    
    .footer {
        text-align: center !important;
        padding: 20px 0 !important;
        margin-top: 40px !important;
        border-top: 1px solid #e0e0e0 !important;
        color: #757575 !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to simulate AI agent thinking
def simulate_agent_thinking(task, duration=3):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    thinking_phrases = [
        "Analyzing request...",
        "Processing data...",
        "Gathering information...",
        "Considering options...",
        "Formulating response...",
        "Evaluating solutions...",
    ]
    
    for i in range(100):
        if i % 20 == 0:
            status_text.text(random.choice(thinking_phrases))
        progress_bar.progress(i + 1)
        time.sleep(duration/100)
    
    status_text.text(f"Task completed: {task}")
    time.sleep(0.5)
    progress_bar.empty()
    status_text.empty()

# Simulated AI agent response generation
def generate_agent_response(query):
    responses = {
        "schedule": "I've analyzed your calendar and found optimal times for new appointments on Tuesday at 2 PM and Thursday at 10 AM. Would you like me to schedule something for you?",
        "research": "Based on the latest data, I've compiled a comprehensive report on market trends showing 15% growth in AI adoption across enterprises. Would you like to see the detailed analysis?",
        "optimize": "After reviewing your workflow, I've identified three automation opportunities that could save you approximately 5 hours per week. Shall I implement these solutions?",
        "summarize": "I've analyzed the 50-page document and extracted the key points: budget allocation has increased by 12%, new project timelines are set for Q3, and team expansion is planned for next month.",
        "default": "I've processed your request and have several suggestions to offer. Would you like me to proceed with implementing my recommendations?"
    }
    
    for key in responses.keys():
        if key in query.lower():
            return responses[key]
    return responses["default"]

# Function for navigation
def create_navigation():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Features", "Demo", "Use Cases", "Pricing", "Contact"],
        icons=["house", "list-check", "play-circle", "briefcase", "tags", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "#1E88E5", "font-size": "16px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "padding": "10px 15px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#1E88E5", "color": "white"},
        }
    )
    return selected

# Sections
def home_section():
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<h1 class="main-header">The Future of AI Assistance Is Here</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Meet AgentAI, your intelligent companion that understands, learns, and takes action on your behalf.</p>', unsafe_allow_html=True)
        
        st.markdown("""
        AgentAI goes beyond simple chatbots by proactively solving problems, automating workflows, and making intelligent decisions based on your preferences and goals.
        
        Unlike traditional AI assistants, our agents can:
        - Take initiative and propose solutions
        - Learn from your feedback and adapt to your style
        - Execute complex tasks across multiple platforms
        - Maintain context awareness throughout conversations
        """)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.button("Get Started")
        with col_btn2:
            st.button("Watch Demo")
    
    with col2:
        st.image("https://via.placeholder.com/600x400?text=AI+Agent+Visualization", use_column_width=True)

def features_section():
    st.markdown('<h2 class="section-header">Key Features</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">🧠</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Autonomous Reasoning</div>', unsafe_allow_html=True)
        st.write("Our agents think critically, evaluate options, and make decisions based on complex criteria and your preferences.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">🔄</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Adaptive Learning</div>', unsafe_allow_html=True)
        st.write("AgentAI continuously improves through interactions, feedback, and observing your preferences and work patterns.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">🛠️</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Tool Integration</div>', unsafe_allow_html=True)
        st.write("Connect with 100+ applications and services to execute tasks across your entire digital workspace.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">📊</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Data Analysis</div>', unsafe_allow_html=True)
        st.write("Process large datasets, identify patterns, and generate actionable insights with advanced analytical capabilities.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">🔐</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Privacy-First Design</div>', unsafe_allow_html=True)
        st.write("End-to-end encryption and localized processing ensure your data stays private and secure at all times.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-icon">📱</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">Cross-Platform</div>', unsafe_allow_html=True)
        st.write("Access your AI agents from any device with seamless synchronization and consistent performance.")
        st.markdown('</div>', unsafe_allow_html=True)

def demo_section():
    st.markdown('<h2 class="section-header">Interactive Demo</h2>', unsafe_allow_html=True)
    st.write("Experience the power of our agentive AI firsthand. Type a request and see how our agent responds.")
    
    # Demo tabs
    tab1, tab2, tab3 = st.tabs(["Try It Yourself", "Example Workflows", "Capabilities"])
    
    with tab1:
        user_input = st.text_area("What would you like the agent to do?", height=100, 
                                placeholder="E.g., 'Research market trends for AI in healthcare' or 'Schedule a team meeting for next week'")
        
        if st.button("Submit Request"):
            if user_input:
                with st.spinner("Agent is processing your request..."):
                    simulate_agent_thinking(user_input, 2)
                    response = generate_agent_response(user_input)
                    st.success("Agent Response:")
                    st.write(response)
            else:
                st.warning("Please enter a request for the agent to process.")
    
    with tab2:
        st.subheader("Example Agent Workflows")
        
        workflow_expander1 = st.expander("Intelligent Scheduling Assistant", expanded=False)
        with workflow_expander1:
            st.write("""
            The agent analyzes your calendar, meeting preferences, and priorities to:
            1. Find optimal meeting times based on your productivity patterns
            2. Automatically suggest rescheduling less important meetings when conflicts arise
            3. Prepare relevant materials before each meeting
            4. Follow up with meeting notes and action items
            """)
            if st.button("See Demo", key="demo1"):
                simulate_agent_thinking("Optimizing schedule and analyzing calendar patterns", 2)
                st.success("Agent has analyzed your calendar and identified that you schedule too many meetings on Mondays, leading to reduced productivity on Tuesdays. Would you like me to suggest a more balanced weekly schedule?")
        
        workflow_expander2 = st.expander("Research & Summarization Agent", expanded=False)
        with workflow_expander2:
            st.write("""
            The agent gathers, analyzes, and synthesizes information to:
            1. Research topics across multiple sources and verify information
            2. Generate comprehensive summaries with key insights
            3. Create visual representations of complex data
            4. Keep information updated with new developments
            """)
            if st.button("See Demo", key="demo2"):
                simulate_agent_thinking("Researching and synthesizing information on renewable energy trends", 3)
                st.success("I've analyzed 27 recent reports on renewable energy adoption and synthesized the following key trends: 1) Solar installation costs decreased 25% in the past year, 2) Wind energy capacity grew 15% globally, and 3) Battery storage technology is now economically viable for grid-scale implementation. Would you like a detailed analysis of any specific aspect?")
    
    with tab3:
        st.subheader("Agent Capabilities")
        
        capabilities = {
            "Natural Language Understanding": 92,
            "Context Retention": 88,
            "Multi-step Planning": 85,
            "Tool Integration": 90,
            "Learning from Feedback": 82,
            "Decision Making": 87,
            "Data Analysis": 94,
            "Creativity": 80
        }
        
        for capability, score in capabilities.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(capability)
                st.progress(score/100)
            with col2:
                st.write(f"{score}%")

def use_cases_section():
    st.markdown('<h2 class="section-header">Use Cases</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Business Operations")
        st.write("""
        - Automate report generation and data analysis
        - Optimize supply chain and inventory management
        - Handle customer support triage and resolution
        - Manage project timelines and resource allocation
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Personal Productivity")
        st.write("""
        - Manage email and communication workflows
        - Plan and optimize daily schedules
        - Research and summarize topics of interest
        - Track goals and provide accountability
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Creative Work")
        st.write("""
        - Generate content ideas and outlines
        - Provide feedback on creative projects
        - Assist with research and reference gathering
        - Collaborate on design and development tasks
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Knowledge Management")
        st.write("""
        - Create and maintain knowledge bases
        - Extract insights from documents and conversations
        - Connect related information across sources
        - Generate training materials and documentation
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("Success Stories")
    
    st.markdown('<div class="testimonial">', unsafe_allow_html=True)
    st.write("\"AgentAI helped our marketing team reduce content creation time by 40% while improving engagement metrics by 25%. The agents now handle our entire social media scheduling and analytics workflow.\"")
    st.write("— Sarah Chen, Marketing Director at TechGrowth")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="testimonial">', unsafe_allow_html=True)
    st.write("\"As a researcher, I needed help organizing vast amounts of scientific literature. AgentAI now curates relevant papers, summarizes findings, and even suggests connections between studies I wouldn't have considered.\"")
    st.write("— Dr. James Wilson, Neuroscience Researcher")
    st.markdown('</div>', unsafe_allow_html=True)

def pricing_section():
    st.markdown('<h2 class="section-header">Pricing Plans</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Starter")
        st.write("$19/month")
        st.write("For individuals getting started with AI assistance")
        st.markdown("""
        - 1 Specialized Agent
        - 100 Agent Actions/month
        - Basic Tool Integrations (5)
        - Email & Chat Support
        """)
        st.button("Choose Starter", key="starter_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Professional")
        st.write("$49/month")
        st.write("For professionals who need comprehensive AI support")
        st.markdown("""
        - 3 Specialized Agents
        - Unlimited Agent Actions
        - Advanced Tool Integrations (20)
        - Priority Support
        - Custom Agent Training
        """)
        st.button("Choose Professional", key="pro_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Enterprise")
        st.write("Custom Pricing")
        st.write("For teams and organizations with advanced needs")
        st.markdown("""
        - Unlimited Specialized Agents
        - Unlimited Agent Actions
        - All Tool Integrations
        - Dedicated Support Manager
        - Advanced Security & Compliance
        - On-premises Deployment Option
        """)
        st.button("Contact Sales", key="enterprise_btn")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("All plans include a 14-day free trial. No credit card required to start.")

def contact_section():
    st.markdown('<h2 class="section-header">Contact Us</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Get in Touch")
        
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=120)
        
        if st.button("Send Message"):
            if name and email and message:
                simulate_agent_thinking("Processing contact form submission", 1)
                st.success("Thank you for reaching out! Our team will contact you within 24 hours.")
            else:
                st.warning("Please fill in all required fields.")
    
    with col2:
        st.subheader("Visit Us")
        st.markdown("""
        **Headquarters**  
        123 AI Avenue, Innovation District  
        San Francisco, CA 94105
        
        **Contact Information**  
        Email: info@agentai.example.com  
        Phone: (555) 123-4567
        
        **Hours of Operation**  
        Monday - Friday: 9 AM - 6 PM PST  
        Customer Support: 24/7
        """)
        
        # Simulated map
        st.image("https://via.placeholder.com/600x300?text=Map+Location", use_column_width=True)

def footer_section():
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("AgentAI")
        st.write("Intelligent agents that understand, learn, and act on your behalf.")
    
    with col2:
        st.subheader("Links")
        st.write("[About Us](#)")
        st.write("[Careers](#)")
        st.write("[Blog](#)")
        st.write("[Documentation](#)")
    
    with col3:
        st.subheader("Legal")
        st.write("[Terms of Service](#)")
        st.write("[Privacy Policy](#)")
        st.write("[Cookie Policy](#)")
        st.write("[Security](#)")
    
    st.write("© 2025 AgentAI Technologies Inc. All rights reserved.")
    st.markdown('</div>', unsafe_allow_html=True)

# Main app
def main():
    # Navigation
    selected = create_navigation()
    
    # Content based on selection
    if selected == "Home":
        home_section()
    elif selected == "Features":
        features_section()
    elif selected == "Demo":
        demo_section()
    elif selected == "Use Cases":
        use_cases_section()
    elif selected == "Pricing":
        pricing_section()
    elif selected == "Contact":
        contact_section()
    
    # Footer (always shown)
    footer_section()

if __name__ == "__main__":
    main()