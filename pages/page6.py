import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
import plotly.graph_objects as go
from numpy.random import seed
from numpy.random import randn
import pytz

def plotly_gauge(pressure):
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = pressure,
        mode = "gauge+number+delta",
        title = {'text': "压力 - MPa"},
        delta = {'reference': 6.0},
        gauge = {'axis': {'range': [None, 8.0]},
                'steps' : [
                    {'range': [0, 3.0], 'color': "lightgray"},
                    {'range': [3.0, 6.0], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 7.9}}))

    return fig



def dataParser(resultsFile):
    sensor1_ID = 'F 0 64 D4 A 75 1 0 0 1 25 29 C 0 48'
    sensor2_ID = 'F 0 63 D3 A 43 1 0 0 8 21 29 D 0 48'
    sensor3_ID = 'F 0 59 E4 A 26 1 0 0 9 23 29 F 0 48'
    with open(resultsFile) as f:
        lines = f.readlines()
    dateTime = []
    sensor1_lines = []
    sensor2_lines = []
    sensor3_lines = []
    sensor4_lines = []
    for line in lines:
        tmp1 = line.strip('\n').split(' ')
        if tmp1[37] == '1' and tmp1[38] == '25':
            sensor1_lines.append(int(tmp1[-1]))
        elif tmp1[37] == '8' and tmp1[38] == '21':
            sensor2_lines.append(int(tmp1[-1]))
        elif tmp1[37] == '9' and tmp1[38] == '23':
            sensor3_lines.append(int(tmp1[-1]))
        else:
            dateTime.append(tmp1[0])
            sensor4_lines.append(int(tmp1[-1]))
    f.close()
    return dateTime, sensor1_lines, sensor2_lines, sensor3_lines, sensor4_lines



def serieschart_plot(dateTime, sensor1_lines, sensor2_lines, sensor3_lines, sensor4_lines):
    # plot time sereis chart
    #dtm = []
    #wl = []

    #for df in sensorSeri:
    #    dtm_tmp, wl_tmp = WEAR_DATA_PARSE(df)
    #    dtm.append(dtm_tmp)
    #    wl.append(wl_tmp)

    # wl = SMOOTH_CURVE(wl, 21)
    #np.savetxt("wearData.csv", wl, delimiter=",")
    fig2 = go.Figure()
    config = {'displayModeBar': False}
    fig2.add_trace(
        go.Scatter(x=dateTime, y=sensor1_lines,
                   line=dict(color='royalblue', width=5),
                   name="#1传感器当前厚度 - [mm]"
                   )
    )

    fig2.add_trace(
        go.Scatter(x=dateTime, y=sensor2_lines,
                   line=dict(color='coral', width=3),
                   name="#2传感器当前厚度 - [mm]"
                   )
    )

    fig2.add_trace(
        go.Scatter(x=dateTime, y=sensor3_lines,
                   line=dict(color='black', width=1),
                   name="#3传感器当前厚度 - [mm]"
                   )
    )
    
    fig2.add_trace(
        go.Scatter(x=dateTime, y=sensor4_lines,
                   line=dict(color='orange', width=1),
                   name="#4传感器当前厚度 - [mm]"
                   )
    )

    fig2.update_layout(
        xaxis_title="运行日期",
        yaxis_title="当前厚度 - [mm]",
        yaxis_range=[10, 50],
        showlegend=False,
        margin=dict(l=1, r=1, t=1, b=1),
        font=dict(
            family="sans serif, regular",
            size=11,
            color="Black"
        )
    )
    fig2.write_html("timeSeriesSensor.html", config=config)
    return

def app():

    #############################################################################
    resultsFile = "sensorData/tcp_3207.txt"
    dateTime, sensor1_lines, sensor2_lines, sensor3_lines, sensor4_lines = dataParser(resultsFile)


    ###  第一部分  模型展示  ###
    top = st.container()
    with top:
        colll1, colll3 = st.columns(2)
        with colll1:
            #st.title("长沙有色院-充填管道智能磨损在线监测系统")
            #st.title("云南驰宏锌锗-会泽矿业")
            st.title("安装工位：1398井筒")
            st.title("管道材料：会泽钢管")
            st.subheader("当前状态（在运行） ")
            installDate = date(2022, 11, 10)
            currentDate = date.today()
            deltaDays = (currentDate - installDate).days
            st.subheader("已运行时间： " + str(deltaDays) + " Days")
        with colll3:
            st.markdown("###")






    st.markdown("###")
    st.markdown("----------------------------------")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("#1磨损传感器当前状态")
        current_thickness1 = str(sensor1_lines[-1]-5) + " mm"
        delta_thickness1 = str(sensor1_lines[-1]-15) + " mm"
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness1, delta=delta_thickness1)

        #
        st.markdown("###")
        st.subheader("#2磨损传感器当前状态")
        current_thickness2 = str(sensor2_lines[-1]-5) + " mm"
        delta_thickness2 = str(sensor2_lines[-1]-15) + " mm"
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value=current_thickness2, delta=delta_thickness2)
    with col2:
        st.subheader("#3磨损传感器当前状态")
        current_thickness3 = str(sensor3_lines[-1]-5) + " mm"
        delta_thickness3 = str(sensor3_lines[-1]-15) + " mm"
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value="未安装")
        #with col4:
        st.markdown("###")
        st.subheader("#4磨损传感器当前状态")
        current_thickness4 = str(sensor4_lines[-1]-5) + " mm"
        delta_thickness4 = str(sensor4_lines[-1]-15) + " mm"
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        st.metric(label="当前磨损状态", value="未安装")
    with col3:
        # echats
        st.image('page2.png', caption='传感器安装示意图')
        
        
    st.markdown("###")
    st.markdown("###")
    #st.markdown("_______________________________________________________________________")
    col11, col22, col33 = st.columns(3)
    with col11:
        st.subheader("压力传感器当前状态")
        hktimez = pytz.timezone("Asia/Hong_Kong") 
        timenowhk = datetime.now(hktimez)
        st.markdown("最新状态时间： " + timenowhk.strftime('%Y-%m-%d %H:%M:%S'))
        seed(1)
        # generate some Gaussian values
        values = randn(1)/5
        finalV = 6.0 + values[0]
        fig = plotly_gauge(finalV)
        #HtmlFile = open("gauge_base.html", "r", encoding='utf-8')
        #source_code_2 = HtmlFile.read()
        #components.html(source_code_2, height=400)
        st.plotly_chart(fig, use_container_width=False)
        



    

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
    #st.markdown("_______________________________________________________________________")

    ###  第三部分  磨损趋势  ###
    #st.subheader("磨损历史数据")
    #serieschart_plot(dateTime, sensor1_lines, sensor2_lines, sensor3_lines, sensor4_lines)
    #HtmlFile_tSS = open("timeSeriesSensor.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS, height=600)
