from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import smtplib
from pyfiglet import Figlet 

figlet = Figlet(font='slant')
print(figlet.renderText('Mail CLI Hoşgeldiniz'))

def mail_gonder(username,password,servis,kime,konu,mesaj):
    host = ''
    port = ''
    if servis == 'Gmail':
        host = 'smtp.gmail.com'
        port = 587
    try:
        email = smtplib.SMTP(host,port)
        email.ehlo()
        email.starttls()
        email.login(username,password)
        email.sendmail(username,kime,f"Subject: {konu}\n\n {mesaj}")
        email.quit()
        return True
    except:
        return False


sorular = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'Mail servisine bağlanacağınız mail adresi',
    },
    {
        'type':'password',
        'name':'password',
        'message':'Mail servisi için şifrenizi girin'
    },
    {
        'type':'checkbox',
        'name':'servis',
        'message':'Hangi servisi kullanıyorsunuz',
        'choices':[
            {'name':'Gmail'},
            {'name':'Yandex','disabled':'Henüz bu servis kullanılabilir değil'}
        ]
    },
    {
        'type':'input',
        'name':'kime',
        'message':'Mail kime gidecek'
    },
    {
        'type':'list',
        'name':'konu',
        'message':'Konu nedir',
        'choices':[
            'Bilgilendirme',
            'Ücret Takibi',
            {
                'name':'Fiyat Teklifi',
                'disabled':'Henüz bu aşamaya gelmedik'
            }
        ]
    },
    {
        'type':'editor',
        'name':'mesaj',
        'message':'Mesajınız: ',
        'eargs' :
        {
            'editor':'default',
            'ext':'.py'
        }
    },
    {
        'type':'confirm',
        'name':'onay',
        'message':'Mail gönderimini onaylıyor musunuz'
    }
]

cevaplar = prompt(sorular)
if cevaplar['onay']:
    flag = mail_gonder(cevaplar['username'],cevaplar['password'],cevaplar['servis'][0],cevaplar['kime'],cevaplar['konu'].encode(),cevaplar['mesaj'].encode())
    if flag:
        print('OK')
    else:
        print('ERR!')
else:
    print('Mail gönderimi iptal edildi')