import smtplib
import random
import time
from email.mime.text import MIMEText


class EmailSender:

    def __init__(self):
        # 设置服务器所需信息
        # 163邮箱服务器地址
        mail_host = 'mail.nike-adidas.com'
        # 163用户名
        mail_user = 'postmaster@nike-adidas.com'
        # 密码(部分邮箱为授权码)
        mail_pass = '123'
        # 邮件发送方邮箱地址
        self.sender = 'postmaster@nike-adidas.com'
        self.receiver = '344126509@qq.com'
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

        self.smtpObj = smtplib.SMTP()
        # 连接到服务器
        self.smtpObj.connect(mail_host, 587)
        self.smtpObj.starttls()
        # 登录到服务器
        self.smtpObj.login(mail_user, mail_pass)

    def send(self, content):
        # 设置email信息
        # 邮件内容设置
        message = MIMEText(content, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = '套利策略通知'
        # 发送方信息
        message['From'] = self.sender
        # 接受方信息
        message['To'] = self.receiver
        # 登录并发送邮件
        try:
            # 发送
            self.smtpObj.sendmail(
                self.sender, self.receiver, message.as_string())
            # 退出

            print('success')
        except smtplib.SMTPException as e:
            print('error', e)


def send_email(content):
    sender = EmailSender()
    sender.send(content=content)

if __name__ == '__main__':
    pass