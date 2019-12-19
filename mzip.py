import zipfile
fp = zipfile.ZipFile("newtest.zip","a")
fp.write("zip.py",compress_type = zipfile.ZIP_DEFLATED)
