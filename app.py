from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My website", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        st.warning(f"CSS file not found at path: {file_path}")
        return ""

# Specify the correct file path for your CSS file
css_file_path = "style/style.css"

# Read the CSS file content
css_content = local_css(css_file_path)

# Apply the CSS styles
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        {css_content}
    </style>
""", unsafe_allow_html=True)

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/36853ef1-8d93-4513-9431-7da39c5dfb67/8plGXL88xC.json")
lottie_Man = load_lottieurl("https://lottie.host/f0d22d59-0e35-4bcb-ad52-3ddb2e9550d9/RywyFDumVc.json")
img_verse = Image.open("images/verse.png")
img_intro = Image.open("images/intro.png")

# Sidebar menu
menu_options = ["Home", "What Huawei Offers", "All About Huawei", "Get In Touch"]
selected_menu = st.sidebar.selectbox("Home", menu_options)

# ---- HEADER SECTION ----
if selected_menu == "Home":
    st.subheader('Hi, I am Daryl D. Silva :wave:', divider='rainbow')
    st.title("Huawei: Connecting the World through Innovation")
    st.write(
        "Welcome to Huawei, a global leader in technology and innovation, connecting people and societies across the world. With a commitment to building a fully connected, intelligent world, Huawei is at the forefront of transforming industries, empowering individuals, and driving positive change."
    )

# ---- WHAT HUAWEI OFFERS ----
elif selected_menu == "What Huawei Offers":
     # Create a Streamlit column layout
    col1, col2 = st.columns([2, 1])

    # Use the first column for content (text)
    with col1:
      st.write("---")
      st.header("What Huawei Can Offer?", divider='rainbow')
      st.write("##")
        st.write(
        """
        - Smartphones: Huawei is well-known for its smartphones, including the Huawei P and Mate series, which often feature advanced camera systems and high-performance hardware.

        - Tablets: Huawei produces tablets like the Huawei MatePad series, offering a range of options for different user needs.

        - Laptops: Huawei has a line of laptops, such as the Huawei MateBook series, which combines sleek design with powerful hardware.

        - Wearables: Huawei offers smartwatches and fitness trackers under its Huawei Watch and Huawei Band series.

        - Networking Equipment: Huawei is a major player in the telecommunications industry, providing networking solutions, including routers and switches.

        - 5G Infrastructure: Huawei is a significant contributor to the development and implementation of 5G technology globally.

        - Audio Products: Huawei produces audio devices like headphones, earphones, and speakers under the Huawei FreeBuds and Sound X series.

        - Smart Home Devices: Huawei offers smart home products, including smart speakers, cameras, and other connected devices.

        - Cloud Services: Huawei provides cloud computing services, including storage, computing power, and AI services, through its Huawei Cloud platform.

        - Software Solutions: In addition to hardware, Huawei develops software solutions, including its EMUI (Emotion UI) for smartphones and other software applications.

        """
    )

    # Use the second column for the Lottie animation on the right side
    with col2:
          st_lottie(lottie_coding, height=800, key="coding")
        pass

# ---- ALL ABOUT HUAWEI ----
elif selected_menu == "All About Huawei":
    st.write("---")
    st.header("All About Huawei", divider='rainbow')
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_verse)
    with text_column:
        st.subheader("History of Huawei")
        st.write(
            """
           The history of Huawei 1987-2022 is the subject of today's video. So, the time has come for a new journey in the history of one of the most appreciated companies in the world, Huawei. Huawei's story began 35 years ago, when Ren Zhengfei, Huawei, started as a rural agent for selling telephone and cable services. Huawei is now a telecommunications and electronics giant and competes with big companies such as Apple, Samsung and Xiaomi. 

            """
        )
        st.markdown("[History OF Huawei](https://www.youtube.com/watch?v=fgbwdTcN-E8&t=49s)")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_intro)
    with text_column:
        st.subheader("Product Of Huawei")
        st.write(
            """
           Huawei's innovative smartphones redefine the boundaries of technology, seamlessly blending cutting-edge design with unmatched performance. With state-of-the-art camera systems, Huawei devices capture moments with breathtaking clarity and detail, empowering users to unleash their creativity. The sleek and sophisticated aesthetics of Huawei products reflect a commitment to elegance and functionality, making each device a statement of style. Boasting powerful processors and long-lasting battery life, Huawei smartphones ensure a seamless and efficient user experience, whether for work or play. In a rapidly evolving tech landscape, Huawei stands as a beacon of ingenuity, consistently delivering products that elevate the user experience to unprecedented heights.
            """
        )
        st.markdown("[For more info about Huawei Products](https://consumer.huawei.com/ph/)")

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
