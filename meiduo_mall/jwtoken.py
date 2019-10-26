

import json
import base64
import hashlib,hmac


header = {
 'typ': 'JWT',
 'alg': 'HS256'
}
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
header = json.dumps(header) # 字符串
header = base64.b64encode(header.encode())
print("header: ", header)


payload = {
 "name": "John Doe",
 "admin": True
}
# eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9
payload = json.dumps(payload)
payload = base64.b64encode(payload.encode())
print("payload: ", payload)


# 生成签名
# signature = sha256(密钥,  (header + payload))
# 1、签名信息的构建
msg = header + b'.' + payload # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9
# 2、sha256加密
SECRET_KEY = b'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='
signature = hmac.new(SECRET_KEY, msg, digestmod=hashlib.sha256).hexdigest()
print("signature: ", signature)

# JWT
JWT_Token = header.decode() + '.' + payload.decode() + '.' + signature
print("JWT_Token: ", JWT_Token)



# 模拟浏览器请求，携带token

# 用户数据没有粗那该
# jwt_token_from_browser = JWT_Token
jwt_token_from_browser = "abc" + JWT_Token

# 如何验证数据集的完整性（数据是否被篡改）
# 对用户携带对header和payload重复加密。加密后得到对新的签名和用户对签名做比对
# 如果一致则用户数据没有篡改，否则篡改了
header_from_browser = jwt_token_from_browser.split(".")[0]
payload_from_browser = jwt_token_from_browser.split(".")[1]
signature_from_browser = jwt_token_from_browser.split(".")[2]


new_msg = header_from_browser + '.' + payload_from_browser # string
new_signature = hmac.new(SECRET_KEY, new_msg.encode(), digestmod=hashlib.sha256).hexdigest()

# 比对新签名和用户签名是否一致
if new_signature == signature_from_browser:
    print("数据是完整对")
else:
    print("数据被篡改了")


