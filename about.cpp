#include <iostream>




int main(){
	std::string choose ; 	
	std::cout << "plaese select a language  : " << std::endl << "english or deutsch "  ; 
	std::getline(std::cin , choose ) ;
       	 	
       	if (choose == "english" ) {
		std::cout<<std::endl << std::endl << std::endl << "It’s a simple to-do list app designed for managing tasks, duties, and time, for those who don’t want to store their information on large company servers. It doesn’t have a graphical user interface (GUI) or any data tracking. I want to highlight that it’s a lightweight app for users who want to run everything, including YouTube or a browser, directly in their terminal. Now, they can also manage their time in the terminal without any background processes (daemons).The app's commands are simple: run or shutdown. Your wish is its command."
 << std::endl << std::endl << "in future i plan to add some feature like qoets and module for personalization . " ; 
	
	}else{
	
		std::cout<< "Es ist eine einfache To-Do-Listen-App, die dazu dient, Aufgaben, Pflichten und Zeit zu verwalten, für diejenigen, die ihre Informationen nicht auf den Servern großer Unternehmen speichern möchten. Sie hat keine grafische Benutzeroberfläche (GUI) und keine Datenverfolgung. Ich möchte hervorheben, dass es eine leichte App für Benutzer ist, die alles, einschließlich YouTube oder eines Browsers, direkt in ihrem Terminal ausführen möchten. Jetzt können sie auch ihre Zeit im Terminal verwalten, ohne Hintergrundprozesse (Daemons)."

std::cout<< "Die Befehle der App sind einfach: run oder shutdown . Dein Wunsch ist ihr Befehl."

std::cout<< " In Zukunft plane ich, Funktionen wie Zitate und Module zur Personalisierung hinzuzufügen."   }
	










return 0 ; }
