import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="نظام الإنذار المبكر الزراعي", page_icon="🌾", layout="wide")

st.title("🌾 لوحة تحكم الإنذار المبكر والتحكم الزراعي - ليبيا")
st.markdown("### نظام رصد وتوقع الأمراض الفطرية بناءً على المتغيرات المناخية (ERA5)")

# الشريط الجانبي للإعدادات
st.sidebar.header("إعدادات النظام والحقول")
crop_choice = st.sidebar.selectbox("اختر المحصول:", ["البطيخ (Alternaria alternata)", "الشعير والقمح", "أشجار الفاكهة"])
region = st.sidebar.selectbox("اختر المنطقة:", ["سرت", "الجبل الأخضر (البيضاء - شحات)", "بنغازي"])

# مؤشرات الحالة العلوية
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="درجة الحرارة الحالية (ERA5)", value="28 °C", delta="+1.5 °C عن المعدل")
with col2:
    st.metric(label="رطوبة الهواء والبلل الورقي", value="78 %", delta="مرتفعة")
with col3:
    st.error("🚨 حالة الإنذار: خطر وبائي محتمل في الحقل")

st.divider()

# عرض الرسوم البيانية أو أقسام التطبيق
tab1, tab2, tab3 = st.tabs(["📊 منحنيات تفشي الأمراض والمناخ", "📷 التشخيص الذكي للصور", "📂 تقارير الحقول"])
import streamlit as strlit

# افتراض أنكِ تقوبين بتخزين اسم الإصابة ونسبة الثقة المتنبأ بها من النموذج في متغيّرات مثل:
# predicted_label = "Alternaria alternata (لفحة الأوراق)"
# confidence_score = 0.94  # نسبة الثقة (مثلاً 94%)

# --- 1. عرض نسبة الثقة بشكل مرئي (Metric أو Progress Bar) ---
strlit.subheader("📊 نتيجة التشخيص الذكي")

# عرض النتيجة بشكل بارزة
strlit.markdown(f"**التشخيص المقترح:** {predicted_label}")

# عرض نسبة الثقة كنسبة مئوية واضحة
confidence_percentage = int(confidence_score * 100)
strlit.metric(label="مستوى دقة الثقة (Confidence Score)", value=f"{confidence_percentage}%")
strlit.progress(confidence_score)

# --- 2. عرض التوصيات العلاجية والوقائية المخصصة ---
strlit.subheader("🛠️ التوصيات الإرشادية وبرنامج المكافحة")

if "Alternaria" in predicted_label:
    strlit.warning(
        "**توصيات إدارة مرض لفحة الأوراق (Alternaria alternata):**\n"
        "- **المكافحة الوقائية:** تجنب الري العلوي المفرط وتقليل رطوبة الأوراق ورش المبيدات الوقائية عند ارتفاع الرطوبة النسبية.\n"
        "- **المكافحة العلاجية:** استخدام مبيدات فطرية تخصصية مسجلة عند ظهور الإصابة الأولى.\n"
        "- **إدارة المخلفات:** التخلص من الأوراق المصابة وبقايا المحصول السابق لمنع بقاء الجراثيم."
    )
else:
    strlit.info(
        "**التوصيات العامة للحقل:**\n"
        "- الاستمرار في مراقبة مؤشرات الحرارة والرطوبة (ERA5).\n"
        "- الحفاظ على تهوية جيدة بين النباتات."
    )
with tab1:
    st.subheader("مقارنة درجات حرارة ERA5 ومنحنى الإصابة التاريخي")
    # محاكاة رسم بياني تفاعلي
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['معدل الإصابة التاريخي', 'درجات حرارة الحارة الحالية']
    )
    st.line_chart(chart_data)

with tab2:
    st.subheader("فحص وتشخيص عينات الأوراق المصابة")
    uploaded_file = st.file_uploader("قم برفع صورة الورقة المصابة هنا...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="الصورة المرفوعة للورقة", use_container_width=True)
        st.info("جاري تحليل الصورة عبر نموذج الذكاء الاصطناعي...")
        st.warning("⚠️ التشخيص المقترح: أعراض الإصابة بلفحة الأوراق (Alternaria alternata). يُنصح باتخاذ إجراءات الوقاية.")

with tab3:
    st.subheader("سجلات التقارير وحفظ البيانات")
    st.write("يمكنك تصدير تقارير الإنذار المبكر كملفات مسجلة لتوשيقها في الأبحاث والجهات الرسمية.")
    if st.button("تصدير التقرير الآن"):
        st.success("تم تجهيز التقرير بنجاح وحفظه في النظام.")
