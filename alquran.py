# coding:utf8
"""
untuk para kang recode mohong authornya di cantumkan
Ya bukan di pelajari mlh di recode
"""
import time,os,sys,re,threading
import subprocess as sp
try:
   from tqdm import tqdm
   import requests as req
   import requests
   from bs4 import BeautifulSoup as bs
except ImportError:
    sp.call('pip2 install tqdm bs4 requests',shell=True, stderr=sp.STDOUT)
#=---data--=
header=({'User-Agent':'Mozillla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'})

#=---data---=

G='\033[92m'
P='\033[97m'
R='\033[91m'
X='\033[90m'

link=[]
nam=[]
ukur=[]

def banner():
    os.system('clear')
    print """
{}   ▒▒{}██████{}▒▒▒▒▒▒{} -{} 30 Juz Downloader
{}   ▒▒{}██{}▒▒{}█████{}▒▒▒{} -{} Abdurrahman-as-sudais
{}   ▒▒{}██{}▒▒▒▒▒{}██{}▒▒▒{} -{} By Muhammad Ikbal
{}   ▒▒{}█████{}▒▒{}██{}▒▒▒{} -{} version 1.0
{}   ▒▒▒▒▒{}██████{}▒▒▒

    {}1.{}Lihat surah
    {}2.{}update
    {}3.{}info
    {}0.{}keluar
   """.format(X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,P,G,P,G,P,G,P)
    menu()
def menu():
    ijo=raw_input(G+'   ["] '+P+'pilih: ')
    if ijo=='1':main()
    elif ijo=='2':
	n=raw_input(G+'   [?] '+P+'yakin(y/n): ')
	if n in ['y','Y']:
	   print G+"   [*]"+P+" Tunggu sebentar jangan keluar nanti error."
    	   sp.call('cd ..;rm -rf 30-Juz',shell=True, stderr=sp.STDOUT)
	   sp.call('git clone https://github.com/Maoundis/30-Juz',shell=True, stderr=sp.STDOUT)
	   sp.call('cd 30-Juz',shell=True, stderr=sp.STDOUT)
	   sp.call('python2 alquran.py',shell=True, stderr=sp.STDOUT)
	else:menu()
    elif ijo=='3':info()
    elif ijo=='0':sys.exit()
    else:banner()

def main():
  try:
    print '{}   [{}*{}]{} memuat surah ...'.format(G,X,G,P)
    url="https://islamdownload.net/124129-download-murottal-mp3-abdurrahman-as-sudais.html"
    data=requests.get(url).text
    parser=bs(data,'html.parser')
    et=parser.findAll('a')
    ha=parser.findAll('div',{'align':'right'})
    b=0
    ukur.append('hai')
    for ai in ha:
        ukur.append(ai.text)
    link.append('hai')
    nam.append('hai')
    print '\n      '+G+25*'-'
    for go in et:
        o=go.get('href')
        if 'SURAT' in o:
           link.append(o)
    	   b+=1
	   hail=hai=o[o.find('_')-0:].replace('%27','').replace('.mp3','').replace('SURAT','').replace('__','').replace('_',' ')
           hai=(o[o.find('_')-0:].replace('%27','').replace('.mp3','').replace('SURAT','').replace('_',' ').replace('27T','T').replace('27A','A')+'\n'+'      '+G+25*'-').lower()
	   nam.append(hail)
	   print X+'      ['+G,b,X+']'+P+hai
        else:pass

    selet=int(raw_input(G+'\n   ["]'+P+' piligan:  '))
    if selet=='':main()
    elif selet=='0':main()
    elif selet>len(link):main()
    else:
        print """
         {}[•] {}surah: {}
         {}[•] {}ukran: {}
         {}----------------------------
        """.format(G,P,nam[selet].lower(),G,P,ukur[selet],G)
        don=raw_input('   '+G+'[+]'+P+' Download'+R+'(y/n): '+P)
        if 'y'==don:
           file=raw_input(G+'   [+] '+P+'save file: ').replace('.mp3','').replace('.mp4','')
	   gokil=req.get(link[selet],headers=header)
	   chunk_size=1024
	   total_size=int(gokil.headers['Content-Length'])
           with open(file+'.mp3','wb') as f:
	     for fdata in tqdm(desc=G+'   [*] '+nam[selet].lower().replace('al ','')+P,iterable = gokil.iter_content(chunk_size = chunk_size),total = total_size/chunk_size, unit = 'kb',ncols=45,ascii=True):
                f.write(fdata)
           print G+'   [+] '+P+'selesai nama: '+file+'.mp3'
           lagi=raw_input(G+'   [?]'+P+' download lagi'+R+'(y/n): '+P)
           if 'y'==lagi:
               banner()
	   else:sys.exit()
        else:banner()
  except Exception as F:
       print G+"   ["+R+"!"+G+"]"+P+" Jaringan Error"
       raw_input(G+'   {•}-'+P+'Enter kembali ke menu ...')

 
def info():
    print """
\t  {}_______________________________
\t [{}:::::::::::{}informasi{}:::::::::::{}]
\t  -------------------------------
\t{}
\t   created      21-agustus-2019
\t   author       Muhammad Ikbal
\t   ig:          @ikbal_rr
\t
\t   thanks_to    CRABS
\t   report       @R_ikbal102
\t   {}youtube{}      Cyber Mandar
\t
\t {}---------------------------------

""".format(G,X,G,X,G,P,R,P,X)
    menu() 


if __name__=="__main__":
   banner()
