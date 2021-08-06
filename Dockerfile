FROM python:3.8

COPY . /app/

EXPOSE 8501

WORKDIR /app/

RUN pip install -r requirements.txt

CMD streamlit run app.py