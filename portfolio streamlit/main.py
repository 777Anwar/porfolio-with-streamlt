from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# lottie
st.set_page_config(page_title="My Webpage", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")


# ---- LOAD ASSETS ----

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_coding1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tfb3estd.json")
img = Image.open("image1.png")
img3 = Image.open("C:/Users/hp/Desktop/port/image2.png.png")

SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}




# - HEADER 

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write("##")


with st.container():
    left_column, right_column = st.columns((2))
    with left_column:
        st.subheader("Hi, I am ANWAR BOUIKHEF :wave:")
        st.title("A Developper web")
        st.write("""
     
<div>
    <div style="width: 80%;">
        <h5 style="color: #FF0000 ; font-family: Elppa;">"Hello, I'm ANWAR and I'm a skilled and passionate web developer. I have extensive experience in developing websites using technologies such as HTML, CSS, and Python.
            I stay up-to-date with the latest web development trends and techniques to ensure that my clients receive the best results possible. 
            I approach challenges with creativity and am always seeking new opportunities to improve as a developer. Effective communication and collaboration are also key strengths of mine, and I thrive in team environments where I can share my knowledge and learn from others.
            If you're in need of a talented and dedicated web developer to bring your vision to life, I'd be thrilled to work with you. Let's work together to create something truly amazing!"
        </h5>
    </div>
</div>
   
""", unsafe_allow_html=True)
st.write("[Learn More >](https://blog.openclassrooms.com/en/2018/03/28/web-development-definition/)")
with right_column:
             st_lottie(lottie_coding1, height=400)



#WHAT I DO 


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
            - ✔️ Building websites with HTML and CSS
            - ✔️ Building Websites with PYTHON AND FRAMWORKS
            - ✔️ I study more in this field to be perfect
            - ✔️ I stay up-to-date with the latest web development
           
            """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# PROJECTS 
with st.container():
    st.write("---")
    st.header("My Skills")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img)
    with text_column:
         st.subheader("HTML&CSS DEVELOPER")
         st.write(
            """
            I am a skilled web developer with a passion for creating visually stunning and functional websites. With my expertise in HTML and CSS, I am able to bring your designs to life and create an online presence that truly represents your brand. My attention to detail and commitment to delivering top-notch results make me an asset to any project.
            """
        )
        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("PYTHON DEVELOPER")
        st.write(
            """
            "As a proficient Python developer, I bring a wealth of experience and expertise to building high-quality and efficient applications. Whether you're looking for a simple website or a complex system, I have the skills and knowledge necessary to deliver the best possible results. With a deep understanding of Python programming and its various libraries and frameworks, I am well-equipped to tackle even the most challenging projects. So if you're looking for a reliable and skilled Python developer to bring your ideas to life, I'm here to help."
            """
        )


st.write("---")

st.header("Contact Me")
st.write("##")

       

#contact


contact_form = """
<style>
    form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: absolute;
        bottom: 1;
        left: 0;
        right: 0;
        margin: auto;
    }
</style>
    
<form action="https://formsubmit.co/bouikhefanwar2001@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)



