import streamlit as st

# Set page config
st.set_page_config(page_title="Cumulonimbus", layout="wide")

# Header and main welcome content
st.markdown(
    """
    <div class="header">
        <div class="nav-links-logo">
            <a href="#home">Cumulonimbus</a>
        </div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about-us">About Us</a>
            <a href="#contact-us">Contact Us</a>
        </div>
    </div>
    
    <div class="full-page">
        <h1>Welcome</h1>
        <p>We are Cumulonimbus, a software agency based in Nairobi, Kenya.</p>
        <p>We specialise in Enterprise Content Management Platform.</p>
        <p>We support your applications as if they were our own.</p>
        <p>We review every line of code and closely vet technical integrations. Our clients tell us that the standards
           we introduce bring confidence and creative freedom to their developers, trust to leadership, and
           efficiency and order to their pipelines.</p>
        <a href="#services" class="btn">LEARN MORE ABOUT US AND OUR SERVICES</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# New Section before Services
st.markdown(
    """
    <div class="intro-section">
        <h2>Our Commitment</h2>
        <div class="intro-content">
            <p>At Cumulonimbus, we are committed to delivering unparalleled solutions that drive success. With a focus on innovation, security, and performance, our team is dedicated to ensuring your digital assets are managed and optimized to their full potential. Our goal is to provide you with the confidence and peace of mind to focus on what you do best—creating amazing digital experiences.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Services section
st.markdown(
    """
    <div class="services-section">
        <h2>Services</h2>
        <div class="service">
            <img src="https://shoreditchdemo.wordpress.com/wp-content/uploads/2018/05/icon-managed-hosting.png" alt="Managed Hosting Icon">
            <div class="service-content">
                <h3>Managed Hosting</h3>
                <p>Cumulonimbus uses its own software, Shorehost, a fully managed cloud platform for unparalleled scale, security, flexibility, and performance. Optimized to make your site shine, every day.</p>
            </div>
        </div>
        <div class="service">
            <img src="https://shoreditchdemo.wordpress.com/wp-content/uploads/2018/05/icon-implementation-support.png" alt="Implementation and Support Icon">
            <div class="service-content">
                <h3>Implementation and Support</h3>
                <p>End-to-end guidance and hands-on support, from project consideration through launch and every day thereafter. We offer expert guidance and hands-on partnership every step of the way.</p>
            </div>
        </div>
        <div class="service">
            <img src="https://shoreditchdemo.wordpress.com/wp-content/uploads/2018/05/icon-build-digital-experiences.png" alt="Build Your Digital Experiences Icon">
            <div class="service-content">
                <h3>Build Your Digital Experiences</h3>
                <p>Solutions at the ready. Shorehost powers mission-critical enterprise media and marketing systems. It can serve as the entire backbone or a key component of your digital content management infrastructure.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Testimonials section
st.markdown(
    """
    <div class="testimonials-section">
        <h2>Testimonials</h2>
        <div class="testimonial-wrapper">
            <div class="testimonial">
                <p>We just love Cumulonimbus. It has been incredibly efficient to work with Cumulonimbus and their team of developers.</p>
                <p>— Anthony – Cloudup</p>
                <img src="https://shoreditchdemo.wordpress.com/wp-content/uploads/2016/04/cloudup-logo.jpg?w=150" alt="Cloudup Logo">
            </div>
            <div class="testimonial">
                <p>With Cumulonimbus, things like security we no longer have to think about. This allows our team to focus on building awesome stuff!</p>
                <p>— Megan – WooCommerce</p>
                <img src="https://shoreditchdemo.wordpress.com/wp-content/uploads/2016/04/woo-logo.jpg?w=150" alt="WooCommerce Logo">
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Ready to get started section
st.markdown(
    """
    <div class="ready-section">
        <h2>Ready to get started?</h2>
        <p>No matter where you are in the planning process, we're happy to help, and we're actual humans here on the other side of the form.</p>
        <p>We're here to discuss your challenges and plans, evaluate your existing resources or a potential partner, or even make some initial recommendations. And, of course, we're here to help any time you're in the market for some robust WordPress awesomeness.</p>
        <a href="mailto:contact@shoreditch.com" class="btn">DROP US A NOTE</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# CSS to style the header, background, overlay text, and new sections
st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 10px 50px;
        box-shadow: 0px 4px 2px -2px gray;
    }
    .header img {
        width: 150px;
    }
    .nav-links a {
        margin-right: 20px;
        color: black;
        text-decoration: none;
        font-size: 0.8em;
    }
    .nav-links a:hover {
        text-decoration: underline;
    }

    .nav-links-logo a {
        # font-weight: bold;
        text-decoration: none;
        font-size: 1.5em;
        color: #e8ba11;
        font-family: "Gill Sans Extrabold", cursive;
    }
    .nav-links-logo a:hover {
        text-decoration: underline;
    }

    .full-page {
        background-size: cover;
        padding: 50px;
        text-align: center;
        color: white;
        # font-family: 'Arial', sans-serif;
        font-size: 0.8em;
    }
    .full-page h1 {
        font-size: 3em;
        margin-bottom: 20px;
        color: white;
    }
    .full-page p {
        font-size: 1.2em;
        margin-bottom: 20px;
    }
    .btn {
        background-color: transparent;
        border: 2px solid white;
        color: white;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        text-decoration: none;
        border-radius: 5px;
    }
    .btn:hover {
        background-color: white;
        color: black;
    }
    .intro-section {
        background-image: url('/mnt/data/image.png');
        background-size: cover;
        padding: 50px;
        color: blue;
        
    }
    .intro-section h2 {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .intro-content {
        max-width: 800px;
        margin: 0 auto;
        font-size: 1.2em;
        text-align: center;
    }
    .services-section {
        background-image: url('/mnt/data/image.png');
        background-size: cover;
        padding: 50px;
        color: white;
        text-align: center;
        background-color: gray;
    }
    .services-section h2 {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 50px;
        color: white;
    }
    .service {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 40px;
        text-align: center;
    }
    .service img {
        width: 100px;
        height: 100px;
        margin-right: 20px;
    }
    .service-content {
        max-width: 600px;
        text-align: left;
    }
    .service-content h3 {
        font-size: 1.5em;
        margin-bottom: 10px;
        color: white;
    }
    .service-content p {
        font-size: 1.1em;
        text-align: left;
    }
    .testimonials-section {
        padding: 50px;
        text-align: center;
        background-color: white;
        color: black;
    }
    .testimonials-section h2 {
        font-size: 2.5em;
        margin-bottom: 50px;
    }
    .testimonial-wrapper {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .testimonial {
        display: inline-block;
        width: 45%;
        background-color: #f9f9f9;
        padding: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .testimonial img {
        width: 50px;
        height: 50px;
    }
    .ready-section {
        background-color: #3572D3;
        color: white;
        padding: 50px;
        text-align: center;
    }
    .ready-section h2 {
        font-size: 2.5em;
        margin-bottom: 20px;
        color: white;s
    }
    .ready-section p {
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .ready-section .btn {
        background-color: white;
        color: #3572D3;
        border: 2px solid white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
    }
    .ready-section .btn:hover {
        background-color: #285b9b;
        color: white;
    }
    /* Change the background color of the main content area */
    .stApp .full-page {
        background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
        background-size: cover
    }
    #MainMenu, header, footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Build responsive apps based on different screen features
from st_screen_stats import ScreenData, WindowQuerySize, WindowQueryHelper

helper_screen_stats = WindowQueryHelper()

def onScreenSizeChange(updated_screen, component_function_):

    st.session_state[updated_screen] = st.session_state[component_function_]

if "large_screen_size_" not in st.session_state:
    st.session_state["large_screen_size_"] = helper_screen_stats.window_range_width(min_width=1000, max_width=1100, key="lg_screen")
else:
    helper_screen_stats.window_range_width(min_width=1000, max_width=1100, on_change=onScreenSizeChange, args=("large_screen_size_", "lg_screen_post_first_mount"), key="lg_screen_post_first_mount")

if st.session_state["large_screen_size_"]["status"]:
    st.write("rest of code here")

# Also works for `ScreenData` and `WindowQuerySize` classes