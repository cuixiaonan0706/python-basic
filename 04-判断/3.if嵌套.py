input_ticket=input('是否有车票？请输入t(有车票)或f(没车票)：')
if input_ticket=='t':
    has_ticket=True
elif input_ticket=='f':
    has_ticket=False
else:
    print('输入有误，请重新输入！')
knife_length=int(input('刀的长度(cm)：'))
if has_ticket == True:
    print('有车票，可以开始安检……\n……')
    if knife_length>20:
        print('刀的长度超过20厘米，不允许上车')
    elif knife_length <= 20:
        print('安检通过，请上车！祝您旅途愉快！')
else:
    print('没有车票，不允许进门安检！请购买车票！')