# Use an official Python runtime as a parent image
FROM python:3.9


# Set the working directory in the container to /usr/src
WORKDIR /usr/src

# Copy the current directory contents into the container at /usr/src
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]