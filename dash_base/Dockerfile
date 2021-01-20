FROM python

RUN apt update -y
RUN apt upgrade -y

RUN apt install -y nano vim

RUN pip install dash plotly pandas dash_bootstrap_components

RUN mkdir /app

EXPOSE 8050
