apt update && apt install python3-pip -y
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000