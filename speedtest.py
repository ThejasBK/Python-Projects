#This program calculates the internet speed

import speedtest
import streamlit as stl
st = speedtest.Speedtest()

def download_speed():
    stl.text('Download speed of your internet: {:.2f}'.format(st.download() / (1024*1024)) + ' mbps')

def upload_speed():
    stl.text('Upload speed of your internet: {:.2f}'.format(st.upload() / (1024*1024)) + ' mbps')
    
def latency():
    servernames = []
    st.get_servers(servernames)
    stl.text('Delay of your internet(ping): '+'{}'.format(st.results.ping)+'ms')
    print(st.results.ping)

button1 = stl.button('Download Speed')
button2 = stl.button('Upload Speed')
button3 = stl.button('Internet latency(ping)')

if button1:
    download_speed()

if button2:
    upload_speed()

if button3:
    latency()
