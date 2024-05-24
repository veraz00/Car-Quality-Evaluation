import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import altair as alt

app_mode = st.sidebar.selectbox("Select Page", ["Home", "Prediction"])
data_path = "./data/car_evaluation.csv"
model_path = "./model/RandomForest.pkl"
mapping = True

if app_mode == "Home":
    st.title("Car Quality Evaluation")
    st.write("App realized by: veraz00")

    st.image("./assets/images/1.jpg")
    st.subheader("Dataset")
    df = pd.read_csv(data_path)
    df.drop("doors", axis=1, inplace=True)
    head_map = {
        "buying": "Buying Price",
        "lug_boot": "Size of Luggage Boot",
        "safety": "Safety",
        "persons": "Number of Persons to Carry",
        "class": "Evaluation Result",
    }

    df = df.rename(columns=head_map)
    if mapping:
        val_map = {
            "vhigh": "very high",
            "unacc": "unacceptable",
            "med": "medium",
            "vgood": "very good",
            "acc": "acceptable",
        }
        df = df.map(lambda x: val_map[x] if x in val_map.keys() else x)

    st.write(df.head())
    # add explanation for head of data and content ??
    st.subheader("Safety VS Class")


    c = (
        alt.Chart(df[["Safety", "Evaluation Result"]])
        .mark_bar()
        .encode(x="Safety", y="count()", color="Evaluation Result")
        .interactive()
    )
    st.altair_chart(c, use_container_width=True)

elif app_mode == "Prediction":

    st.subheader(
        "We're almost there! Just a few more details about your car and we can get started on the evaluation."
    )
    st.image("./assets/images/evaluation.jpg")
    st.sidebar.header("Information about the car :")

    buying_dict = {"very high": 1, "high": 2, "medium": 4, "low": 3}
    maint_dict = {"very high": 1, "high": 2, "medium": 4, "low": 3}
    persons_dict = {"2": 3, "4": 2, "5+": 1}
    lug_boot_dict = {"small": 2, "medium": 1, "big": 3}
    safety_dict = {"low": 1, "medium": 3, "high": 2}

    class_dict = {
        "unacc": "Unacceptable",
        "acc": "Acceptable",
        "good": "Good",
        "vgood": "Very Good",
    }

    buying_val = st.sidebar.radio("Buying Price", tuple(buying_dict.keys()))
    maint_val = st.sidebar.radio("Past Maintenance Fee", tuple(maint_dict.keys()))
    persons_val = st.sidebar.radio(
        "Number of Persons to Carry", tuple(persons_dict.keys())
    )
    lug_boot_val = st.sidebar.radio(
        "Size of Lugguage Boot", tuple(lug_boot_dict.keys())
    )
    safety_val = st.sidebar.radio("Safety Level", tuple(safety_dict.keys()))

    if st.sidebar.button("Evaluate"):

        model = pickle.load(open(model_path, "rb"))
        input_data = np.array(
            [
                buying_dict[buying_val],
                maint_dict[maint_val],
                persons_dict[persons_val],
                lug_boot_dict[lug_boot_val],
                safety_dict[safety_val],
            ]
        ).reshape(1, -1)

        prediction = model.predict(input_data)
        prediction_val = class_dict[prediction[0]]
        if prediction_val == "Very Good":
            file_name = "very_good.gif"
        elif prediction_val == "Unacceptable":
            file_name = "unacceptable.gif"
        else:
            file_name = "drive-safe.gif"

        file = open(f"./assets/images/{file_name}", "rb")
        contents = file.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file.close()

        if prediction_val == "Very Good":
            st.success(f"Great! The car quality is: {prediction_val}!")

        elif prediction_val == "Unacceptable":
            st.error(f"Sadly, The car quality is: {prediction_val}!")

        else:
            st.warning(f"The car quality is: {prediction_val}")
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" \
                    alt="cat gif" style="width: 100%; height: auto;">',
            unsafe_allow_html=True,
        )
