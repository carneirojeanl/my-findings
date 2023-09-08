import streamlit as st
import webbrowser
from api_requests import Request

st.set_page_config(
    page_title="Client",
)


def products():
    list_of_products = Request.get_findings()
    return list_of_products


def open_url(url):
    webbrowser.open(url)


search_value = st.text_input(label="Search Bar", placeholder="Search for a Finding", label_visibility="hidden")
st.write("#")
if not search_value:
    for p in products():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.image(p['picture'], use_column_width=True, caption=p['content'])

            with col2:
                st.subheader(p['name'])
                visit = st.button(label="Visit Page", key=f"buttonKey{p['pk']}")
                if visit:
                    open_url(p['link'])
        st.divider()
else:
    for p in products():
        if search_value in p['name'] or search_value in p['name'].lower():
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.image(p['picture'], use_column_width=True, caption=p['content'])

                with col2:
                    st.subheader(p['name'])
                    visit = st.button(label="Visit Page", key=f"buttonKey{p['pk']}")
                    if visit:
                        open_url(p['link'])
            st.divider()


