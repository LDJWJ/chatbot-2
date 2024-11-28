import streamlit as st  
from PIL import Image  

# 앱 제목  
st.title("이미지 반으로 줄이기")  

# 이미지 업로드  
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])  

if uploaded_file is not None:  
    # 이미지 열기  
    image = Image.open(uploaded_file)  
    
    # 원본 이미지 표시  
    st.image(image, caption="원본 이미지", use_column_width=True)  
    
    # 이미지 크기 반으로 줄이기  
    new_width = image.width // 2  
    new_height = image.height // 2  
    resized_image = image.resize((new_width, new_height))  
    
    # 줄인 이미지 표시  
    st.image(resized_image, caption="줄인 이미지", use_column_width=True)  

    # 줄인 이미지 다운로드  
    st.download_button(  
        label="줄인 이미지 다운로드",  
        data=resized_image,  
        file_name="resized_image.png",  
        mime="image/png"  
    )
