'''from  bs4 import  BeautifulSoup
import requests
import request sınıfı bir adresten veri çekmeye yarar .Siteden ctr+u ya pastığında çıkan şeyi getiri
beautifull spft ise verilen veriye göre parçalama işlemi yapar.Bu parçalama işlemiyle sayfanın başlığını, içeriğini vs. alabiliriz
Genel olarakgörsel bir bot yapılmicak ise bs4 ve request kullanılır.




#request.get web sayfaasından içeriği kaynak kodu olarak çeker.
buradaki r.content çekilmiş olan kaynak kodu temsil eder
source kısmında bautifulsoup sınıfına çekmiş olduğumuz kaynak kodu göndermek
title ya da title.text yazdık title.text yazınca başlığı verdi.Bu bod mantığının çalışabilmesi için lxml sınıfının yüklenmesi gerekiyor pip üzerinden'''
'''32. satırsa strog spM DİVİN AŞAĞISINDAKİ İÇNDEKİ DİV ÇEŞİTLERİ ONLARI DA BELİRTTİK VA İSE AMA 40. SATIRDA İHTİYAÇ DUYMADIK.
 internal eror=while true^
fs.find_all : 54. satırda all dememeizin nedeni siteye v-bak director writers stars kısmının çoğul olması ama puan ve film açıklamasında böyle
bir şey yapmadık tekil olduğu için'''



from  bs4 import  BeautifulSoup
import requests
import webbrowser
r=requests.get("https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm")
source=BeautifulSoup (r.content, "lxml")
#print(source.title.text)
'''incele x path den sonra gelen bağlantının calssını kopyalıyoruz (yukarda oluyor) td idi imdb sayfasında mesela'''
filmler=source.find_all("td",attrs={"class" : "titleColumn"})

for film in filmler :
    film_adi=film.a.text
    film_adresi=film.a.get("href")
    yeniAdres="https://www.imdb.com" + film_adresi

    f = requests.get(yeniAdres)
    fs = BeautifulSoup(f.content, "lxml")
    film_puan = ""
    try:
        film_puan = fs.find("div", attrs={"class": "ratingValue"}).strong.span.text
    except:
        film_puan = "bulunamadı"


    film_aciklama= ""
    try :
        film_aciklama=fs.find("div", attrs={"class": "summary_text"}) .text
    except:
        film_aciklama="açıklama bulunamadı"
    cumle="film Adı: " + film_adi + "\nFilm puanı: "+film_puan + "\nFilm acıklaması: \n " +film_aciklama
    try:
        cast=fs. find_all("div" , attrs={"class" :"credit_summary_item"})
        for aciklamalar in cast:
            cumle =cumle+"\n" + aciklamalar.h4.text+ " = "+ aciklamalar .a . text
    except :
        pass

    with open("filmler/" + film_adi + ".txt" ,"w" )as f:
        f.write(cumle)
