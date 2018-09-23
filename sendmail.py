#!/usr/bin/python
# encoding: GBK
"""
@author: lwqhp
Contact: �����ʼ�
@file: sendmail.py
@time:2018/9/17 1:31
"""
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os
from testdata.getpath import GetTestConfig


class MyMail:
    def __init__(self, mail_config_file):
        config = configparser.ConfigParser()
        config.read(mail_config_file)
        self.smtp = smtplib.SMTP_SSL()
        self.login_user = config.get("SMTP", 'login_user')
        self.login_pwd = config.get("SMTP", 'login_pwd')
        self.from_addr = config.get("SMTP", 'from_addr')
        self.to_addrs = config.get("SMTP", 'to_addrs')
        self.host = config.get("SMTP", 'host')
        self.port = config.get("SMTP", 'port')


    # ���ӵ�������
    def connect(self):
        # self.smtp.set_debuglevel(True)
        # self.smtp.starttls()
        self.smtp.connect(self.host, self.port)

    # ��½�ʼ�������
    def login(self):
        try:
            self.smtp.login(self.login_user, self.login_pwd)
        except Exception as e:
            print('%s' % e)

    #�����ʼ�
    def sendmail(self, mail_subject, mail_content, attachment_path_set):
        #����MIMEMultipart������Ϊ������
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(eval(self.to_addrs))
        msg['Subject'] = mail_subject

        #����ʼ�����
        #�����_charset����Ϊgbk,��#-*-coding:GBK ����һ�£������ʼ���������
        content = MIMEText(mail_content, "html", _charset='gbk')

        msg.attach(content)

        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path): #�����������
                type, coding = mimetypes.guess_type(attachment_path)
                if type == None:
                    type = 'application/octet-stream'

                major_type, minor_type = type.split('/',1)
                with open(attachment_path, 'rb') as file:
                    if major_type == 'text':
                        attachment = MIMEText(file.read(), _subtype=minor_type,_charset='GB2312')
                    elif major_type == 'image':
                        attachment = MIMEImage(file.read(), _subtype=minor_type)
                    elif major_type == 'application':
                        attachment = MIMEApplication(file.read(),_subtype=minor_type)
                    elif major_type == 'audio':
                        attachment = MIMEAudio(file.read(), _subtype=minor_type)

                #�޸ĸ�������
                attachment_name = os.path.basename(attachment_path)
                attachment.add_header('Content-Disposition', 'attachment', filename=('gbk', '', attachment_name))
                #�����gbk����˸���Ϊ��������ʱ����ʾ���Ե�����
                msg.attach(attachment)

        #�õ���ʽ����������ı�
        full_text = msg.as_string()
        #�����ʼ�
        self.smtp.sendmail(self.from_addr, eval(self.to_addrs), full_text)

    #�˳�
    def quit(self):
        self.smtp.quit()


if __name__ == '__main__':
    mymail = MyMail(GetTestConfig('mail.conf'))
    mymail.connect()
    mymail.login()
    mail_content = 'hi,����'
    mail_title = '[����]����'

    attachments = set([GetTestConfig('mail.conf')])
    mymail.sendmail(mail_title, mail_content, attachments)
    mymail.quit()