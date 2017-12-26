import os
from os.path import join,dirname
from dotenv import load_dotenv

dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)


C_KEY=os.environ.get('Ckey')
C_SECRET=os.environ.get('Csecret')
A_KEY=os.environ.get('Akey')
A_SECRET=os.environ.get('Asecret')