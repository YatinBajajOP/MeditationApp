import pickle
import json
# Adding theory
list1 = ['Walking away.', 'Taking  some deep breaths.', 'Counting backwards from 10.']
list2 = ['<b>PURITY</b> : Purity is the first virtue and the mother of Peace and Happiness. The meaning of purity however, is not celibacy alone. In fact, its accurate meaning is to have purity in our mind, words, and actions. We generally consider the holiness as that of the body. But a person is said holy only if his thoughts are also pure. Thoughts are infact the immediate creation of our mind; and our mind is a reflection of who we are.', '<b>PEACE</b>  : Peace is a garland of your neck - God father Shiv baba (Source: Murli)Every human being today is urging for peace in life. But from where do we get peace? In actuality, peace is the natural stage of us souls. Think this, what if you have no burden, no question and no wasteful thought going in your mind. There is this stillness and in this stillness, everything is clear. This is peace. This is the natural stage of soul and for it to happen with our mind, we need to guide our thoughts towards the right direction. We cannot supress the mind not to think.', "<b>GOD</b>  : God is an ocean love', it is said.Love is a natural feeling of a soul. If you ask 10 people the same question 'What is Love' then you must expect unique answers. Since for everyone the definition of this feeling of love is different. Yet I tell you this, the most innate love of ours is when we realise an eternal spiritual love with the supreme soul (as our father) and with all souls (as brothers). Here on earth, we love someone or something that appeals to us, isn't it?", "<b>JOY</b>  : Joy is a momentous feeling of freedom and attainment. Happiness depends on attainments (what we have achieved or earn). Many people feels joy on material achievements like wealth, fame, good family, respects, etc. Yet, the real joy of more of spiritual attainment. If one has peace and love in his life, it will be said that he is happy as well. Of course, as happiness is nothing but a natural feeling when there is peace and loving relationships in our life, isn't it?", "<b>BLISS</b>  : Bliss is the superior stage of happiness (joy). It is beyond any worldly feeling of happiness and sorrow. Bliss simply means to become 'free' from the experiences of the 5 senses of the body. This freedom from worldly and bodily matters is the source of this utmost joyous experience.Such stage was of ours, when we were in the Golden age. Soul experiences bliss, in the company of its spiritual father, the supreme soul. This can be experienced right in this world, living in this body, through the practice of Raja Yoga.", "<b>POWER</b>  : These are soul's spiritual powers, which we use in many situations of life. Soul has these eight innate powers within whether in merged or in emerged form: Power to Accommodate, Tolerate, to pack up, to Face, to Discriminate, to Judge, to Co-operate & Power to Withdraw. When these powers are in emerged form, they are being used. And when in merged form, they are not used. Yoga (RajYog) is the process by which these powers are emerged and experienced. Learn more on 8 Powers of Soul page.", '<b>KNOWLGDE</b> : True knowledge is the source of all virtues. It means knowing the creation and its almighty creator.The source of spiritual knowledge is only one: the ocean of knowledge, the supreme soul. This knowledge is the very source of all attainments and the method to emerge our above said original virtues.']
questions = [
  "Q1 - What is B in the innate qualities?",
  "Q2 - What does the color blue signifies?",
  "Q3 - Which of the following is not a faculty of the soul",
  "Q4 - ______ are the thoughts about organizing daily life or to carry out everyay activities",
  "Q5 - Thought leads to feelings and feelings leads to action. True or False",
  "Q6 - What is 'O' in SOS?",
  "Q7 - Which faculty of soul is responsible for reasoning an jugement power?",
  "Q8 - When we think about the past or the coming future incidences , what kind of thoughts are we producing?",
  "Q9 - What is vice of the color orange",
  "Q10 - What is the being part in 'Human being'",
  "Q11 - _____ are the most powerful and pure thoughts that empowers us",
  "Q12 - Happiness impacts which part of our body",
  "Q13 - what does mederi means?",
  "Q14 - Which  faculty of consciousness is responsible for thinking?",
  "Q15 - Who am I?"
]

list3 = [
          [questions[0] , ["Being" , "Beautiful" , "Beloved" , "Bliss"] , "Bliss"],
          [questions[1] , ["Peace" , "Bliss" , "Purity" , "Power"] , "Peace"],
          [questions[2] , ["Intellect" , "Heart" , "Mind" , "Resolves"] , "Heart"],
          [questions[3] , ["Waste Thoughts" , "Elevated  Thoughts" , "Essential Thoughts" , "Toxic Thoughts"] , "Essential Thoughts"],
          [questions[4] , ["True" , "False"] , "False"],
          [questions[5] , ["Omit" , "Observe" , "Oblige" , "Or"] , "Observe"],
          [questions[6] , ["Mind" , "Resolves" , "Intellect" , "Soul"] , "Intellect"],
          [questions[7] , ["Positive Thoughts" , "Elevated Thoughts" , "Waste Thoughts" , "Unnecessary Thoughts"] , "Waste Thoughts"],
          [questions[8] , ["Lust" , "Greed" , "Attachment" , "Ego"] , "Lust"],
          [questions[9] , ["The body" , "The presence of mind" , "The soul" , "The Energy of a person"] , "The soul"],
          [questions[10] , ["Elevated Thought" , "Essential Thought" , "Positive Thought" , "Happy"] , "Elevated Thought"],
          [questions[11] , ["Lungs" , "Heart" , "Interstine and liver" , "Brain"] , "Interstine and liver"],
          [questions[12] , ["Supreme father" , "Mother" , "Teachers and guide" , "All of the above"] , "All of the above"],
          [questions[13] , ["Intellect" , "Mind" , "Heart" , "Brain"] , "Mind"],
          [questions[14] , ["My Name" , "My Body" , "My Money" , "An eternal being of light"] , "An eternal being of light"]

]

imagelist = [
             "https://www.yogajournal.com/wp-content/uploads/2007/08/sunset-meditation-mudra.jpg" ,
             "https://img.etimg.com/thumb/msid-70945485,width-640,height-480,imgsize-47100,resizemode-4/knowledge-vs-application.jpg",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPLiwwXxKSeHWD0BoxNtg5-F3UnUSb0EJRmA&usqp=CAU",
             "https://www.isb.edu/content/dam/sites/isb/research-thought-leadership/research-center/sritne/1920x587_ALOH.jpg.transform/isb-carouselBanner-mobile/img.jpeg",
             "https://img.freepik.com/free-vector/bush-peace-sign-background_23-2148009662.jpg?w=2000",
             "https://images-platform.99static.com/_mfQ_AXRT28npseJEX01Qx83G4s=/187x3381:1572x4766/500x500/top/smart/99designs-contests-attachments/89/89395/attachment_89395301",
             "https://img.freepik.com/free-vector/school-knowledge-concept_23-2147503320.jpg?w=2000"
  ]

with open("./constants/Constants.pkl", 'wb') as pklFile:
  pickle.dump([list1, list2, list3, imagelist], pklFile)

# Adding credentials
# with open("./constants/serviceAccountsKey.json") as f:
#   creds = json.loads(f)
# print(creds)

# data = json.load(open('./constants/serviceAccountsKey.json'))

# f = open("./constants/.env", "x")

# for key, value in data.items():
#     f.write(f"{key.upper()}={value}\n")

# with open('./constants/Constants.pkl', 'rb') as f:
#   list1, list2 = pickle.load(f)

# print(list1)
# print("===============================")
# print(list2)
