import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
import plotly.graph_objects as go
#import pyecharts.options as opts
#from pyecharts.charts import Gauge
# mapbox_access_token = open(".mapbox_token").read()
#def SMOOTH_CURVE(data, window):
#    yhat = savgol_filter(data, window, 3)
#    return yhat
#def PLOT_GAUGE(Pre):#
#
#    c = (
#        Gauge(init_opts=opts.InitOpts(width = "500px", height="400px"))
#        .add("压力传感器 - MPa", [(" ", Pre)], min_=0.0, max_=10.0)
#        .set_global_opts(title_opts=opts.TitleOpts(title=""))
#        .render("gauge_base.html")
#    )#
#
#    return

def plotly_gauge(pressure):
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = pressure,
        mode = "gauge+number+delta",
        title = {'text': "压力 - MPa"},
        delta = {'reference': 3.0},
        gauge = {'axis': {'range': [None, 8.0]},
                'steps' : [
                    {'range': [0, 3.0], 'color': "lightgray"},
                    {'range': [3.0, 6.0], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 7.9}}))

    return fig


def WEAR_DATA_PARSE(wf):
    date = wf.split('.txt')[0].split('/')[-1].split('_')[0]
    # hours, minutes, secends = wf.split('.txt')[0].split('_')[1].split('-')
    hours, minutes, secends = wf.split('.txt')[0].split(date)[1].split('_')[1].split('-')
    dtm_obj = date + ' ' + hours + ':' + minutes + ':' + secends
    with open(wf) as f:
        lines = f.readlines()
    wl_obj = int(lines[9].split('\n')[0]) - 2
    ss_obj = int(lines[4].split('\n')[0])
    return dtm_obj, wl_obj, ss_obj


def main():
    st.set_page_config(page_title="有色院IoT", layout="wide", initial_sidebar_state='auto')
    st.markdown(
        f"""
            <style>
                .reportview-container .main .block-container{{
                    max-width: 1350px;
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                    padding-bottom: 1rem;
                }}

            </style>
            """,
        unsafe_allow_html=True,
    )
    #page = st.markdown(
    ##            f"""
    #            <style>
    #            .stApp {{
    #                background: url("https://kycg.s3.ap-east-1.amazonaws.com/sidebarBG.png");
    #                background-size: cover
    #            }}
    #            </style>
    #            """,
    #            unsafe_allow_html=True,
    #)

    # define files dir for all inputs
    #     cwd = os.getcwd()
    #cwd = "E:\\2项目资料\\耐普云平台demo"
    #sensorDataDir = 'UDP/'
    

    #sensorName = sensorDataDir + '*.txt'
    #sorted(glob.glob(sensorName))
    #sorted(glob.glob(sensorName), key=os.path.getmtime)
    #sensorSeri = glob.glob(sensorName)
    ##sensorSeri.sort(key=os.path.getmtime)
    #sensen1_data = []
    #sensen2_data = []
    #sensen3_data = []

    #sensen1_dt = []
    #sensen2_dt = []
    #sensen3_dt = []
    #for sss in sensorSeri:
    #    if sss != 'tmp.txt':
    #        latestDate, latestRead, sensor_label = WEAR_DATA_PARSE(sss)
    #        if sensor_label == 1:
    #            sensen1_dt.append(latestDate)
    #            sensen1_data.append(latestRead)
    #        elif sensor_label == 2:
    #            sensen2_dt.append(latestDate)
    #            sensen2_data.append(latestRead)
    #        elif sensor_label == 3:
    #            sensen3_dt.append(latestDate)
    #            sensen3_data.append(latestRead)

    #serieschart_plot(sensen1_dt, sensen1_data, sensen2_dt, sensen2_data, sensen3_dt, sensen3_data)
    #indicator_plot(latestRead)
    sensen1_data = 13
    sensen2_data = 14
    sensen3_data = 12
    sensen4_data = 12


    ###  第一部分  模型展示  ###
    top = st.container()
    with top:
        colll1, colll3 = st.columns(2)
        with colll1:
            st.title("长沙有色院-充填管道智能磨损在线监测系统")
            st.title("云南驰宏锌锗-会泽矿业")
            st.subheader("当前状态（在运行） ")
        with colll3:
            st.markdown("###")
            st.image("bradken.png")






    st.markdown("###")
    st.markdown("----------------------------------")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("#1磨损传感器当前状态")
        current_thickness1 = str(sensen1_data) + " mm"
        delta_thickness1 = str(sensen1_data-15) + " mm"
        st.markdown("最新状态时间： " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness1, delta=delta_thickness1)

        #
        st.markdown("###")
        st.subheader("#2磨损传感器当前状态")
        current_thickness2 = str(sensen2_data) + " mm"
        delta_thickness2 = str(sensen2_data-15) + " mm"
        st.markdown("最新状态时间：" + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness2, delta=delta_thickness2)
    with col2:
        st.subheader("#3磨损传感器当前状态")
        current_thickness3 = str(sensen3_data) + " mm"
        delta_thickness3 = str(sensen3_data-15) + " mm"
        st.markdown("最新状态时间：" + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness3, delta=delta_thickness3)
        #with col4:
        st.markdown("###")
        st.subheader("#4磨损传感器当前状态")
        current_thickness4 = str(sensen4_data) + " mm"
        delta_thickness4 = str(sensen3_data-15) + " mm"
        st.markdown("最新状态时间：" + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness4, delta=delta_thickness4)
    with col3:
        # echats
        fig = plotly_gauge(3.4)
        #HtmlFile = open("gauge_base.html", "r", encoding='utf-8')
        #source_code_2 = HtmlFile.read()
        #components.html(source_code_2, height=400)
        st.plotly_chart(fig, use_container_width=True)
        
    
    
    installDate = date(2022, 8, 10)
    currentDate = date.today()
    deltaDays = (currentDate - installDate).days
    st.subheader("已运行时间： " + str(deltaDays) + " Days")
    st.markdown("_______________________________________________________________________")
    #pyLogo = Image.open("install.png")
    st.subheader("传感器安装示意三维")
    #HtmlFile_tSS1 = open("dexxxing.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS1, height=500)
    #imgcol1, imgcol2, imgcol3 = st.columns(3)
    #with imgcol1:
    ##im1 = Image.open("install.png")
    #st.image(im1)
    #with imgcol2:
    #    im2 = Image.open("photos/image2.jpg")
    #    st.image(im2)
    #with imgcol3:
    #    im3 = Image.open("photos/image3.jpg")
    #    st.image(im3)
    #@st.cache
    iframeLINK = "https://dexing-pump-nzjah350-7b9d991d6fe-1306024390.tcloudbaseapp.com/huize.html"
    st.write(
            f'<iframe src=' + iframeLINK + ' height = "1000" width = "100%"></iframe>',
            unsafe_allow_html=True,
    )
    st.markdown("_______________________________________________________________________")

    ###  第三部分  磨损趋势  ###
    st.subheader("磨损历史数据")
    HtmlFile_tSS = open("timeSeriesSensor.html", 'r', encoding='utf-8').read()
    components.html(HtmlFile_tSS, height=600)

if __name__ == "__main__":
    main()











