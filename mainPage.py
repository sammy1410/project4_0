from utility.shared import this
import os
import streamlit as st
import page.Contact_us as Contact,page.Home as Home, page.product as product,page.SCADA as SCADA
import page.SignIn as SignIn,page.SignUp as SignUp
import page.accountInfo as accountInfo,page.Admin_page as Admin
import page.addProduct as New_Product
import page.addUser as New_User

admin_pages = {
    "Admin": Admin,
    "Product": product,
    "SCADA": SCADA,
    "My Account": accountInfo,
    "New_Product":New_Product,
    "New_User" : New_User
}

user_pages = {
    "Home": Home,
    "Contact": Contact,
    "Product": product,
    "My Account": accountInfo,
}

guest_pages = {
    "Home": Home,
    "Contact": Contact,
    "Product": product,
    "Sign In": SignIn,
    "Sign Up":SignUp
}

def change_page(pageName):
    print(f"Change Page: {pageName}")
    this.pageName=pageName
    
def logout():
    del this.user_session
    del this.user
    change_page("Home")

def showAdminNavMenu():
    st.image("./images/WebBanner.png",use_column_width=True)
    page_name=list(admin_pages.keys())
    page_name.remove("Product")
    page_name.remove("New_Product")

    pageNo = len(page_name)
    columns = st.columns(pageNo)
    
    st.button("Logout",on_click=logout)
    for col,page_ in zip(columns,page_name):
        with col:
            st.button(page_,on_click=change_page,args=(page_,),key=page_)
    st.write("________________________________")

def showUserNavMenu():
    st.image("./images/WebBanner.png",use_column_width=True)
    page_name=list(user_pages.keys())
    page_name.remove("Product")

    pageNo = len(page_name)
    columns = st.columns(pageNo)
    st.button("Logout",on_click=logout)    
    for col,page_ in zip(columns,page_name):
        with col:
            st.button(page_,on_click=change_page,args=(page_,),key=page_)
    st.write("________________________________")

def showGuestNavMenu():
    st.image("./images/WebBanner.png",use_column_width=True)
    page_name=list(guest_pages.keys())
    page_name.remove("Product")
    page_name.remove("Sign Up")
    pageNo = len(page_name)
    columns = st.columns(pageNo)
    
    for col,page_ in zip(columns,page_name):
        with col:
            st.button(page_,on_click=change_page,args=(page_,),key=page_)
    st.write("________________________________")

if "page" not in this:
    this.pageName="Home"
    this.page = guest_pages[this.pageName]
    showGuestNavMenu()
    this.page.layout()
else:
    if "user_session" in this:
        if this.user_session["access"] == "Admin":
            if this.pageName != "SCADA":
                showAdminNavMenu()
            #this.page = admin_pages[this.pageName]
            try:
                this.page = admin_pages[this.pageName]
            except:
                pass
        else:
            showUserNavMenu()    
            this.page = user_pages[this.pageName]
    else:
        showGuestNavMenu()
        this.page = guest_pages[this.pageName]
    
    this.page.layout()