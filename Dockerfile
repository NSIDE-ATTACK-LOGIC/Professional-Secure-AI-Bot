FROM python:3.12

WORKDIR /app

ARG OPENAI_API_KEY

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

COPY . /app

RUN pip install .

RUN python -m spacy download en_core_web_sm

EXPOSE 5000

CMD ["secure_ai_bot"]
