#Cel ćwiczenia: 

W trakcie ćwiczenia studenci wykonają program iteracyjnego serwera usługi ECHO na bazie protokołu TCP.
Usługa Echo: serwer czeka na połączenie klienta. Po zaakceptowaniu połączenia oczekuje na wiadomość.
Każdą odebraną od klienta wiadomość natychmiast odsyła do klienta bez zmian.
Zaimplementowany program serwera można testować napisaną na poprzednich zajęciach własną aplikacją
klienta TCP_Client.jar bądź aplikacją dostępną w folderze PROGRAMY.
Polecenie ćwiczeniowe:  

Do zaliczenia ćwiczenia wymagane jest napisanie programu udostępniającego usługę ECHO. Do realizacji
ćwiczenia można zastosować dowolną preferowaną platformę programistyczną.
Zadaniem programu jest:  

- nasłuchiwanie usługi dla wybranych interfejsów sieciowych
(domyślnie dla wszystkich, a nie localhost!),
- udostępnienie usługi ECHO dla protokołu TCP/IP na podanym porcie (wartość domyślna 7 ).
- udostępnienie możliwości wprowadzenia innego portu komunikacji,
- rejestrowanie wszystkich połączeń i wyświetlanie dostępnych informacji o podłączonym komputerze
odległym wraz z numerem portu tej komunikacji,
- odporność na niewłaściwe dane wpisane przez użytkownika, niewłaściwe zamknięcie gniazda
po stronie klienta i zwalnianie zasobów w chwili zamykania programu,
- odsyłanie wiernej kopii otrzymanej wiadomości (tzn. funkcja wysyłająca wysyła TYLKO tyle danych, ile
serwer otrzymał od klienta),
- informowanie użytkownika o każdej otrzymanej wiadomości z zaznaczeniem IP i numeru portu
nadawcy oraz treści i rozmiaru.