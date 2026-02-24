#Use Python 
FROM python:3.11.4-slim

# set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY  requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the application code
COPY . . 

# Expose the application code
EXPOSE 8000

#Command to start Fastapi application
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]