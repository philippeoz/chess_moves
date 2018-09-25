FROM python:3.6
 
ENV PYTHONUNBUFFERED 1
 
# -- Pipenv install
RUN set -ex && pip install pipenv --upgrade
 
# -- create app folder on container
RUN set -ex && mkdir /app
 
# -- add scripts
ADD /compose/*.sh /
RUN set -ex && chmod +x /*.sh

WORKDIR /app
 
# -- add pipfiles
ADD Pipfile /
ADD Pipfile.lock /
 
# -- deploy requirements
RUN set -ex && pipenv install --deploy --system