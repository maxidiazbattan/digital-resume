from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# --- PROJECTS CARD FUNCTION ---
def projects_card(image_url="", proyect_name="",  proyect_url=""):

    card = f"""
        <div style="border-radius: 10px; padding: 1rem; background-color: #484c63; display: flex; align-items: center; margin-bottom: 0.5rem;">
            <img src="{image_url}" alt="Project image" style="border-radius: 10%; width: 80px; height: 80px; margin-right: 1rem;">
            <div style="line-height: 1;">
                <a href="{proyect_url}" target="_blank" style="font-size: 0.8rem;">{proyect_name}</a>
            </div>
        </div>
    """

    return card


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Resume | Maximiliano Diaz Battan"
PAGE_ICON = ":wave:"
NAME = "Maximiliano Diaz Battan"
DESCRIPTION =   """
                BBA | Data Analyst
                """
EMAIL = "maxidiazbattan@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- OPTION MENU ---

selected = option_menu(
    menu_title=None,
    options=['Home', 'Proyects', 'Contact'],
    icons=['house', 'book', 'envelope'],
    default_index=0,
    orientation='horizontal',
    styles= {
        "container": {"padding": "0!important", "background-color": "#141414"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "darkgray"},
            }

)


if selected == 'Home':

    # --- ME SECTION ---
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
    
    with col2:
        st.write('')
        
    with col3:
        st.image(profile_pic, width=230)

    # --- ABOUT ME ---
    st.write('\n')
    st.header("About me")
    st.write("---")
    st.write(
    """
    I have been working as a business administrator for 10 years and have always been fascinated by the field of data. A few years ago, I discovered Python and its vast capabilities. 
    That's why I decided to focus on studying data analysis with Python and am now pursuing data science. 
    My goal is to obtain a master's degree in the field of data in the next few years and transition fully into this exciting field.
    """
    )


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.header("Experience & Qualifications")
    st.write("---")
    st.write(
        """
    - ✔️ 10 Years of accounting experience and more than a year of freelancing experience extracting insights of data and machine learning.
    - ✔️ Deep understanding of Python, SQL and Excel.
    - ✔️ A strong grasp of statistical principles and their practical applications.
        """
    )


    # --- SKILLS ---
    st.write('\n')
    st.header("Hard Skills")
    st.write("---")
    st.write(
        """
    - 💻 Languages: Python, SQL, Excel.
    - 📊 Data analysis: Pandas, Modin, Rapids (cuDF & cuPY), DuckDB, Sqlite3, Numpy, Matplotlib, Seaborn, Plotly, Dash, and more.
    - 📚 Machine Learning: Sklearn, Rapids (cuML), XGBoost, LightGBM, Catboost, Interpret, Tabnet, Optuna, Feature Engine, SHAP, Streamlit, and more.
    - 📚 Deep Learning: Pytorch, Pytorch lightning, Timm, SMP, Albumentations, Audiomentations, Transformers, and more.
    - 🗄️ Others skills: Docker, Git & Github, Office, Linux.
        """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.header("Recent Work History")
    st.write("---")

    # --- JOB 1
    st.write("👷", "**Self employed - Freelancer** | From 02/2018 to Present")
    st.write(
        """
    - ► Frelancing data analysis and machine learning jobs.
    - ► Accounting administrative tasks.
    - ► Business plans, Economic analysis, Feasibility studies, etc.
        """
    )

    # --- JOB 2
    st.write('\n')
    st.write("👷", "**Banking and Accounting manager - Ferretería Zárate (sME)** | From 02/2016 to 06/2017")
    st.write(
        """
    - ► Various banking operations (sale of securities, deposits, loans, leases, banking agreements, etc.).
    - ► Accounting.
    - ► Treasury.
    - ► Suppliers payment.
    - ► In charge of a work team of 5 people.
        """
    )

    # --- JOB 3
    st.write('\n')
    st.write("👷", "**Accounting assistant - Ferretería Zárate (sME)** | From 02/2014 to 06/2016")
    st.write(
        """
    - ► Bank reconciliations.
    - ► Bank debt statements.
    - ► Accounting.
    - ► Bank checks and payments.
        """
    )


if selected == 'Proyects':

    # --- Projects ---
    st.write('\n')
    st.header("Projects")
    st.write("---")
    
    st.write('\n')
    st.subheader("Exploratory data analysis")
    st.write("---")
    st.write(
        """
        Exploratory Data Analysis (EDA) is an approach to analyzing datasets that summarizes their main characteristics using statistical graphics and other data visualization methods. 
        While various statistical models can be used, EDA is primarily used to see what the data can tell us beyond the formal modeling or hypothesis-testing task. 
        EDA is one of the crucial steps in Data Science that allows us to gain insights and statistical measures of the data we are dealing with. For this task, I utilized several Python libraries such as Pandas, Numpy, Plotly, and more.
        """
    )

    EDA =   {
            "kaggle": {'name':"Kaggle survey EDA - Extracting insights about Kagglers users", 'url': "https://www.kaggle.com/code/maxdiazbattan/kaggle-survey-2021-eda-initial-insights",
                  'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_1.png'},
            "covid_dl": {'name':"Covid impact on learning EDA - Covid pandemic impact on american students", 'url': "https://www.kaggle.com/code/maxdiazbattan/covid-impact-digital-learning-data-cleaning-eda",
                  'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_2.png'},
            "covid_la": {'name':"Covid Latin america EDA - Covid pandemic analysis over Latin america", 'url': "https://www.kaggle.com/code/maxdiazbattan/covid-eda-on-latin-america-dash-dashboard",
                  'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_3.png'},
    }

    for project in EDA:
        st.markdown(projects_card(image_url=EDA[project]['image'], proyect_name=EDA[project]['name'], proyect_url=EDA[project]['url']), unsafe_allow_html=True)


    st.write('\n')
    st.subheader("Dashboards")
    st.write("---")
    st.write(
    """
    A dashboard is a user interface that organizes and presents information in an easy-to-read format. Through dashboards, stakeholders can quickly identify current and historical performance and can also utilize the data to define metrics and set goals. 
    To create dashboards, I used Dash, a Python library that allows you to create dashboards in pure Python. I also used Pandas for data cleansing. 
    The dashboards are deployed on Render website, a cloud service platform that allows you to deploy web apps among other things. It may take a few seconds to load because the apps are hosted on Render servers.
    """
    )

    DASHBOARDS = {
        "covid": {'name':"Covid dashboard - Covid pandemic Dashboard", 'url': "https://covid-dashboard-colj.onrender.com/",
                  'image': 'https://raw.githubusercontent.com/maxidiazbattan/covid-dashboard/main/assets/covid%20dash.png'},

        "crypto": {'name':"Crypto dashboard - Cryptocurrencies Dashboard", 'url': "https://crypto-dashboard-33bn.onrender.com/",
                  'image': 'https://raw.githubusercontent.com/maxidiazbattan/crypto-dashboard/main/assets/crypto%20dash.jpg'},

        "house": {'name':"House prices Dashboard - New York house prices Dashboard", 'url': "https://ny-house-prices-dashboard.onrender.com/",
                  'image': 'https://raw.githubusercontent.com/maxidiazbattan/house-prices-dashboard/main/assets/house%20prices.png'},
            }


    for project in DASHBOARDS:
        st.markdown(projects_card(image_url=DASHBOARDS[project]['image'], proyect_name=DASHBOARDS[project]['name'], proyect_url=DASHBOARDS[project]['url']), unsafe_allow_html=True)
    

    st.write('\n')
    st.subheader("Machine learning")
    st.write("---")
    st.write(
    """
    Machine learning (ML) is a process that uses a variety of algorithms that iteratively learn from data to improve, describe data, and predict outcomes. 
    As the algorithms ingest training data, it is then possible to produce more precise models based on that data. A machine learning model is the output generated when you train your machine learning algorithm with data. 
    I have worked on several ML projects and competitions where I have used different libraries such as Pandas, Matplotlib, Seaborn, Plotly, Sklearn, Xgboots, LightGBM, Catboost, Shap, etc. 
    Below are some examples of my work:
    """
    )

    ML =   {
    'wallmart':{'name':"Wallmart forecasting - Predict sales of Wallmat stores",
                'url': " https://www.kaggle.com/code/maxdiazbattan/wallmart-sales-top-3-eda-feature-engineering",
                'image':'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_7.png'},
    'house':{'name':"House prices - Predict house prices",
                'url' : "https://www.kaggle.com/code/maxdiazbattan/house-prices-top-4",
             'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_8.png'},
    'categorizer': {'name':"Categorizer app - E-commerce categorizer real freelance project ",
                     'url': "https://github.com/maxidiazbattan/streamlit-categorizador-RepuestosYa",
                    'image':'https://github.com/maxidiazbattan/streamlit-categorizador-RepuestosYa/raw/main/streamlit-categorizador-repuestosya.jpg'}
    }

    for project in ML:
        st.markdown(projects_card(image_url=ML[project]['image'], proyect_name=ML[project]['name'], proyect_url=ML[project]['url']), unsafe_allow_html=True)

    st.write('\n')
    st.subheader("Deep learning")
    st.write("---")
    st.write(
    """
    Deep learning (DL) is a computer technique that uses multiple layers of neural networks to extract and transform data. Each of these layers takes its inputs from previous layers and progressively refines them. 
    The layers are trained by algorithms that minimize their errors and improve their accuracy. In this way, the network learns to perform a specified task, like human speech recognition to animal image classification. 
    Below are some examples of my DL projects from two different Kaggle competitions:    
    """
    )

    DL =   {
    'cassava':{'name':"Cassava competition - Identify the type of disease present on a cassava leaf image",
               'url':" https://www.kaggle.com/code/maxdiazbattan/cassava-pipeline-top-5-pytorch-lightning-w-b",
               'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_10.jpg'},
    'tps':{'name':"📊 Tabular Playground -  Predict the forest cover type (the predominant kind of tree cover) ",
            'url': "https://www.kaggle.com/code/maxdiazbattan/tps-2021-pytorch-lightning",
           'image': 'https://github.com/maxidiazbattan/digital-curriculum/blob/main/assets/thumbs/thumb_11.png'}
    }

    for project in DL:
        st.markdown(projects_card(image_url=DL[project]['image'], proyect_name=DL[project]['name'], proyect_url=DL[project]['url']), unsafe_allow_html=True)


if selected == 'Contact':
    
    st.write('\n')
    st.subheader("Contact information")
    st.write("---")
    st.write("Email:")
    st.write("📫", EMAIL)

    # --- Download CV ---
    st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
    
    SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/maxidiazbattan/?locale=en_US",
    "Kaggle": "https://www.kaggle.com/maxdiazbattan",
    "GitHub": "https://github.com/maxidiazbattan",
                    }

    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA), gap="large")
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
