import os,sys

embedStr = "local EmbeddedModules = {\n"
files = os.listdir("modules")

fileName = sys.argv[1] if len(sys.argv) > 1 else "out.lua"

def readfile(path):
    with open(path,"r") as file:
        str = file.read()
    return str

def addModuleFile(path):
    global embedStr

    moduleName = os.path.splitext(os.path.basename(path))[0]
    moduleSource = readfile(path)

    embedStr = (
        f'{embedStr}["{moduleName}'
        + '"] = function()\n'
        + moduleSource
        + '\nend,\n'
    )

for filename in files:
    addModuleFile(f"modules/{filename}")

embedStr = embedStr + "}"
embedStr = embedStr + "\n" + readfile("main.lua")

with open(f'{fileName}.lua',"w") as file:
    file.write(embedStr)