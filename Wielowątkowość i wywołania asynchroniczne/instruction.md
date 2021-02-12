#Program 1 – pierwszy wątek
Napisać program wyświetlający „Hello World!!” w oddzielnym wątku (CreateThread). Przed
zakończeniem głównej procedury programu należy zaczekać na zakończenie wątku
(WaitForSingleObject lub Join).  

#Program 2 – ręczne wznawianie wątków  
Napisać program, który utworzy 10 wątków. Każdy z wątków z częstotliwością raz
na sekundę ma wyświetlać napisy od ‘Ax’ do ‘Zx’, gdzie x jest numerem wątku (dla wątku
numer 10 wstawić 0). Wątki należy utworzyć z jako SUSPENDED.
Użytkownikowi należy udostępnić możliwość sterowania działaniem programu. W zależności
od zastosowanego GUI mogą to być kontrolki graficzne np. pole edycyjne do ustawiania
numeru wątku i przyciski zatrzymaj i wznów lub też w przypadku aplikacji konsolowej mogą
to być komendy np. start 1 lub stop 1-3.
#Program 3 – wykorzystanie synchronizacji
Zadanie identyczne do Programu 2, jednak kod wyświetlający napisy od ‘Ax’ do ‘Zx’ ma być
wykonywany tylko przez jeden wątek w danej chwili (sekcja krytyczna). W tym celu należy
zmienić działanie program. Zaraz po jego uruchomieniu wszystkie wątki mają być jako
RESUMED. Nie potrzebne będzie też sterowanie wątkami przez użytkownika.
#Program 4 – asynchroniczność
Zaimplementuj program z zadania nr 2 z wykorzystaniem wywołań asynchronicznych.
Użytkownikowi należy dać tylko możliwość kasowania dowolnych zadań.