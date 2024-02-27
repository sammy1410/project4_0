from utility.shared import this
import os
import streamlit as st
import page.Contact_us as Contact,page.Home as Home, page.product as product,page.SCADA as SCADA
import page.login as login
pages = {
    "Home": Home,
    "Contact": Contact,
    "Product": product,
    "SCADA": SCADA,
    "Login": login
}


def change_page(pageName):
    print(f"Change Page: {pageName}")
    this.pageName=pageName
    
def logout():
    del this.user
    change_page("Home")

def showNavMenu():
    st.image("./images/WebBanner.png",use_column_width=True)
    pageNo = len(pages.keys())
    columns = st.columns(pageNo)
    page_name=list(pages.keys())
    if "user" in this:
        page_name.remove("Login")
        st.button("Logout",on_click=logout)
    else:
        page_name.remove("SCADA")
    page_name.remove("Product")
    for col,page_ in zip(columns,page_name):
        with col:
            st.button(page_,on_click=change_page,args=(page_,),key=page_)
    st.write("________________________________")

if "page" not in this:
    this.pageName="Home"
    this.page = pages[this.pageName]
    showNavMenu()
    this.page.layout()
else:
    if not this.pageName == "SCADA":
        showNavMenu()
    this.page = pages[this.pageName]
    this.page.layout()