Selenium IDE, web tarayıcılarında otomatik test senaryoları oluşturmak için kullanılan bir araçtır. Bu araç, kayıt ve oynatma özelliği ile kullanıcıların etkileşimli olarak tarayıcıda gerçekleştirdikleri işlemleri kaydedip, bu işlemleri daha sonra otomatik olarak tekrar etmelerine olanak tanır. İşte Selenium IDE'de kullanılan bazı temel komutlar:

open:

Açıklama: Belirtilen URL'yi açar.
Örnek: open | https://www.example.com
click:

Açıklama: Belirtilen öğeye (buton, bağlantı, vb.) tıklar.
Örnek: click | id=loginButton
type:

Açıklama: Belirtilen alanı doldurur.
Örnek: type | id=username | kullanici_adi
select:

Açıklama: Belirtilen dropdown listesinden bir öğe seçer.
Örnek: select | id=country | Turkey
pause:

Açıklama: Belirtilen süre kadar testin durmasını sağlar (milisaniye cinsinden).
Örnek: pause | 3000 (3 saniye duraklatma)
verifyText:

Açıklama: Belirtilen öğenin metnini kontrol eder.
Örnek: verifyText | id=welcomeMessage | Welcome, User!
waitForElementPresent:

Açıklama: Belirtilen öğenin sayfada görünmesini bekler.
Örnek: waitForElementPresent | id=submitButton
store:

Açıklama: Belirtilen değeri bir değişkene atar.
Örnek: store | Example Text | myVar
echo:

Açıklama: Belirtilen metni konsola yazdırır.
Örnek: echo | This is a message
assert:

Açıklama: Belirtilen koşulu kontrol eder, eğer doğru değilse testi durdurur.
Örnek: assert | id=errorDiv | An error occurred
Bu komutlar, Selenium IDE'nin temel kullanımını kapsar. Selenium IDE'nin kayıt ve oynatma yetenekleri sayesinde, bu komutları manuel olarak yazmak zorunda kalmadan test senaryolarınızı oluşturabilirsiniz. Unutmayın ki, sayfa yapısı ve öğe tanımlayıcıları (id, class, xpath vb.) sayfanın HTML yapısına bağlı olarak değişebilir, bu nedenle kaydedilen senaryoların zamanla güncellenmesi gerekebilir.
