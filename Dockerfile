FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies (Flask)
RUN pip install flask

# Copy the app code into the image
COPY app.py /app/app.py

# Expose port 5000 (for Flask)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
