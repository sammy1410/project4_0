import streamlit as st
import time

this = st.session_state

def change_page(page):
    this.pageName=page
    print(f"Change Page: {this.pageName}")

def file_name(file):
    dot_index = file.rfind(".")
    
    if dot_index != -1:
        file_name_without_ext = file[:dot_index]
        return file_name_without_ext
    else:
        return file
    
def usleep(micro):
    start_time = time.perf_counter()
    while ( time.perf_counter()-start_time ) < (micro/1_000_000):
        pass

