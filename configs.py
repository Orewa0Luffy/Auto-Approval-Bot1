from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "20793620"))
    API_HASH = getenv("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    BOT_TOKEN = getenv("BOT_TOKEN", "7968721529:AAH6akAWG8DRXb5rPe3Rf0PcKhejNjubkJY")
    
    # Your Force Subscribe Channel Id
    CHID = int(getenv("CHID", ""))  # Make the bot admin in this channel
    
    # Bot owners (use space-separated user IDs in env)
    SUDO = list(map(int, getenv("SUDO", "6853851676").split()))
    
    # MongoDB connection URI
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()
