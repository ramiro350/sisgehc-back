FROM python:3.12.3-slim

# Install required dependencies, including git
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev git

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000


# Define the entrypoint command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
