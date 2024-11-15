import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pk
import pandas as pd
import plotly.express as px

# Set the background image for the app
pg_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("crop.png");
background-size: cover;
}
</style>
"""

# Set page configuration
st.set_page_config(page_title='CROP_RECOMMENDATION_SYSTEM', layout='wide', page_icon='🌱')

# Markdown for the attribution section
attribution = """
- N - ratio of Nitrogen content in soil
- P - ratio of Phosphorous content in soil
- K - ratio of Potassium content in soil
- temperature - temperature in degree Celsius
- humidity - relative humidity in %
- ph - ph value of the soil
- rainfall - rainfall in mm
"""

# Apply the background style
st.markdown(pg_bg_img, unsafe_allow_html=True)

# Horizontal menu without the "info" button
selected = option_menu(
    menu_title='🌾CROP RECOMMENDATION SYSTEM🌾',
    options=['Dashboard', 'predict'],
    icons=['person-circle', 'info-circle-fill'],
    menu_icon='🌾',
    orientation='horizontal',
    default_index=1,
    styles={
        "container": {"padding": "5!important", "background-color": '#6AC6F7'},
        "icon": {"color": "white", "font-size": "23px"},
        "nav-link": {"color": "black", "font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#8EF314"},
        "nav-link-selected": {"background-color": "white"},
    }
)

# Content for the "predict" tab
if selected=='predict':
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color:#6AC6F7;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #0C0C0C ;
        color:#ff99ff;
        }
    </style>""", unsafe_allow_html=True)
    model=pk.load(open('model.pkl','rb'))
    with st.expander('Data fields'):
        st.markdown(attribution)
    p1,p2=st.columns(2)
    with p1:
        
        pp1,pp2,pp3=st.columns(3)
            
        with pp1:
            N=st.number_input('Nitrogen(N)',0,140)
            P=st.selectbox('Phosphorous(P)',range(5,145))
            K=st.selectbox('Potassium(K)',range(5,205))  
             
        with pp2:
            temperature=st.selectbox('Temperature',range(8,44)) 
            humidity=st.number_input('humidity',14,100)
            ph=st.selectbox('ph',range(3,10))
            
        with pp3:
            rainfall=st.selectbox('rainfall',range(20,299))
            if st.button('predict.'):
                with p2:
                    
                    
                    input_data_module=pd.DataFrame([[N,P,K,temperature,humidity,ph,rainfall]],
                    columns=['N','P','K','temperature','humidity','ph','rainfall']
                    )
                
                    with st.expander('View you selected Soil nutrien values'):
                        st.dataframe(input_data_module)
                    l1,l2=st.columns(2)
                    crop=model.predict(input_data_module)
                    if crop==1:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Rice 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('1.png',width=180)    
                    elif crop==2:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Maize 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('2.PNG',width=180)    
                    elif crop==3:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Chickpea 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('3.png',width=180)    
                    elif crop==4:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Kidneybeans 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('4.png',width=180)    
                    elif crop==5:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Pigeonpeas 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('5.png',width=180)    
                    elif crop==6:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mothbeans 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('6.png',width=180)    
                    elif crop==7:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mungbean
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('7.png',width=180)    
                    elif crop==8:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Blackgram
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('8.png',width=180)    
                    elif crop==9:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Lentil
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('9.png',width=180)    
                    elif crop==10:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Pomegranate
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('10.png',width=180)    
                    elif crop==11:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Banana
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('11.png',width=180)    
                    elif crop==12:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mango
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('12.png',width=180)    
                    elif crop==13:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Grapes
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('13.png',width=180)    
                    elif crop==14:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Blackgram
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('14.png',width=180)    
                    elif crop==15:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Muskmelon
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('15.png',width=180)    
                    elif crop==16:
                        st.write('apple')
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Apple
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('16.png',width=180)    
                    elif crop==17:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Orange
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('17.png',width=180)    
                    elif crop==18:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Papaya
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('18.png',width=180)    
                    elif crop==19:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Coconut
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('19.png',width=180)    
                    elif crop==20:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Cotton
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('20.png',width=180)    
                    elif crop==21:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - jute
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('21.png',width=180)    
                    elif crop==22:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Coffee
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('22.png',width=180)    



if selected == 'Dashboard':
    cpro = pd.read_csv('crop_production.csv')

    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

    with c5:
        state_name = st.selectbox('State Name', cpro['State_Name'].unique())
    with c6:
        crop1 = st.selectbox('Crop', cpro['Crop'].unique())
    with c7:
        district_name = st.selectbox('District Name', cpro['District_Name'].unique())

    with c1:
        with st.container():
            st.write('Number of Crops')
            rce = cpro['Crop'].nunique()
            st.subheader(rce)
    with c2:
        with st.container():
            st.write('Total Season')
            st.subheader(cpro['Season'].nunique())
    with c3:
        with st.container():
            st.write('Total State Name ')
            st.subheader(cpro['State_Name'].nunique())
    with c4:
        with st.container():
            st.write('Total District Name')
            st.subheader(cpro['District_Name'].nunique())

    s1, s2, s3 = st.columns(3)

    with s1:
        with st.container():
            # Fix: Rename 'count' to avoid conflict
            std_wise_crop = cpro.groupby('State_Name')['Crop'].value_counts().reset_index(name='count')
            std_input = std_wise_crop[std_wise_crop['State_Name'] == state_name]
            fig = px.pie(std_input, values='count', names='Crop', title=f'State {state_name} Wise Crop',
                         color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig)

    with s3:
        with st.container():
            dis_wise_crop = cpro.groupby('District_Name')['Crop'].value_counts().reset_index(name='count')
            dis_input = dis_wise_crop[dis_wise_crop['District_Name'] == district_name]
            fig = px.pie(dis_input, values='count', names='Crop', title=f'District {district_name} Wise Crop')
            st.plotly_chart(fig)

    with s2:
        with st.container():
            cro_wise_prod = cpro.groupby('Crop')['State_Name'].value_counts().reset_index(name='count')
            crop_input = cro_wise_prod[cro_wise_prod['Crop'] == crop1]
            fig = px.bar(crop_input, x='State_Name', y='count', title=f'Crop {crop1} Wise State name')
            st.plotly_chart(fig)

    v1, v2 = st.columns([0.35, 0.65])
    with v1:
        with st.container():
            Season_wise = cpro.groupby('Season')['Production'].sum().reset_index()
            fig = px.bar(Season_wise, y='Season', x='Production', title='Season Wise Production')
            st.plotly_chart(fig)

    with v2:
        with st.container():
            year_wise = cpro.groupby('Crop_Year')['Production'].sum().reset_index()
            fig = px.line(year_wise, x='Crop_Year', y='Production', title='Year Wise Production', markers=True)
            st.plotly_chart(fig)

    h1, h2, h3, h4 = st.columns(4)
    crop = pd.read_csv('Crop.csv')

    with h1:
        with st.container():
            k_wise_crop = crop[['K', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(k_wise_crop, y="label", x="K", title='Potassium content in soil wise crop')
            st.plotly_chart(fig)

    with h2:
        with st.container():
            p_wise_crop = crop[['P', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(p_wise_crop, x="label", y="P", title='Phosphorous content in soil wise crop',
                         labels={'P': 'Phosphorous', 'label': 'Crop'})
            st.plotly_chart(fig)

    with h3:
        with st.container():
            tem_wise_crop = crop[['temperature', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(tem_wise_crop, x="label", y="temperature", title='Temperature in degree Celsius wise crop')
            st.plotly_chart(fig)

    with h4:
        with st.container():
            n_wise_crop = crop[['N', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(n_wise_crop, y="label", x="N", title='Nitrogen content in soil wise crop')
            st.plotly_chart(fig)

    p1, p2 = st.columns([0.35, 0.65])
    with p1:
        with st.container():
            h_wise_crop = crop[['humidity', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(h_wise_crop, y="label", x="humidity", title='Relative humidity wise crop')
            st.plotly_chart(fig)

    with p2:
        with st.container():
            ph_wise_crop = crop[['ph', 'label']].groupby('label').value_counts().reset_index(name='count')
            fig = px.bar(ph_wise_crop, y="ph", x="label", title='pH wise crop')
            st.plotly_chart(fig)

    with st.container():
        rain_wise_crop = crop[['rainfall', 'label']].groupby('label').value_counts().reset_index(name='count')
        fig = px.line(rain_wise_crop, y="rainfall", x="label", title='Rainfall wise crop')
        st.plotly_chart(fig)

st.markdown('_____________________________________________________')
