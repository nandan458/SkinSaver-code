import streamlit as st
from PIL import Image
from ultralytics import YOLO
import requests
from streamlit_lottie import st_lottie

# Load the model
@st.cache_resource
def models():
    mod = YOLO('best.pt')
    return mod

st.set_page_config(page_title="SkinSaver", layout="wide")

# Function to load Lottie animation
@st.cache_resource
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_skin_care = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")

# Define the data for the skin conditions
skin_conditions = [
    {
        "name": "Acne",
        "description": "Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells. It often causes pimples, blackheads, and cysts.",
        "prevention_treatment": "Prevent by maintaining a good skincare routine, using non-comedogenic products, and avoiding excessive touching of the face. Treatment may include topical treatments, oral medications, and lifestyle changes.",
        "image": "https://dermablue.com/wp-content/uploads/2018/01/AdobeStock_61720335-scaled.jpeg"
    },
    {
        "name": "Eczema",
        "description": "Eczema, or atopic dermatitis, is a condition that makes your skin red and inflamed, and it can cause itching and dryness.",
        "prevention_treatment": "Prevent by avoiding irritants, using moisturizers regularly, and managing stress. Treatments often involve topical corticosteroids, emollients, and avoiding triggers.",
        "image": "https://skinandcancercenterofarizona.com/wp-content/uploads/2023/05/Eczema-Treatment.webp"
    },
    {
        "name": "Psoriasis",
        "description": "Psoriasis is an autoimmune condition that speeds up the growth cycle of skin cells, resulting in thick, scaly patches of skin that can be itchy and painful.",
        "prevention_treatment": "Prevent by managing stress, avoiding skin trauma, and using moisturizers. Treatments may include topical treatments, phototherapy, and systemic medications.",
        "image": "https://www.vistadermsa.com/wp-content/uploads/2020/05/Psoriasis-scaled-e1588772611595.jpg"
    },
    {
        "name": "Pigment",
        "description": "Pigment conditions are characterized by changes in skin color. Common examples include: - Melasma: Dark, discolored patches often found on the face. Freckles: Small, brown spots usually caused by sun exposure.",
        "prevention_treatment": "- Use sunscreen daily to protect against UV rays. - Avoid excessive sun exposure, especially during peak hours.- Consider wearing protective clothing, such as hats and long sleeves.- Consult a dermatologist for skin treatments and preventive measures.",
        "image": "https://media.healthdirect.org.au/images/inline/original/vitiligo-inline-ff7d37.jpg"
    },
    {
        "name": "Malignant",
        "description": "Malignant skin conditions are cancerous and can be life-threatening. Important types include: - Melanoma: A serious form of skin cancer that arises from pigment-producing cells. - Basal Cell Carcinoma: The most common form of skin cancer, usually appearing as a small, shiny bump. - Squamous Cell Carcinoma: Often appears as a firm, red nodule or a flat lesion with a scaly crust.",
        "prevention_treatment": "- Apply broad-spectrum sunscreen with SPF 30 or higher.- Conduct regular skin self-exams to detect any changes early. - Schedule annual skin checks with a dermatologist.- Avoid tanning beds and limit sun exposure.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Melanoma.jpg"
    },
    {
        "name": "Benign",
        "description": "Benign skin conditions are non-cancerous and usually do not pose a serious health risk. Examples include:- Moles: Common growths on the skin that are usually harmless.- Seborrheic Keratosis: Non-cancerous growths that often appear as rough, scaly patches.- Cysts: Fluid-filled sacs that can form under the skin, usually harmless.",
        "prevention_treatment": "- Monitor your skin regularly for changes in moles or new growths.  - Maintain good skin hygiene to reduce the risk of cysts.  - Use moisturizers to keep the skin healthy and hydrated.  - Avoid picking at or irritating existing skin growths.",
        "image": "https://www.shutterstock.com/image-photo/close-picture-dangerous-brown-nevus-600nw-1403142380.jpg"
    }
]


def welcome_page():
    with st.container():
        col = st.columns([2,1,7,2])
        col[1].image('logo (2).png', width=100)
        col[2].markdown("<h1 style='text-align: center; color: #FFA07A;'>SkinSaver - Skin Disease Detection</h1>", unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: #FFA07A;'>SkinSaver - Skin Disease Detection</h1>", unsafe_allow_html=True)
    st.write("""---""")
    col = st.columns(2)
    with col[1]:
        if lottie_skin_care:
            st_lottie(lottie_skin_care, height=300, key="skin_care_animation")
    with col[0]:
        st.markdown("### Intoduction")
        st.markdown(
            """
            **SkinSaver** is a tool designed to help you better understand skin conditions and manage your skin health effectively. 
            
            Skin diseases can present with symptoms like redness, itching, bumps, and more. 
            
            Some common skin conditions include: **Eczema, Acne, Pigment disorders, Benign and Malignant tumors**.
            """
        )
    
    st.markdown(
        """
        ### Common Causes of Skin Conditions
        - Bacteria trapped in pores or hair follicles.
        - Conditions affecting the thyroid, kidneys, or immune system.
        - Contact with environmental triggers, such as allergens.
        - Genetics and family history.
        - Stress and hormonal imbalance.
        
        Keeping your skin healthy requires protective measures, good skincare habits, and reducing stress levels.
        """
    )
    
    st.markdown("""---""")

    # Streamlit application
    st.header("Skin Conditions Overview")
    st.subheader("Click on each skin condition to learn more!")

    # Create two columns for buttons and details
    col1, col2 = st.columns([1, 3])

    # Variable to keep track of the selected condition
    selected_condition = None

    # Loop through the conditions and create buttons in the first column
    with col1:
        for condition in skin_conditions:
            if st.button(condition["name"], key=condition["name"]):
                selected_condition = condition

    # Display details of the selected condition in the second column
    with col2:
        if selected_condition:
            show_condition_details(selected_condition)

    st.markdown(
            """
            **Let's explore and understand skin health together!**
            """
        )
    
    st.video("https://www.youtube.com/watch?v=ryox2SQKQPU")


def show_condition_details(condition):
    col = st.columns([4,6])
    col[0].markdown(f"## {condition['name']}")
    col[1].image(condition["image"], use_column_width=True)
    with st.expander("Description"):
        st.write(condition["description"])
    with st.expander("Prevention and Treatment"):
        st.write(condition["prevention_treatment"])
    st.markdown("""---""")


def scan_page():
    st.subheader('Steps to Use the App')
    st.markdown('''
        1. Take a clear image of the affected skin area.
        2. Upload the image below.
        3. Click "Analyze" to detect the skin condition and get detailed insights.
    ''')

    # Image upload and analysis section
    with st.container():
        img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
        analyse = st.button('Analyze')

    if analyse:
        if img is not None:
            image = Image.open(img)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.subheader('Analysis Results:')
            model = models()
            res = model.predict(image)
            label = res[0].probs.top5
            conf = res[0].probs.top5conf
            conf = conf.tolist()
            st.write('**Disease Detected**: ' + str(res[0].names[label[0]].title()))
            st.write('**Confidence Level**: ' + str(round(conf[0] * 100, 2)) + '%')
        else:
            st.error("Please upload an image for analysis.")


def about_me_page():
    st.title("About Skin Saver")
    st.write(
        """
        SkinSaver is designed to help people learn more about their skin and manage it effectively.
        
        Developed by **Nandan Kommineni**, a high school freshman with a passion for technology and helping others.
        
        My motivation for this project is to help those struggling with skin conditions feel more confident about themselves and raise awareness about these conditions.
        
        **For more information, visit [SkinSaver.com](http://skinsaver.com) or contact us at nandankomm@gmail.com**
        """
    )
    st.image('image.png', caption="My Picture", use_column_width=True)


def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Scan", "About Me"])
    with tab1:
        welcome_page()
    with tab2:
        scan_page()
    with tab3:
        about_me_page()


main()
