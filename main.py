import streamlit as st
import langchain_helper

# --- Component: Logo and Title ---
def render_header():
    st.markdown(
        """
        <style>
        body, .stApp { background: #0F172A !important; }  /* Deep navy background */
        
        .header-title {
            font-size: 2.5rem;
            font-weight: 900;
            color: #FACC15; /* Golden accent */
            letter-spacing: 1.5px;
            margin-bottom: 0.3rem;
        }
        .header-sub {
            color: #38BDF8; /* Sky blue highlight */
            font-size: 1.15rem;
            font-weight: 500;
        }
        .header-wrap {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            padding: 1.5rem 2rem 1.2rem 1.2rem;
        }
        .header-logo {
            border-radius: 50%;
            box-shadow: 0 2px 16px rgba(250,204,21,0.4);
            width: 70px;
            height: 70px;
            object-fit: cover;
            background: #1A1A1A;
            border: 2px solid #FACC15;
        }
        .main-content {
            background: linear-gradient(135deg, #1A1A1A 0%, #232526 100%);
            border-radius: 20px;
            padding: 2.2rem 2.5rem 2.5rem 2.5rem;
            margin: 0 auto 2rem auto;
            max-width: 1000px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.45);
        }
        h4 {
            font-family: 'Segoe UI', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns([0.13, 0.87])
    with cols[0]:
        st.image('Logo.png', width=90)
    with cols[1]:
        st.markdown("""
            <div class='header-title'>Restaurant Name Generator</div>
            <div class='header-sub'>Get a creative restaurant name and menu based on your favorite cuisine!</div>
        """, unsafe_allow_html=True)


# --- Component: Cuisine Selector ---
def cuisine_selector():
    return st.selectbox(
        "Pick a Cuisine",
        ("Indian", "Italian", "Mexican", "Arabic", "American", "Chinese", "French", "Japanese", "Mediterranean", "Thai"),
        index=0,
        key="cuisine_select"
    )

# --- Component: Restaurant Name and Menu ---
def render_suggestion(response):
    st.markdown(
        f"<h4 style='color:#FACC15; margin-top:1.5rem; font-weight:800;'>{response['restaurant_name'].strip()}</h4>",
        unsafe_allow_html=True
    )

    menu_items = [item.strip() for item in response['menu_items'].strip().split(",") if item.strip()]
    st.markdown("<h4 style='margin-top:1rem; color:#38BDF8;'>Menu Items</h4>", unsafe_allow_html=True)

    for item in menu_items:
        st.markdown(
            f"""
            <div style='
                background:linear-gradient(90deg,#232526 0%,#414345 100%);
                border-radius:10px;
                padding:0.6rem 1rem;
                margin-bottom:0.6rem;
                display:flex;
                align-items:center;
                gap:0.6rem;
                font-size:1.1rem;
                color:#F8FAFC;
                box-shadow:0 3px 12px rgba(250,204,21,0.25);'>
                🍴 <span style='color:#FACC15;'>{item}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Main Layout ---
render_header()


cuisine = cuisine_selector()

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    render_suggestion(response)

st.markdown("</div>", unsafe_allow_html=True)
