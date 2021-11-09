FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . /app/

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

# Expose port 80
EXPOSE 80

# Run app.py at container launch
# gunicorn -k uvicorn.workers.UvicornWorker -b :5000 main:app
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", ":5000", "main:app"]
