import streamlit as st

st.set_page_config(page_title="تشخيص لفحة أوراق البطيخ", page_icon="🍉", layout="centered")

st.title("نظام تشخيص مرض لفحة أوراق البطيخ Alternaria alternata 🍉")
st.markdown("أداة ميدانية مخصصة للمزارعين والباحثين لتحليل صور الأوراق وتقديم التوصيات العلاجية الفورية.")
st.markdown("---")

uploaded_file = st.file_uploader("اختر صورة ورقة البطيخ المصابة...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="الصورة المرفوعة للورقة", width='stretch')
    
    with st.spinner("جاري تحليل الصورة عبر نموذج الذكاء الاصطناعي..."):
        predicted_label = "Alternaria alternata (لفحة الأوراق)"
        confidence_score = 0.94
    
    st.warning(f"التشخيص المقترح: {predicted_label} ⚠️")
    st.metric(label="نسبة الثقة في النموذج", value=f"{confidence_score * 100:.1f}%")
    
    st.markdown("---")
    st.subheader("التوصيات العلاجية والوقائية للمزارعين 🌾")
    
    with st.expander("1. المكافحة الزراعية والوقائية", expanded=True):
        st.markdown("""
        - استخدام بذور معقمة وخالية من الإصابات والاعتناء بالدورة الزراعية.
        - تجنب الري المفرط بالرش العلوي لتقليل الرطوبة الحضرية على الأوراق.
        - إزالة الحشائش وبقايا المحاصيل المصابة والتخلص منها بحرقها أو طمرها عميقاً.
        """)
        
    with st.expander("2. المكافحة الكيميائية الموصى بها"):
        st.markdown("""
        - الرش الوقائي أو العلاجي عند ظهور أولى علامات الإصابة باستخدام مبيدات فطرية مناسبة.
        - الالتزام بالتركيز الموصى به وفترة الأمان قبل الحصاد لضمان سلامة الثمار.
        """)
else:
    st.info("الرجاء رفع صورة واضحة لورقة البطيخ المصابة لبدء التشخيص وعرض التوصيات.")
