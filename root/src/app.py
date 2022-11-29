import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import pickle
from functions import *

# Constants
if not firebase_admin._apps:
  cred = credentials.Certificate("./constants/serviceAccountsKey.json")
  # load_dotenv("./constants/.env")
  # MED_APP_CREDS = create_keyfile_dict()
  # jsondata = os.getenv("MED_APP_CREDS")
  # with open("./constants/credsData.json", "w") as f:
  #   json.dump(jsondata, f)
  
  # st.write(MED_APP_CREDS)
  # st.write(type(MED_APP_CREDS))
  # cred = credentials.Certificate("./constants/credsData.json")
  firebase_admin.initialize_app(cred)


with open('./constants/Constants.pkl', 'rb') as f:
  list1, list2, list3, imagelist = pickle.load(f)

db = firestore.client()

# Streamlit
st.set_page_config(page_icon="🕯️", page_title="Meditation App", layout="wide")
st.sidebar.title("Meditation App🕯️")
st.markdown('<center><h1 style="color:yellow;">Welcome to the Meditation Application🕯️</h1></center>', unsafe_allow_html=True)

if 'login' not in st.session_state:
  st.session_state.login = False

if 'email' not in st.session_state:
  st.session_state.email = ""

if st.session_state.login == False:
  choice = st.sidebar.radio("", ("Sign In", "Sign Up"))
  if choice == "Sign In":
    st.write("Enter details for signin")
    email = st.text_input('Enter email address')
    password = st.text_input('Enter password', type="password")
    if st.button("Submit"):
      try:
        # singninobj = auth.sign_in_with_email_and_password(email, password)
        user = auth.get_user_by_email(email)
        # print(user.custom_claims)
        if password == user.uid:
          st.session_state.login = True
          st.session_state.email = email
        else:
          raise Exception("Password is incorrect!")
      except Exception as e:
        st.error(e)
      else:
        st.balloons()
        st.success("Logged In succesfully")
        time.sleep(2)
        st.experimental_rerun()
        
  elif choice == "Sign Up":
    st.write("Enter details for signup")
    name = st.text_input('Enter your name')
    email = st.text_input('Enter email address')
    password = st.text_input('Enter password', type="password")
    
    if st.button("Submit"):    
      try:
        # signupobj = auth.create_user_with_email_and_password(email, password)
        auth.create_user(
            email=email,
            uid=password,
            password=password
        )
        # user = auth.get_user_by_email(email)
        # auth.create_custom_token(user.uid, {"pass" : password})
      except Exception as e:
        st.error(e)
        # st.error("Username Already exists")
      else:
        st.balloons()
        st.success("User successfully created")

if st.session_state.login:
  choice = st.sidebar.selectbox("Meditation", ("Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Explore", "Assessment"))
  if choice == "Chapter 1":
    # st.write("Welcome to chapter 1")
    st.markdown("<h2>Chapter 1 : SOS</h2>", unsafe_allow_html=True)
    st.markdown("<h3>S : Stand Back</h3>" , unsafe_allow_html = True )
    st.write("When we are angry we can be very quick to react so taking a step back can give us some time to cool off and think rationally.")
    for i in list1:
      st.markdown("• "+i , unsafe_allow_html=True)
    st.markdown("<h3>O : Observe</h3>", unsafe_allow_html=True)
    st.write("Once you can feel yourself calming down take some time to observe the situation. Think about the situation and what triggered you to get angry? Is your reaction to the situation rationale? It is also good to try to figure out what the emotion underneath your anger is. Ask yourself what am I feeling underneath this anger? Am I sad? Am I hurt? Am I disappointed")
    st.markdown("<h3>S : Steer</h3>", unsafe_allow_html=True)
    st.write("Once you have worked out what it is that has triggered your anger and the feelings underneath it you can start to figure out a plan. Ask yourself what is this the best way to react to this situation in order to achieve the best outcome? Once you have thought of the best way to handle the situation you can steer.  This might mean going and talking to the person that upset you and apologising. It might mean telling someone that you are hurt.")
  
  elif choice == "Chapter 2":
    # st.write("Welcome to chapter 2")
    st.markdown("<h2><b>Chapter 2 : Innate Qualities</b></h2>", unsafe_allow_html=True)
    col1 , col2 = st.columns(2)
    with col1:
      for i in list2:
          st.markdown("• "+i , unsafe_allow_html=True)
    with col2:
      for j in imagelist:
          st.image(j , width=190)
          

  elif choice == "Chapter 3":
    st.markdown("<h2>Chapter 3: Meditation<h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
      st.image("./constants/image/meditation.jpg", caption="Connecting with the Supreme Being", width=400)
    st.markdown("<h4>Let's meditate<h4>", unsafe_allow_html=True)
    st.audio("./constants/audio/meditation.mp3")
    pre_med_stress = st.slider("What was your stress level before meditation?", min_value=0, max_value=100, value=80)
    completion = st.slider("How much you were able to complete the video ?", min_value=1, max_value=100, value=50)
    concentration = st.slider("How much you were able to concentrate ?", min_value=1, max_value=100, value=50)
    post_med_stress = st.slider("What is your stress level after meditation?", min_value=0, max_value=100, value=40)
    feedback = st.text_area("Tell us about the meditation process")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
      if st.button("Submit"):
        now = datetime.now()
        saveData(email=st.session_state.email,
          completion=completion,
          concentration=concentration,
          feedback=feedback,
          date=now.strftime('%d-%m-%Y %H:%M:%S'), 
          pre_med_stress=pre_med_stress, 
          post_med_stress=post_med_stress,
          db=db)
  
  elif choice=="Chapter 4":
    st.markdown("<h4>Chapter 4: Thoughts</h4>", unsafe_allow_html=True)
    st.write("Let's learn about the types of thoughts and what is their significance.")
    # video_file = open('./constants/video/thoughts_meditation.mp4', 'rb')
    # video_bytes = video_file.read()
    st.video("https://www.youtube.com/watch?v=c25iy0Jas60")

  
  elif choice == "Explore":
    st.header("Feedbacks")
    database = extractData(db=db)
    st.write(database)
    if st.checkbox("Start the data analysis"):
      analysed_feedbacks = analyseFeedbacks(reviews=database)
      st.write(analysed_feedbacks)
      col = st.color_picker("Select plot colour")
      interactivePlot(database, col)

  else:
    st.write("Now it is the time to test your learnings.")
    count = 0
    for i in list3:
      a = st.radio(i[0],i[1])
      if a==i[2]:
            count=count+1
    if st.button("Submit"):
      score = count*100/15
      if count>=(len(list3)*0.7):
        st.success("Well Done , You have scored "+(str)(score)+"%")
      else:
        st.error("Sorry , You have scored "+(str)(score)+"% , Minimum passing marks are 70.0%")
      now = datetime.now
      # saveScore(st.session_state.email, now.)
  if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.session_state.email = ""
    st.experimental_rerun()