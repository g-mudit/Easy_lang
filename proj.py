
import os
import streamlit as st
import fitz  # PyMuPDF
from sarvamai import SarvamAI

st.set_page_config(
    page_title="PaperBhasha",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PaperBhasha")
st.subheader("Research papers, explained in your language")
st.write(
    "Upload a research paper and turn complex research "
    "into an accessible explanation."
)

languages = [
    "Hindi", "English", "Telugu", "Tamil", "Bengali",
    "Marathi", "Gujarati", "Kannada", "Malayalam", "Punjabi"
]

language = st.selectbox("Choose your language", languages)

level = st.selectbox(
    "Explanation style",
    ["Beginner-friendly", "University student", "Technical"]
)

pdf = st.file_uploader("Upload research paper (PDF)", type=["pdf"])

if st.button("✨ Explain this paper", type="primary"):
    if not pdf:
        st.warning("Please upload a PDF first.")
        st.stop()

    api_key = "sk_4ko0uph7_arKpkXvBB7CRxDYddTbUs8ej"
    if not api_key:
        st.error("Please set the SARVAM_API_KEY environment variable.")
        st.stop()

    with st.spinner("Reading and explaining your paper..."):
        try:
            document = fitz.open(stream=pdf.getvalue(), filetype="pdf")
            pages = []
            for page in document:
                pages.append(page.get_text())
            paper_text = "\n".join(pages).strip()
            document.close()

            if not paper_text:
                st.error(
                    "No selectable text found. This may be a scanned PDF."
                )
                st.stop()

            # Keep this first demo small and fast.
            paper_text = paper_text[:18000]

            client = SarvamAI(api_subscription_key=api_key)

            prompt = f"""
You are an expert research-paper explainer and teacher.

Read the research paper below and explain it in {language}.
Explanation level: {level}.

Use these sections:
1. Paper title and main idea
2. What problem are the authors solving?
3. Why does this problem matter?
4. Methodology: explain the approach step by step
5. Important experiments and results
6. What is genuinely new in this paper?
7. Limitations and unanswered questions
8. Explain one important concept using a simple example
9. Five key takeaways

Preserve technical terms, equations, and model names where useful.
Explain jargon in the chosen language.
Do not invent results or claims absent from the paper.
If information is missing, say so clearly.

Research paper text:
{paper_text}
"""

            response = client.chat.completions(
                model="sarvam-105b",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000,
                reasoning_effort=None,
            )


            summary = response.choices[0].message.content
            print(summary)
            if not summary:
                finish_reason = response.choices[0].finish_reason
                st.error(
                    f"Sarvam returned no text. Finish reason: {finish_reason}. "
                    "Try a shorter paper or check the token limit."
                )
                st.stop()
            st.success("Your paper explanation is ready!")
            st.markdown(summary)

            st.download_button(
                "⬇️ Download explanation",
                data=summary,
                file_name="paper_explanation.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.caption("Powered by Sarvam AI • Built for curious minds")
