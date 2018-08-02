import sys

totalInput = sys.stdin.read()
line = ""
formalInput = []
for char in totalInput:
    if char != '\n':
        line += char
    else:
        formalInput.append(line)
        line = ""
newFile = False
addedFiles = []
modifiedFiles = []
deletedFiles = []
for lines in formalInput:
    if lines[0:10] == "diff --git":
        fileName = lines.split(' b/')[1]
        newFile = True
    else:
        newFile = False
    tracked = False
    if not newFile:
       if lines == "+++ /dev/null": #deleted
           deletedFiles.append(fileName)
           tracked = True
       if lines == "--- /dev/null": #added
           addedFiles.append(fileName)
           tracked = True
       if lines[0:2] == "@@" and not tracked: #modified
           modifiedFiles.append(fileName)
           tracked = True

print("Added Files (" + str(len(addedFiles)) + "): " + ', '.join(addedFiles))
print("Deleted Files (" + str(len(deletedFiles)) + "): " + ', '.join(deletedFiles))
print("Modified Files (" + str(len(modifiedFiles)) + "): " + ', '.join(modifiedFiles))
