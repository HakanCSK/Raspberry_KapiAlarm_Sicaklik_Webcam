# Raspberry_KapiAlarm_Sicaklik_Webcam
Raspberry pi  Manyetik kamera uygulaması kurulumu ; 
1 - "rpiManyetikKamera" adlı dosya micro sd karta yazdırılır.
2 - Raspberry pi başlatılır 
user: pi
Password: raspberry
3 - wifi bağlantısı için ;
sudo nano /etc/network/interfaces    

komutuyla açılan belgeyi şu şekilde değiştireceğiz:

auto lo
iface lo inet loopbook
iface etn0 inet dhcp
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
 wpa-ssid "Ağ ismi"
 wpa-psk "şifresi"

bu kadar şimdi ctrl+x ve y diyip enter’a basıp komut satırına iniyoruz ve yeniden başlatıyoruz:

sudo reboot

3 - Gönderen ve alıcı maillerini değiştirmek için;
 sudo nano /home/pi/gonder.py
yukardaki komut ile gonder.py dosyasını açıyoruz
server.login(USERNAME,PASSWORD)
bu satırla gonderen mail adresini ve şifresini giriyoruz.
(örn= server.login("coskunhakan95@gmail.com","*********")  )

sendMail( ["AlıcıMailAdresi"],

bu satırdada alıcı epostayı yazıyoruz, kaydetmek için ctrl+x kullanıp gelen uyarılara evet diyoruz.

4 - Oda numarası ayarlamak;
sudo nano /home/pi/ayar.py
komutla açtığımız belgede kapi="1" satırını değiştirerek konumunuza isim verebilirsiniz.




