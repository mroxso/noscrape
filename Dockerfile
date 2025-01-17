FROM python:3.11

# Set the working directory
WORKDIR /app

COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "main.py"]