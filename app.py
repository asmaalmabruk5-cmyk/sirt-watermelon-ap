if uploaded_file is not None:
        st.image(uploaded_file, caption="الصورة المرفوعة للورقة", use_container_width=True)
        st.info("جاري تحليل الصورة عبر نموذج الذكاء الاصطناعي...")
        
        # نتائج المحاكاة
        predicted_label = "Alternaria alternata (لفحة الأوراق)"
        confidence_score = 0.94
        
        # عرض النتيجة
        st.warning(f"⚠️ التشخيص المقترح: {predicted_label}")
        
        confidence_percentage = int(confidence_score * 100)
        st.metric(label="مستوى دقة الثقة (Confidence)", value=f"{confidence_percentage}%")
        st.progress(confidence_score)
        
        # --- التوصيات العلاجية ---
        if "Alternaria" in predicted_label:
            st.warning("""
**توصيات إدارة مرض لفحة الأوراق (Alternaria alternata):**
- **المكافحة الوقائية:** تجنب الري العلوي المفرط وتقليل رطوبة الأوراق ورش المبيدات الوقائية.
- **المكافحة العلاجية:** استخدام مبيدات فطرية تخصصية مسجلة عند ظهور الإصابة الأولى.
- **إدارة المخلفات:** التخلص من الأوراق المصابة وبقايا المحصول لمنع بقاء الجراثيم.
            """)