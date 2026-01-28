import re

#print(re.match([a-zA-Z0-9]{5,}[@]((gmail)|(yahoo))[.]((com)|(in)),email))\

def email_vali(email):
    pattern = r"[a-zA-Z0-9]{5,}[@]((gmail)|(yahoo)|(hotmail))[.]((com)|(in)|(us)|(uk))"
    return re.match(pattern,email)

'''email = 'shettysathwika6@gmail.com'
if email_vali(email) is not None:
    print('valid')
else:
    print('not valid')
''' 
