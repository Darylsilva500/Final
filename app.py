from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My website", page_icon=":tada:", layout="wide")

# Define your profile picture URL
profile_picture_url = "https://github.com/Darylsilva500/Final/blob/main/images/user.png"

# Load the profile picture
profile_picture = Image.open(requests.get(profile_picture_url, stream=True).raw)

# Sidebar background image
sidebar_bg_image_url = "https://github.com/Darylsilva500/Final/blob/main/images/background1.jpg"

# Load the background image
sidebar_bg_image = Image.open(requests.get(sidebar_bg_image_url, stream=True).raw)

# Set sidebar width and background image
st.markdown(
    f"""
    <style>
        .sidebar .sidebar-content {{
            width: 300px;
            background-image: url("{sidebar_bg_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            padding-top: 20px;
        }}
        .sidebar .sidebar-content .stImage {{
            border-radius: 50%;
            margin-bottom: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
menu_options = ["Home", "What Huawei Offers", "All About Huawei", "Get In Touch"]
selected_menu = st.sidebar.selectbox("Home", menu_options)

# Profile picture and username at the top of the sidebar
st.sidebar.image(profile_picture, use_column_width=True, caption="Your Name")
st.sidebar.markdown("---")

# ---- HEADER SECTION ----
if selected_menu == "Home":
    st.subheader('Hi, I am Daryl D. Silva :wave:', divider='rainbow')
    st.title("Huawei: Connecting the World through Innovation")
    st.write(
        "Welcome to Huawei, a global leader in technology and innovation, connecting people and societies across the world. With a commitment to building a fully connected, intelligent world, Huawei is at the forefront of transforming industries, empowering individuals, and driving positive change."
    )

# ---- WHAT HUAWEI OFFERS ----
elif selected_menu == "What Huawei Offers":
    st.write("---")
    st.header("What Huawei Can Offer?", divider='rainbow')
    st.write("##")
    st.write(
        """
        - Smartphones: Huawei is well-known for its smartphones, including the Huawei P and Mate series, which often feature advanced camera systems and high-performance hardware.
        
        ... (rest of your code)
        """
    )
    st_lottie(lottie_coding, height=800, key="coding")

# ---- ALL ABOUT HUAWEI ----
elif selected_menu == "All About Huawei":
    st.write("---")
    st.header("All About Huawei", divider='rainbow')
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    

# ---- GET IN TOUCH ----
elif selected_menu == "Get In Touch":
    st.write("---")
    st.header("Get In Touch With Me!", divider='rainbow')
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/thelaststand500@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 
    with right_column:
        st_lottie(lottie_Man, height=400, key="Man")
