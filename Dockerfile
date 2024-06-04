FROM python:3.12.3-bullseye

# Set the working directory
WORKDIR /app

# Copy the project files into the working directory
COPY . .

# install poetry and dependencies
RUN pip install poetry

# Set python version for poetry
RUN poetry env use python3.12

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-root


# Run main.py when the container launches
CMD ["poetry", "run", "fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]

# Make port 8000 available to the world outside this container
EXPOSE 8000