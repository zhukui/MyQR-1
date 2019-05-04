# Code By GhostGuest
from MyQR import myqr


def main():
    message_State = """
    1.静态二维码
    2.动态二维码
    """
    print(message_State)
    State = input("请输出要制作的二维码状态: ")

    if int(State) == 1:
        Static()
    elif int(State) == 2:
        Dynamic()


def Static():
    # 静态二维码
    message = """
    二维码颜色种类：
        1.黑白二维码
        2.彩色二维码
    """
    print(message)
    state = input("请选择二维码颜色：")
    if int(state) == 1:
        blackQR()
    elif int(state) == 2:
        colorQR()


def Dynamic():
    # 动态二维码
    picture_name = input("请输入动图文件名：")
    message = input("请输入要保存的信息：")
    save_name = input("请输入要保存二维码名字：")
    myqr.run(
        words="{}".format(message),
        picture='ImageSources/{}.gif'.format(picture_name),
        colorized=True,
        save_name='{}.gif'.format(save_name),
        save_dir='SaveImages',
    )


def colorQR():
    # 彩色二维码
    picture_name = input("请输入背景照片名称：")
    message = input("请输入要保存的信息：")
    save_name = input("请输入要保存二维码名字：")
    myqr.run(
        words="{}".format(message),
        picture='ImageSources/{}.jpg'.format(picture_name),
        colorized=True,
        save_name='{}.png'.format(save_name),
        save_dir='SaveImages/',
    )


def blackQR():
    # 黑白二维码
    picture_name = input("请输入背景照片名称：")
    message = input("请输入要保存的信息：")
    save_name = input("请输入要保存二维码名字：")
    myqr.run(
        words="{}".format(message),
        picture='ImageSources/{}.jpg'.format(picture_name),
        save_name='{}.png'.format(save_name),
        save_dir='SaveImages/',
    )


main()
