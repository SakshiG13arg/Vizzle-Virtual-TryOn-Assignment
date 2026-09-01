import os
import time
from pathlib import Path

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vizzle Virtual Try-On Evaluation", layout="wide")

st.title("Vizzle Virtual Try-On")
st.caption("Virtual Try-On Model Evaluation Interface")

st.markdown("""
This interface is used to organize person/garment inputs and record
virtual try-on evaluation results. Model inference is kept separate
so that results from a hosted VTON model can be evaluated without
pretending that the local laptop generated them.
""")

col1, col2 = st.columns(2)

with col1:
    person_file = st.file_uploader(
        "Upload Person Image",
        type=["jpg", "jpeg", "png"],
        key="person"
    )
    if person_file:
        st.image(Image.open(person_file), caption="Person", use_container_width=True)

with col2:
    garment_file = st.file_uploader(
        "Upload Garment Image",
        type=["jpg", "jpeg", "png"],
        key="garment"
    )
    if garment_file:
        st.image(Image.open(garment_file), caption="Garment", use_container_width=True)

st.divider()

category = st.selectbox(
    "Clothing Category",
    ["Saree", "Kurti", "Lehenga", "Top", "T-shirt",
     "Jumpsuit", "Coat", "Shirt", "Jeans", "Trousers"]
)

st.subheader("Evaluation Record")

c1, c2, c3 = st.columns(3)
with c1:
    model = st.text_input("Model", "IDM-VTON")
with c2:
    time_seconds = st.number_input("Observed time (seconds)", min_value=0.0, step=0.1)
with c3:
    cost_inr = st.number_input("Direct test cost (INR)", min_value=0.0, step=0.01)

scores = {}
for label in ["Fit", "Drape", "Texture", "Body Preservation",
              "Face Preservation", "Artifact Control"]:
    scores[label] = st.slider(label, 1, 10, 5)

accuracy = sum(scores.values()) / len(scores)
st.metric("Overall visual score", f"{accuracy:.2f}/10")

st.info(
    "Only enter measurements and scores that were actually observed. "
    "Do not invent latency, cost, or quality results."
)

if st.button("Save Evaluation Record"):
    out = Path("evaluation")
    out.mkdir(exist_ok=True)
    csv_path = out / "results.csv"
    new_file = not csv_path.exists()

    import csv
    row = {
        "Category": category,
        "Model": model,
        **scores,
        "Accuracy": round(accuracy, 2),
        "Time_Seconds": time_seconds,
        "Cost_INR": cost_inr,
    }
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if new_file:
            writer.writeheader()
        writer.writerow(row)

    st.success(f"Saved {category} / {model} evaluation to {csv_path}")
