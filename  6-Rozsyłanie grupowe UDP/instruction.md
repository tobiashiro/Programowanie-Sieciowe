#Cel ćwiczenia:
W trakcie ćwiczenia studenci wykonają dwa rodzaje aplikacji sieciowych do wysyłania i odbierania komunikatów
tekstowych wykorzystując do transmisji danych protokół UDP (obie aplikacje mogą być połączone w jeden
program). 


#Polecenie ćwiczeniowe:
Pierwszym zadaniem jest rozsyłanie grupowe – multicast, a drugim broadcast. W każdym przypadku należy
utworzyć dwa moduły klienta i serwera, jak to można zaobserwować w przykładzie udostępnionym na stronie
przedmiotu na platformie WIKAMP w sekcji „Techniki rozgłaszania UDP”.
Do zaliczenia ćwiczenia wymagane jest napisanie programu wysyłającego dowolne komunikaty (np. wpisywany
przez użytkownika) w trybach multicast i broadcast w sieci LAN oraz modułu odbierającego te sygnały.
Należy użytkownikowi dać możliwość dowolnego definiowania adresu IP grup multicast’owej oraz numeru
portu.
Program powinien mieć możliwość jego wielokrotnego uruchamiania na tej samej maszynie (wielokrotne
bindowanie gniazda).
Program musi być odporny na niewłaściwe dane wpisane przez użytkownika.