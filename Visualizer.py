import requests
import sys

# 0 for only top perspective
# other for tri perspective
def GetSvgBytes(alg:str, type:int = 0):
    # 先用着别人的api八
    root_str = "http://cube.crider.co.uk/visualcube.php?fmt=svg&size=200&view=plan&case="
    if type != 0:
        root_str = "http://cube.crider.co.uk/visualcube.php?fmt=svg&size=200&alg="
    response = requests.get(root_str+alg)
    response.raise_for_status()
    svg_str = response.text
    svg_bytes = bytearray(svg_str, encoding='utf-8')
    return svg_bytes

