import subprocess
import os


def convert(inputfile: str, outputfile: str, **kwargs):
    """Convert a file to another format."""
    
    inplace=False

    tags = [f"{key}={value}" for key, value in kwargs.items()]

    args = []

    for index in range(len(tags)):
        args += ["-metadata"] + [tags[index]]
    
    
    
    webp=inputfile.replace(inputfile.split(".")[-1], "webp")
    jpg=inputfile.replace(inputfile.split(".")[-1], "jpg")
    png=inputfile.replace(inputfile.split(".")[-1], "png")
    
    if os.path.exists(webp):
        process = ["dwebp", webp, "-o", png]
        process = subprocess.Popen(process)
        if process.wait() != 0:
            raise Exception("Error converting image file")
        os.remove(webp)
    elif os.path.exists(jpg):
        process = ["ffmpeg", "-i", jpg, png]
        process = subprocess.Popen(process)
        if process.wait() != 0:
            raise Exception("Error converting image file")
        os.remove(jpg)
    
    if inputfile==outputfile:
        inputfile = inputfile.replace(inputfile.split(".")[-2], inputfile.split(".")[-2]+"_temp")
        os.rename(outputfile, inputfile)
        inplace=True
    

    process = ["ffmpeg", "-i", inputfile]
    process+=["-i",png,"-map","0:a","-map","1:0","-c","copy","-id3v2_version","3","-metadata:s:v","title=\"Album cover\"","-metadata:s:v","comment=\"Cover (front)\""] 
    process+= args + [outputfile]

    command = ""

    for part in process:
        command += part + " "

    print(command)

    process = subprocess.Popen(process)
    if process.wait() != 0:
        raise Exception("Error converting file")
    os.remove(inputfile)
    os.remove(png)
    
    return outputfile
