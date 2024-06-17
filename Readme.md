# Car Quality Evaluation 

This project is a web application built by **Streamlit** for evaluating car quality. It uses a [Random Forest Classifier](https://www.kaggle.com/code/prashant111/random-forest-classifier-tutorial) model trained on the [Car Evaluation Data Set](https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set) from Kaggle. The model was built by [Prashant Banerjee](https://www.kaggle.com/prashant111).

## Demo 

You can view a demo of the web application on YouTube:

[![Demo](http://img.youtube.com/vi/G3D9sThPSRk/0.jpg)](https://youtu.be/G3D9sThPSRk)


## Live Demo
You can try this live demo of the application: [Here](https://veraz00-car-quality-evaluation.streamlit.app/)

## Deployment

To deploy the web application on your local machine, follow these steps:

```bash
# Clone the repository
git clone https://github.com/veraz00/Car-Quality-Evaluation.git

# Create a virtual environment
python3 -m venv car_env 

# Activate the virtual environment
source car_env/bin/activate 

# Navigate to the project directory
cd <path to current project>

# Install the dependencies
pip3 install . 
# pip3 install .[dev]


# Run the application
streamlit run main.py
```
