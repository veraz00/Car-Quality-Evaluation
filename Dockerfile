# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /src

COPY ./src /src
COPY ./pyproject.toml /pyproject.toml
COPY ./main.py /main.py 


RUN pip install /.


# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the command to start the Streamlit app
CMD ["streamlit", "run", "/main.py"]