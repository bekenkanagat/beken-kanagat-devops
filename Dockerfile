FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
RUN python -m py_compile main.py
EXPOSE 8000
CMD ["python", "-u", "main.py"]
