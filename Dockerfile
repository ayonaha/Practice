FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the local repo to the container
COPY . /app

# Install the MySQL driver dependency
# RUN apt-get install python3-pymysql

# Install the required packages
RUN pip install -r requirements.txt

# Expose the container port
EXPOSE 8000

# Run the command to start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]