# Use a lightweight Python image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy requirements first for efficient caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Install missing libraries for OpenCV/Streamlit rendering
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Copy app code into container
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
