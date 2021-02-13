#Cel ćwiczenia:
W trakcie ćwiczenia studenci wykonają pierwszy prosty program sieciowy wieloużytkownikowego serwera
usługi ECHO.
Usługa Echo: serwer czeka na połączenie klienta. Po zaakceptowaniu połączenia oczekuje na wiadomość.
Zaimplementowany program serwera można testować napisaną na poprzednich zajęciach własną aplikacją
klienta bądź aplikacją dostępną w folderze PROGRAMY w sekcji „Połączenie TCP klient-serwer”.
Polecenie ćwiczeniowe:
Do zaliczenia ćwiczenia wymagane jest napisanie programu udostępniającego kilku użytkownikom
jednocześnie usługę ECHO. Możliwa dowolna platforma programistyczna.
Zadaniem programu jest: 


- udostępnianie usługi dla wybranych interfejsów sieciowych
(domyślnie dla wszystkich, a nie localhost!),
- udostępnienie usługi ECHO dla protokołu TCP/IP na podanym porcie (wartość domyślna 7 ).
- udostępnienie możliwości wprowadzenia innego portu komunikacji,
- rejestrowanie wszystkich połączeń i wyświetlanie dostępnych informacji o podłączonym komputerze
odległym wraz z numerem portu tej komunikacji,
- posiadać limit aktywnych połączeń do 3, a po jego przekroczeniu wysyłać do kolejnego nadliczbowego
klienta komunikat o zajętości serwera i rozłączać połączenie,
- odporność na niewłaściwe dane wpisane przez użytkownika, niewłaściwe zamknięcie gniazda
po stronie klienta i zwalnianie zasobów (wątków) w chwili zamykania programu,
- natychmiastowe odsyłanie wiernej kopii otrzymanej wiadomości (tzn. funkcja wysyłająca wysyła TYLKO
tyle danych, ile serwer otrzymał od klienta),
- informowanie użytkownika o każdej otrzymanej wiadomości z zaznaczeniem IP i numeru portu
nadawcy oraz treści i rozmiaru,
-informowanie użytkownika o bieżącej liczbie połączonych klientów.