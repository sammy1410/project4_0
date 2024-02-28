from utility.shared import this
import os
import streamlit as st
import page.Contact_us as Contact,page.Home as Home, page.product as product,page.SCADA as SCADA
import page.SignIn as SignIn,page.SignUp as SignUp
import page.accountInfo as accountInfo

pages = {
    "Home": Home,
    "Contact": Contact,
    "Product": product,
    "SCADA": SCADA,
    "My Account": accountInfo,
    "Sign In": SignIn,
    "Sign Up": SignUp
}


def change_page(pageName):
    print(f"Change Page: {pageName}")
    this.pageName=pageName
    
def logout():
    del this.user_session
    del this.user
    change_page("Home")

def showNavMenu():
    st.image("./images/WebBanner.png",use_column_width=True)
    page_name=list(pages.keys())
    page_name.remove("Sign Up")
    page_name.remove("SCADA")
    pageNo = len(page_name)
    columns = st.columns(pageNo)
    if "user" in this:
        page_name.remove("Sign In")
        st.button("Logout",on_click=logout)
    else:
        page_name.remove("My Account")
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