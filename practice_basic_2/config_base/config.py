from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env file
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# AWS Config
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
