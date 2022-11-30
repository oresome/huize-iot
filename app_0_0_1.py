# coding=utf-8
import streamlit as st
from multipage import MultiPage
from pages import page1, page2, page3, page4, page5, page6

MAGE_EMOJI_URL = "streamlitBKN.png"
st.set_page_config(page_title='长沙有色IoT',page_icon=MAGE_EMOJI_URL, initial_sidebar_state = 'auto', layout="wide")
#page_icon = favicon,
st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 1600px;
                padding-top: 1rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 1rem;
            }}

            .fullScreenFrame > div {{
                display: flex;
                justify-content: left;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

app = MultiPage()

# add applications
app.add_page('📘  1764斜坡道287号-POE耐磨管', page1.app)
app.add_page('📕  1764转弯口-POE耐磨管', page2.app)
app.add_page('📗  1764充填井连道口-POE耐磨管', page3.app)
app.add_page('📔  1764斜坡道288号-钢管', page4.app)
app.add_page('📒  1404井口-钢管', page5.app)
app.add_page('📙  1398井筒-钢管', page6.app)

# Run application
if __name__ == '__main__':
    app.run()
