import streamlit as st
import requests as rq
import pandas as pd

api_key = st.text_input("Neon API Key", type="password")

if api_key:
    url = "https://console.neon.tech/api/v2/projects?limit=10"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + api_key
    }

    st.title("Neon MiniDash")
    data = rq.get(url,headers=headers).json()
    df = pd.DataFrame(data["projects"])

    # You could do a sidebar here... 
    # st.sidebar.header("Projects")
    # for project in df.id:
    #     st.sidebar.button(project)

    projects = st.selectbox("Select a project", df.id, placeholder="Select a project or view to query ...")

    if projects:
        project_url = f"https://console.neon.tech/api/v2/projects/{projects}"
        project_data = rq.get(project_url,headers=headers).json()
        
        with st.expander("Project Details", expanded=False):
            st.write(project_data)
        
        branch_url = f"https://console.neon.tech/api/v2/projects/{projects}/branches"
        branch_data = rq.get(branch_url,headers=headers).json()
        with st.expander("Branches", expanded=False):
            st.write(branch_data)

        endpoint_url = f"https://console.neon.tech/api/v2/projects/{projects}/endpoints"
        endpoint_data = rq.get(endpoint_url,headers=headers).json()
        with st.expander("Endpoints", expanded=False):
            st.write(endpoint_data)

        operation_url = f"https://console.neon.tech/api/v2/projects/{projects}/operations"
        operation_data = rq.get(operation_url,headers=headers).json()
        df = pd.DataFrame(operation_data["operations"])
        with st.expander("Operations", expanded=False):
            st.table(df.iloc[:,[2,3,4,5]])
