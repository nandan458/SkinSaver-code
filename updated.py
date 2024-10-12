# SkinSaver-code
import streamlit as st
from PIL import Image

# # Load the model
# 	@st.cache_resource
# 	def models():
# 	    mod = YOLO('best.pt')
# 	    return mod

st.set_page_config(page_title="SkinSaver",layout="wide")

# Define the data for the skin conditions
skin_conditions = [
    {
        "name": "Acne",
        "description": "Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells. It often causes pimples, blackheads, and cysts.",
        "prevention_treatment": "Prevent by maintaining a good skincare routine, using non-comedogenic products, and avoiding excessive touching of the face. Treatment may include topical treatments, oral medications, and lifestyle changes.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Acne_1.jpg/640px-Acne_1.jpg"
    },
    {
        "name": "Eczema",
        "description": "Eczema, or atopic dermatitis, is a condition that makes your skin red and inflamed, and it can cause itching and dryness.",
        "prevention_treatment": "Prevent by avoiding irritants, using moisturizers regularly, and managing stress. Treatments often involve topical corticosteroids, emollients, and avoiding triggers.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Eczema_Hyperpigmentation.jpg/640px-Eczema_Hyperpigmentation.jpg"
    },
    {
        "name": "Psoriasis",
        "description": "Psoriasis is an autoimmune condition that speeds up the growth cycle of skin cells, resulting in thick, scaly patches of skin that can be itchy and painful.",
        "prevention_treatment": "Prevent by managing stress, avoiding skin trauma, and using moisturizers. Treatments may include topical treatments, phototherapy, and systemic medications.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Psoriasis.jpg/640px-Psoriasis.jpg"
    }
]

def welcome_page():
    with st.container():
        col = st.columns([3,9])
        #col[0].write("logo")
        col[0].image('logo.png')
        col[1].text('')
        col[1].text('')
        col[1].text('')
        col[1].text('')
        col[1].markdown("<h1 style='text-align: center; color: white;'>SkinSaver - Skin Disease Detection</h1>", unsafe_allow_html=True)
	    
    st.write(
        """
        Skin diseases are conditions that affect your skin and can cause symptoms like bumps, scaly or rough skin, and more. Some common skin diseases include: 
        \n**Eczema, Acne, Pigment, Benign and Malignant tumors**
        \nSkin diseases can be caused by a number of things, including:
        """)
    st.markdown(
        """
        - Bacteria trapped in your pores or hair follicles 
        - Conditions that affect your thyroid, kidneys, or immune system 
        - Contact with environmental triggers, such as allergens or another person's skin 
        - Genetics
        """
    )
    st.write(
        """
        Psychological stress can also impact your skin health by triggering the release of hormones that can lead to inflammation, which can exacerbate existing skin conditions. 
        \nTo keep your skin healthy, you can try wearing protective equipment, cleaning cuts and scrapes right away, and using sunscreen when outdoors.
        """
    )
    # Streamlit application
    st.title("Skin Conditions Overview")

    # Create columns
    col1, col2, col3 = st.columns(3)

    # Loop through the conditions and populate the columns
    for i, condition in enumerate(skin_conditions):
        with st.container():
            if i == 0:
                with col1:
                    st.subheader(condition["name"])
                    st.write("**Description:**", condition["description"])
                    st.write("**Prevention and Treatment:**", condition["prevention_treatment"])
                    st.image(condition["image"], use_column_width=True)
            elif i == 1:
                with col2:
                    st.subheader(condition["name"])
                    st.write("**Description:**", condition["description"])
                    st.write("**Prevention and Treatment:**", condition["prevention_treatment"])
                    st.image(condition["image"], use_column_width=True)
            elif i == 2:
                with col3:
                    st.subheader(condition["name"])
                    st.write("**Description:**", condition["description"])
                    st.write("**Prevention and Treatment:**", condition["prevention_treatment"])
                    st.image(condition["image"], use_column_width=True)
      

    

def scan_page():

    st.subheader('Steps to use the app')
    st.markdown('''
	- Take a clear image
	- Upload the image
	- Analyze the image and the name and confidence level of the disease along with the causes, preventions, and remedies will be displayed in the result panel below''')
	
	# Image upload and analysis section
    with st.container():
        img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
        analyse = st.button('Analyze')

    if analyse:
        if img is not None:
            image = Image.open(img)
            st.image(image)
	        # st.subheader('Your skin is affected by:')
	        # model = models()
	        # res = model.predict(img)
	        # label = res[0].probs.top5
	        # conf = res[0].probs.top5conf
	        # conf = conf.tolist()
	        # st.write('Disease: ' + str(res[0].names[label[0]].title()))
	        # st.write('Confidence level: ' + str(conf[0]))
    
def about_me_page():


    st.title("About Skin Saver")
    st.write(
     """
     Skin Saver is designed to help people learn more about their skin manage it.
     Developed by Nandan Kommineni. A highschool freshman whose goal is to help people manage their skin and feel confident about themselves. 
    For more information, visit SkinSaver.com or contact us at nandankomm@gmail.com.
     """
    )

def main():
    tab1, tab2, tab3 = st.tabs(["Welcome","Scan","About Me"])
    with tab1:
        welcome_page()
    with tab2:
        scan_page()
    with tab3:
        about_me_page()
main()