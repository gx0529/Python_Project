from django.db import models

# Create your models here.

# 设计和表对应的类
# 一类
# 图书类
class BookInfo(models.Model):
    # 图书模型类

    # CharField说明是一个字符串， max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期，DateField说明是一个日期类型
    bpub_date = models.DateField()

# 多类
# 英雄人物类
# 英雄名 name
# 性别 hgender
# 年龄 hage
# 备注 hcomment
# 关系属性，建立图书类和英雄人物类之间的一对多关系
class HeroInfo(models.Model):
    """英雄人物类"""
    hname = models.CharField(max_length=20)

    # 性别，BooleanField 说明是bool类型，default指定默认值，False代表男
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 hbook，建立图书类与英雄人物类之间的一对多关系
    # 关系属性对应的表的字段名格式：关系属性名_id
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)







