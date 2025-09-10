import streamlit as st
import requests

st.set_page_config(page_title="AI Skincare Analysis", page_icon="💆", layout="centered")

st.title("💆 AI Skincare Full Analysis")
st.write("Upload your selfie and lifestyle details for a full personalized skincare analysis.")

# 🔹 Backend URL (Deploy के बाद अपने Render URL से बदलें)
BACKEND_URL = "https://your-backend-url.onrender.com/analyze-full"

# 📂 Selfie Upload
uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "png", "jpeg"])

# 📊 Lifestyle Inputs
sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
water_intake = st.slider("Water Intake (Liters/Day)", 0.0, 5.0, 2.0)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
diet_quality = st.slider("Diet Quality (1-10)", 1, 10, 7)

# 🖱️ Analysis Button
if uploaded_file and st.button("Analyze Full Skin Health"):
    with st.spinner("Analyzing your skin... Please wait"):
        try:
            files = {"file": uploaded_file.getvalue()}
            data = {
                "sleep_hours": sleep_hours,
                "water_intake": water_intake,
                "stress_level": stress_level,
                "diet_quality": diet_quality
            }

            response = requests.post(BACKEND_URL, files=files, data=data)

            if response.status_code == 200:
                result = response.json()

                st.success("Analysis Complete! 🎉")
                st.subheader("📋 Results")
                st.write(f"**Skin Type:** {result.get('skin_type', 'N/A')}")
                st.write(f"**Current Skin Score:** {result.get('skin_score', 'N/A')}")
                st.write(f"**Future Skin Score:** {result.get('future_skin_score', 'N/A')}")
                st.write(f"**Issues:** {', '.join(result.get('issues', [])) if result.get('issues') else 'None'}")
                st.write(f"**Lifestyle Factor:** {result.get('lifestyle_factor', 'N/A')}")

                st.subheader("💡 Recommendations")
                for rec in result.get('recommendations', []):
                    st.write(f"- {rec}")
            else:
                st.error("Backend Error: Please check server logs.")

        except Exception as e:
            st.error(f"Request failed: {e}")

st.markdown("---")
st.markdown("🚀 **Note:** Change `BACKEND_URL` to your Render backend URL after deployment.")
