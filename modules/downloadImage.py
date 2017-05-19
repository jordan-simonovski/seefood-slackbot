import urllib2

def getImage(imageUrl):
    isHotdogImage = urllib2.urlopen(imageUrl)
    return isHotdogImage

