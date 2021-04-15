str = 'X-DSPAM-Confidence:0.8475'

isCollon = str.find(':')
subStr = str[isCollon + 1:]

subStrFloat = float(subStr)
print(subStrFloat)