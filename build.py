import os,sys

embedStr = "local EmbeddedModules = {\n"
files = os.listdir("modules")

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = "out.lua"

def readfile(path):
    file = open(path,"r")
    str = file.read()
    file.close()
    return str

def addModuleFile(path):
    global embedStr

    moduleName = os.path.splitext(os.path.basename(path))[0]
    moduleSource = readfile(path)

    embedStr = embedStr + '["' + moduleName + '"] = function()\n' + moduleSource + '\nend,\n'

for filename in files:
    addModuleFile("modules/" + filename)

embedStr = embedStr + "}"
embedStr = embedStr + "\n" + readfile("main.lua")

file = open(f'{fileName}.lua',"w")
file.write(embedStr)
file.close()