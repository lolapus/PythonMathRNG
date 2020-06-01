import math
import psutil
import uptime
# Estimated time since Boot
mainTime = uptime.uptime()
# How much memory is available
Mem = psutil.virtual_memory().free
# Multiply them to get a random seed each time
mainTime *= Mem


# If your numbers aren't random enough mix the seed
def MixSeed():
    global mainTime
    mainTime = 0
    mainTime = uptime.uptime()
    mainTime *= psutil.virtual_memory().free


# Accepts any positive number for the seed argument and any number for the range argument.
def RNG(numrange, seed=0):
    global mainTime
    mainTime += psutil.virtual_memory().free

    if seed < 0:
        raise ValueError("The seed is not greater than 0")
    else:
        if seed > 0:
            return math.fabs(numrange)*(math.sin(math.pow(20*seed, math.pi))*math.sin(math.pow(4*seed, math.e)))
        else:
            return math.fabs(numrange) * (math.sin(math.pow(20 * mainTime, math.pi)) * math.sin(math.pow(4 * mainTime, math.e)))


# Returns a table of random numbers
def batchRNG(numrange, totalnumbers):
    collection = []
    for i in range(1, totalnumbers+1):
        collection.append(RNG(numrange))
    return collection


# Check if an array has duplicate items
def Duplicates(array):
    if len(array) == len(set(array)):
        return False
    else:
        return True


# Generate a random image with the optional seed parameter
def randomImage(sizeX, sizeY, seed=0):
    from PIL import Image, ImageColor
    im = Image.new('1', (sizeX, sizeY))
    for x in range(0, sizeX):
        for y in range(0, sizeX):
            if RNG(1, x*y*seed) >= 0:
                im.putpixel((x, y), ImageColor.getcolor('white', '1'))
            else:
                im.putpixel((x, y), ImageColor.getcolor('black', '1'))
    return im

