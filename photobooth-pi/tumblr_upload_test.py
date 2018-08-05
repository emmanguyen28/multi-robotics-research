import pytumblr

client = pytumblr.TumblrRestClient(
    'lxfsEd0tRSPFYjEymv92trQrJqynq2izOOkbNt2wO9EzkWEZfX',
    'DjhY2cP8yKigHLTRdDu8vMi1OdKOMS7foFKNolJRgyTUdq3V5M',
    'TQdWZj4k57ElbVIsssvGCAXDyK98sTPyCSAlztvTksw4Zou2Ik',  
    'l8sBVG8nSERZcj1WaH3PCQ4lca8fh97an8fhqLptkjiZQxak3s'
)

client.create_photo(
    'emmanguyen28',
    state="published",
    tags=["raspberrypi", "picamera"],
    data="/home/pi/Pictures/joined.gif"
)
print("uploaded") 
