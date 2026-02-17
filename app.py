import streamlit as st
from transformers import pipeline
import random

# Load AI model
generator = pipeline("text-generation", model="gpt2")

# App Title
st.set_page_config(page_title="AI Social Media Caption Generator", layout="wide")
st.title("✨ AI Social Media Caption & Content Generator")

# Sidebar for options
st.sidebar.header("Customization Options")
tone = st.sidebar.selectbox("Choose Caption Tone:", ["Catchy", "Professional", "Funny", "Trendy", "Inspirational"])
platform = st.sidebar.selectbox("Platform:", ["Instagram", "Twitter", "LinkedIn", "Facebook"])
add_hashtags = st.sidebar.checkbox("Generate Hashtags")
num_captions = st.sidebar.slider("Number of Captions", 1, 5, 3)

# Main input
product = st.text_area("Describe your product/service/event:", placeholder="e.g., Organic skincare brand launch")

# Generate captions
if st.button("Generate Captions"):
    if product:
        st.subheader("Generated Captions:")
        captions = []
        for i in range(num_captions):
            prompt = f"Write a {tone} {platform} caption for {product}"
            result = generator(prompt, max_length=60, num_return_sequences=1)
            caption = result[0]['generated_text']
            captions.append(caption)
            st.write(f"**Caption {i+1}:** {caption}")

            # Hashtag generator
            if add_hashtags:
                hashtags = ["#Love", "#Trending", "#Inspiration", "#Viral", "#NewLaunch", "#AIContent", "#BusinessGrowth", "#SocialMediaMagic"]
                random.shuffle(hashtags)
                st.write("📌 Suggested Hashtags:", " ".join(hashtags[:5]))

        # Download option
        st.download_button(
            label="Download Captions",
            data="\n".join(captions),
            file_name="captions.txt",
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.markdown("🚀 Built with Hugging Face + Streamlit | Free Premium Access Now | Advanced Features Coming Soon")