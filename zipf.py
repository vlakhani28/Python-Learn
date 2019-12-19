import zipfile
fp = zipfile.ZipFile("testzip.zip")
fp.namelist()
fp.extractall()

