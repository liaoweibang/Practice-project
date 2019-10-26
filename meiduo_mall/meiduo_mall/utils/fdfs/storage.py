from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework import serializers


def fdfs_send_filebuffer(file_buffer):
    """
    上传文件数据到fdfs
    :param file_buffer: 文件数据 --> 字节数据
    :return: 上传后的结果
    """
    # 1、构建fdfs链接对象
    conn = Fdfs_client(settings.FDFS_CONF_PATH)
    # 2、调用上传函数
    res = conn.upload_by_buffer(file_buffer)
    # 3、返回结果
    return res


# 自定义存储后端
# 1、继承自django.core.files.storage.Storage: django开放给我们的自定义的存储后端基础类
class FdfsStorage(Storage):

    def _open(self, name, mode='rb'):
        """
        打开本地文件；
        :param name: 文件名字
        :param mode: 打开文件文件权限
        :return: 本地打开的文件对象
        """
        # 咱们的后台管理业务，不需要将前端传来的图片文件保存django本地
        return None


    def _save(self, name, content, max_length=None):
        """
        保存前端传来的文件（上传fdfs文件）
        :param name: 文件名字
        :param content: 文件对象 --> 序列化器校验之后得到的文件对象
        :param max_length: 最大长度
        :return: 返回文件的标示 --> fdfs保存文件之后给我们的文件id --> 保存mysql
        """
        res = fdfs_send_filebuffer(content.read())
        if res['Status'] != "Upload successed.":
            raise serializers.ValidationError("上传失败")

        # 返回的结果就是用于相关字段在mysql的保存数据
        return res['Remote file_id']


    def url(self, name):
        """
        序列化返回的当前文件字段的结果
        :param name: "文件名" --> 本质就是当前字段在mysql数据库中存储的值（用来标示一个文件的）
                      group1/M00/00/02/CtM3BVrOMI-AVPWrAAAPN5YrVxw2187795
        :return: 返回的结果就是该字段序列化后的结果
        """

        # http://image.meiduo.site:8888/group1/M00/00/02/CtM3BVrOMI-AVPWrAAAPN5YrVxw2187795
        return settings.FDFS_URL + name

    def exists(self, name):
        """
        django存储后端使用该函数，判断保存的文件是否存在
        :param name: 文件名称
        :return: 布尔值
        """
        # return True # 保存的文件存在

        # 统一上传fdfs
        return False # 保存的文件不存在










