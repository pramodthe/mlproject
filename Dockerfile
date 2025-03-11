# Use Python 3.9 on Debian as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app/

# Install system dependencies
RUN apt-get update && \
    pip3 install awscli && \
    pip3 install -r requirements.txt


EXPOSE 8501

CMD streamlit run app.py server=“0.0.0.0”