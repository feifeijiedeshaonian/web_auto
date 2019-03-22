import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def new_report(test_report):

    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report+'\\'+fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new


def send_email(file_new):

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    username = 'zhangkai@tjmeiteng.com'
    password = '960811kai'
    sender = 'zhangkai@tjmeiteng.com'
    receiver = ['wanghui01@tjmeiteng.com']
    subject = "自动化测试报告"
    msg = MIMEText(mail_body, 'html', 'utf-8') 
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'zhangkai@tjmeiteng.com<zhangkai@tjmeiteng.com>'
    msg['To'] = ";".join(receiver) 
    smtp = smtplib.SMTP()    
    smtp.connect('smtp.tjmeiteng.com')
    smtp.login(username, password)    
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()


if __name__ == "__main__":   
    
    # 测试用例的路径
    test_dir = 'C:\\Users\\LENOVO\\Desktop\\python\\美腾\\zhiyou_guanli\\创建正式项目与子项目'
    # 知道测试报告的路径
    test_report = "E:\\html"
    discover = unittest.defaultTestLoader.discover(test_dir, 
                                                   pattern='test*.py')
    filename = test_report+'\\' + 'result1.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(discover)
    fp.close() 
    # 取最新测试报告
    new_report = new_report(test_report)
    # 发送邮件，发送最新测试报告html
    send_email(new_report)
