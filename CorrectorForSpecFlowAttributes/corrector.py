import os

DIRS = [ "/Users/Company/Mobile/Src/Project.Mobile.Core.SpecFlow/Tests/",
         "/Users/Company/Mobile/Src/Project.Mobile.Droid.SpecFlow/Tests/",
         "/Users/Company/Mobile/Src/Project.Mobile.iOS.SpecFlow/Tests/"    ]

ECHO = "True"

old_text1 = 'OneTimeSetUpAttribute'
new_text1 = 'TestFixtureSetUp'

old_text2 = 'OneTimeTearDownAttribute'
new_text2 = 'TestFixtureTearDown'


def replace_text(path):
    if(ECHO == "True"): print "READING.."
    file = open(path, 'r')
    text = file.read()
    file.close
    text = text.replace(old_text1, new_text1)
    text = text.replace(old_text2, new_text2)
    if(ECHO == "True"): print "WRITING.."
    file = open(path, 'w')
    file.write(text)
    file.close()


def replace_attributes_subfolders(dirs):
    for dir in dirs:
        subdirs = os.listdir(dir)
        subdirs.pop(0) # remove '.DS_Store'
        for sub in subdirs:
            for file in os.listdir(dir+sub):
                if (file.endswith(".feature.cs")):
                    if(ECHO == "True"): print dir + sub + "/" + file
                    replace_text(dir + sub + "/" + file)


replace_attributes_subfolders(DIRS)
