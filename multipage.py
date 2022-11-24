# coding=utf-8
import streamlit as st

#lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_9asbexx5.json")
#key1="hello"+str(random())

class MultiPage:
    """Framework for combining multiple streamlit applications
    """
    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func):
        self.pages.append(
            {
            'title': title,
            'function': func
            }
        )
    
    def run(self):
        #st.sidebar.title("Grind Master")
        page = st.sidebar.image("bradken.png")
        #page = st.sidebar.title("Bradken OptiGrind")
        page = st.sidebar.markdown("###")
        intro = '<p style="color:Black; font-size: 22px; font-weight: bold;">充填管道智能磨损在线监测系统</p>'
        page = st.sidebar.markdown(intro, unsafe_allow_html=True)
        #page = st.sidebar.title("长沙有色院")
        #page = st.sidebar.title("充填管道智能磨损在线监测系统")
        page = st.sidebar.title("云南驰宏锌锗-会泽矿业")
        page = st.sidebar.selectbox(
            '请选择安装地点：', 
            self.pages,
            format_func=lambda page: page['title']  # Function to modify the display of the labels.

        )
        page['function']()