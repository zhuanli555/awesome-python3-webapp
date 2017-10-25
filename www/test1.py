from PIL import Image


im = Image.open("1.ico")
im = im.convert("P")
his = im.histogram()
values = {}
for i in range(0, 256):
    values[i] = his[i]

# 排序，x:x[1]是按照括号内第二个字段进行排序,x:x[0]是按照第一个字段
temp = sorted(values.items(), key=lambda x: x[1], reverse=True)
for j, k in temp[:10]:
     print(j, k)

im2 = Image.new("P", im.size, 255)
for y in range(im.size[1]):
    # 获得y坐标
    for x in range(im.size[0]):

        # 获得坐标(x,y)的RGB值
        pix = im.getpixel((x, y))

        # 这些是要得到的数字
        # 220灰色，227红色
        if pix == 182 or pix == 189:
            # 将黑色0填充到im2中
            im2.putpixel((x, y), 0)
# 生成了一张黑白二值照片
im2.show()