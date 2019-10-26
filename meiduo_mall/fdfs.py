


from fdfs_client.client import Fdfs_client

# 链接对象
conn = Fdfs_client('./meiduo_mall/client.conf')

# 使用链接对象，上传文件

# 上传"本地"文件
res = conn.upload_by_filename('./1.png')

# 上传文件,传入的参数是"文件数据"
# conn.upload_by_buffer(f.read())


print(res)



def fun():
    pass
