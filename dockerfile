FROM python:3.11

WORKDIR /usr/apps/tcc

COPY requirements.txt ./
# RUN pip install pip --upgrade
# RUN pip install pyopenssl --upgrade
RUN pip install firebase-admin --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${API_PORT}

CMD ["python3","application.py"]