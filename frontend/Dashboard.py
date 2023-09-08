import streamlit as st
from api_requests import Request
import os
from PIL import Image
from st_pages import Page, show_pages

# CONFIG
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
)

show_pages(
    [
        Page("Dashboard.py", "Dashboard"),
    ]
)


# CONFIG

# METHODS

def products():
    list_of_products = Request.get_findings()
    return list_of_products


def selected_category(category_chosen):
    categories_dict = {
        "TECH": 0,
        "EBOOK": 1,
        "ON_COURSE": 2,
        "OTHER": 3,
    }
    category_index = categories_dict.get(category_chosen)
    return category_index


# METHODS

# STATICS

new_finding = {}

categories = {"Tech": "TECH",
              "Ebook": "EBOOK",
              "Online course": "ON_COURSE",
              "Other": "OTHER",
              }
no_picture = Image.open('static/no-picture.png')

products = products()

# STATICS

st.title("Dashboard")
st.divider()
col1, col2 = st.columns(2)
with col1:
    with st.expander("Add New Finding", expanded=True):
        with st.form("my_new_finding", clear_on_submit=True):
            name = st.text_input("Your finding name")
            price = st.number_input("Price")
            content = st.text_area("Talk a little bit about it")
            category = st.selectbox("Select a category", ["Tech", "Ebook", "Online course", "Other"])
            link = st.text_input("Place the link of your finding")
            picture = st.file_uploader("Upload a picture")

            submitted = st.form_submit_button("Submit")

            if submitted:
                with st.spinner('Wait for it...'):
                    if picture:
                        with open(os.path.join("temp/", picture.name), "wb") as f:
                            f.write(picture.getbuffer())
                    new_finding["name"] = name
                    new_finding["price"] = price
                    new_finding["content"] = content
                    new_finding["category"] = categories.get(category)
                    new_finding["link"] = link
                    new_finding["picture_name"] = picture.name if picture else None

                    post_request = Request.post_new_finding(payload=new_finding)
                    if post_request == 201:
                        st.experimental_rerun()
                    else:
                        st.error('Something went wrong')

with col2:
    if len(products):
        for p in products:
            with st.expander(p['name']):
                with st.form(f"findings{p['pk']}"):
                    st.image(p['picture'] if p['picture'] else no_picture)
                    name = st.text_input("Name", p['name'])
                    price = st.number_input("Price", float(p['price']))
                    content = st.text_area("Talk a little bit about it", p['content'])
                    category = st.selectbox("Select a category", ["Tech", "Ebook", "Online course", "Other"],
                                            index=selected_category(p['category']))
                    link = st.text_input("The link of your finding", p['link'])
                    picture = st.file_uploader("Edit picture")
                    submitted = st.form_submit_button("Edit")
                    delete = st.form_submit_button(label='Delete', type="primary")
                    if submitted:
                        with st.spinner('Wait for it...'):
                            if picture:
                                with open(os.path.join("temp/", picture.name), "wb") as f:
                                    f.write(picture.getbuffer())
                            new_finding["name"] = name
                            new_finding["price"] = price
                            new_finding["content"] = content
                            new_finding["category"] = categories.get(category)
                            new_finding["link"] = link
                            new_finding["picture_name"] = picture.name if picture else None

                            put_request = Request.update_finding(payload=new_finding, finding_id=int(p['pk']))
                            if put_request == 200:
                                st.experimental_rerun()
                            else:
                                st.error('Something went wrong')
                    if delete:
                        delete_request = Request.delete_finding(finding_id=int(p['pk']))
                        if delete_request == 204:
                            st.experimental_rerun()
                        else:
                            st.error('Something went wrong')
    else:
        st.write("You don't have any findings so far.")
