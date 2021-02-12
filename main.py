import streamlit as st

st.set_page_config(layout='wide',initial_sidebar_state='expanded')




st.title("Gender Variomat")

gender = st.sidebar.radio("Wie willst du gendern?", ("Maskulin","Feminin","Entgendern","Phettberg","Albrecht"))
gender = gender.lower()

text = "{person} geht {zur_person} und kauft ein Br&ouml;tchen."
fill = {}



if gender == 'maskulin':
    fill['person'] = "Der Wirtschaftsinformatiker"
    fill['zur_person'] = "zum B&auml;cker"
elif gender == 'feminin':
    fill['person'] = "Die Wirtschaftsinformatikerin"
    fill['zur_person'] = "zur B&auml;ckerin"
elif gender == 'entgendern':
    fill['person'] = "Der Wirtschaftsinformatikende"
    fill['zur_person'] = "zum Bakenden"
elif gender == 'phettberg':
    fill['person'] = "Das Wirtschaftsinformatiky"
    fill['zur_person'] = "zum B&auml;cky"
elif gender == 'albrecht':
    fill['person'] = "Das Wirtschaftsinformatikeral"
    fill['zur_person'] = "zum B&auml;ckeral"

st.write(text.format(**fill))

st.sidebar.markdown("[Sourcecode at Github](https://github.com/MartinEnders/Gender-Variomat)")
