import streamlit as st
def welcome_page():
    coli1,coli2=st.columns(2)
    with coli2:
        st.title("Welcome to Skin Saver")
    with coli1:
        st.image("logo.png")
    st.write(
        """
        Skin Saver helps you identify different skin conditions.

         Conditions you might find:
        - Acne
        - Eczema
        - Psoriasis
        - Rosacea
        - Skin Cancer

        Please visit the Scan page to analyze your skin.
        """)
      

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
def welcome_page():
    coli1,coli2=st.columns(2)
    with coli2:
        st.title("Welcome to Skin Saver")
    with coli1:
        st.image("logo.png")
    st.write(
        """
        Skin Saver helps you identify different skin conditions.

         Conditions you might find:
        - Acne
        - Eczema
        - Psoriasis
        - Rosacea
        - Skin Cancer

        Please visit the Scan page to analyze your skin.
        """)
      

    

def scan_page():

    st.title("Skin Scan")
    st.write(
    """
    To scan your skin, please upload an image or use a device.
    """
    )
    uploaded_files = st.file_uploader(
    "Choose a CSV file"
)
    
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

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Scan", "About Me"])
    if page == "Welcome":
     welcome_page()
    elif page == "Scan":
     scan_page()
    elif page == "About Me":
     about_me_page()
main()










    