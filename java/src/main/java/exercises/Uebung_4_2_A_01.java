/* Entwickle ein Java-Programm, das einen einfachen Text-Adventure-Spielablauf simuliert. 
Das Spiel soll verschiedene Räume haben, die durch Zahlen repräsentiert werden. 
Der Spieler startet im Raum 0 und das Ziel ist es, Raum 5 zu erreichen. 
In jedem Raum muss der Spieler eine Entscheidung treffen, um in den nächsten Raum zu gelangen. 
Die Entscheidungen sollen mit einer switch-case-Verzweigung implementiert werden, bei der der Spieler die Möglichkeit hat, 
eine Zahl zwischen 1 und 3 einzugeben, die jeweils für eine unterschiedliche Aktion steht. 
Zusätzlich soll das Spiel eine while-Schleife enthalten, die sicherstellt, 
dass der Spieler so lange im aktuellen Raum bleibt, bis die richtige Aktion gewählt wurde, um weiterzukommen. 
Nutze eine for-Schleife, um eine Nachricht am Anfang jedes neuen Raumes anzuzeigen, die den Fortschritt des Spielers (Raumnummer) 
und eine kurze Beschreibung des Raumes enthält. Implementiere auch eine do-while-Schleife, 
die am Ende des Spiels fragt, ob der Spieler das Spiel wiederholen möchte. 
Die Eingabe des Spielers soll über die Konsole erfolgen und die Ausgabe soll entsprechende Hinweise und Erfolgsmeldungen enthalten.

a) Implementiere die switch-case-Verzweigung für die Entscheidungen des Spielers in jedem Raum.

b) Verwende eine while-Schleife, um den Spieler im Raum zu halten, bis die richtige Entscheidung getroffen wurde.

c) Nutze eine for-Schleife, um zu Beginn jedes Raumes eine Nachricht mit der Raumnummer und einer Beschreibung anzuzeigen.

d) Implementiere eine do-while-Schleife am Ende des Spiels, um den Spieler zu fragen, ob er das Spiel wiederholen möchte.  */

import java.util.Scanner;

public class Uebung_4_2_A_01 {

    // Hilfsfunktion für kurze Pause zwischen Raumwechseln
    public static void warteKurz() {
        try {
            System.out.println(". . . ");
            Thread.sleep(1200); // 1,2 Sekunden Pause
        } catch (InterruptedException e) {
            // Thread wurde unterbrochen, ignorieren wir hier bewusst
            Thread.currentThread().interrupt();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int entscheidung;
        char spielNochmal;

        do {
            int raum = 0;

            System.out.println("\n" + "=".repeat(60));
            System.out.println("    WILLKOMMEN ZUM EPISCHEN TEXT-ADVENTURE!");
            System.out.println("    Dein Ziel: Erreiche Raum 5 und entkomme mit dem Schatz!");
            System.out.println("=".repeat(60) + "\n");

            while (raum != 5) {
                // Nachricht zu Beginn des Raumes
                for (int i = 0; i < 3; i++) {

                    if (i == 0) {
                        System.out.println("\n" + "-".repeat(60));
                        System.out.println(">>> RAUM " + (raum + 1));
                        System.out.println("-".repeat(60));
                    }

                    if (i == 1) {
                        switch (raum) {
                            case 0:
                                System.out.println("DAS ALTE TOR");
                                break;
                            case 1:
                                System.out.println("DER DUNKLE KORRIDOR");
                                break;
                            case 2:
                                System.out.println("DER SCHATZ");
                                break;
                            case 3:
                                System.out.println("DER FLUSS");
                                break;
                            case 4:
                                System.out.println("DER DRACHE");
                                break;
                        }
                        System.out.println("-".repeat(60));
                    }

                    if (i == 2) {
                        switch (raum) {
                            case 0:
                                System.out.println(
                                        "Abenteuerlustig näherst Du Dich dem alten Gemäuer. Gerüchten zufolge sind hier schon viele Schatzsucher verschwunden.");
                                warteKurz();
                                System.out.println(
                                        "Kurz zögerst du, doch deine Neugierde siegt. Du öffnest das knarrende Tor und trittst ein.");
                                warteKurz();
                                System.out.println(
                                        "Du gehst durch das alte Tor und gelangst in eine Halle. Überall hängen Spinnweben und es riecht muffig. Es ist dunkel, aber du kannst gerade noch die Umrisse von Türen erkennen.");
                                warteKurz();
                                System.out.println("Als Du hindurchschreitest, siehst Du drei Türen vor dir.");
                                break;
                            case 1:
                                System.out.println("Ein dunkler Korridor, es riecht nach Abenteuer.");
                                System.out.println("Plötzlich entdeckst Du eine Weggabelung mit drei Gängen vor dir:");
                                System.out.println("Gehst du links (1), rechts (2) oder geradeaus (3)?");
                                break;
                            case 2:
                                System.out.println(
                                        "Du siehst eine kleine Schatztruhe und einen ledernen kleinen Beutel vor Dir. \nDie Truhe ist geöffnet und einige Münzen liegen auf dem Boden. \nDer Schatz auf dem Boden glitzert.");
                                break;
                            case 3:
                                System.out.println("Ein Fluss blockiert deinen Weg.");
                                System.out.println("Du musst eine Brücke finden.");
                                break;
                            case 4:
                                System.out.println("Ein Drache liegt schlafend vor dir. Vorsicht!");
                                break;
                        }
                    }
                }
                System.out.println("-".repeat(60));

                // Entscheidungen des Spielers
                boolean raumVerlassen = false;
                while (!raumVerlassen) {
                    // Optionen für den aktuellen Raum anzeigen (in der Schleife, damit sie immer
                    // sichtbar sind)
                    System.out.println("\nDeine Möglichkeiten:");
                    switch (raum) {
                        case 0:
                            System.out.println("  [1] Linke Tür nehmen");
                            System.out.println("  [2] Geradeaus gehen");
                            System.out.println("  [3] Rechte Tür nehmen");
                            break;
                        case 1:
                            System.out.println("  [1] Links abbiegen");
                            System.out.println("  [2] Geradeaus weitergehen");
                            System.out.println("  [3] Rechts abbiegen");
                            break;
                        case 2:
                            System.out.println("  [1] Truhe durchsuchen");
                            System.out.println("  [2] Beutel aufhebenn");
                            System.out.println("  [3] Raum durchsuchen");
                            break;
                        case 3:
                            System.out.println("  [1] Durch den Fluss schwimmen");
                            System.out.println("  [2] Am Ufer entlang flussaufwärts suchen");
                            System.out.println("  [3] Weiter flussabwärts gehen");
                            break;
                        case 4:
                            System.out.println("  [1] Renn schnell an Ihm vorbei!");
                            System.out.println("  [2] Leise am Drachen vorbeischleichen");
                            System.out.println("  [3] Den Drachen aufwecken");
                            break;
                    }

                    System.out.println("\n[?] Triff eine Entscheidung (1, 2 oder 3):");
                    entscheidung = scanner.nextInt();

                    switch (raum) {
                        // Türen
                        case 0:
                            switch (entscheidung) {
                                case 1:
                                    System.out.println(
                                            "[✓] Du gehst links, die linke Tür knarrt laut, aber öffnet sich dann doch. \nMit Spannung trittst Du hindurch.");
                                    raum = 1;
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                case 2:
                                    System.out.println("[✗] Die mittlere Tür ist verschlossen. Versuch es woanders.");
                                    break;
                                case 3:
                                    System.out.println(
                                            "[✗] Der Türgriff der rechten Tür bricht ab und sieht nicht so aus, als wenn Du ihn \nreparieren könntest. Versuch es bei einer anderen Tür.");
                                    break;
                                default:
                                    System.out.println("[!] Ungültige Eingabe. Wähle 1, 2 oder 3.");
                            }
                            break;

                        case 1:
                            // Gänge
                            switch (entscheidung) {
                                case 1:
                                    System.out.println(
                                            "[✓] Du gehst links, der Gang weitet sich und du kannst passieren.");
                                    raum = 2;
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                case 2:
                                    System.out.println(
                                            "[✗] Du gehst geradeaus und erreichst eine Sackgasse, da der Gang vor dir eingestürzt ist.");
                                    break;
                                case 3:
                                    System.out.println(
                                            "[✗] Du gehst rechts und erreichst einen Abgrund den du nicht passieren kannst. Du musst umdrehen.");
                                    break;
                                default:
                                    System.out.println("[!] Ungültige Eingabe. Wähle 1, 2 oder 3.");
                            }
                            break;

                        case 2:
                            // Schatz
                            switch (entscheidung) {
                                case 1:
                                    System.out
                                            .println(
                                                    "[✓] Du gehst vorsichtig zum Schatz und füllst Deine Taschen mit allem Gold, das hineinpasst. \n Dabei entdeckst Du eine Falle auf einer Trittplatte und kannst sie entschhärfen.  \nDu findest den Ausgang von Raum 3.");
                                    raum = 3;
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                case 2:
                                    System.out.println("[✗] Du ignorierst den Schatz und gehst weiter.");
                                    System.out.println("    Plötzlich stürzt die Decke ein und du bist gefangen!");
                                    warteKurz();
                                    System.out.println("\n" + "*".repeat(60));
                                    System.out.println("    GAME OVER - Du bist verhungert!");
                                    System.out.println("*".repeat(60));
                                    warteKurz();
                                    raum = 0; // Reset auf Start
                                    raumVerlassen = true;
                                    break;
                                case 3:
                                    System.out.println(
                                            "[✗] Falsche Wahl. Als Du den Raum durchsuchen willst, zwingt Dich ein unheimliches grünes Leuchten abzubrechen.");
                                    System.out.println(
                                            "     Es muss sich um einen Abwehrzauber handeln.Du hast zu viel Angst. Der Schatz bleibt unberührt.");
                                    break;
                                default:
                                    System.out.println("[!] Ungültige Eingabe. Wähle 1, 2 oder 3.");
                            }
                            break;
                        case 3:
                            // Fluss
                            switch (entscheidung) {
                                case 1:
                                    System.out.println(
                                            "[✗] Du versuchst, durch den Fluss zu schwimmen, aber die Strömung ist so stark und zieht sich zurück.");
                                    System.out.println(
                                            "    Du kannst gerade noch so eine Wurzel greifen die herausragt und dich an Land retten.");
                                    break;
                                case 2:
                                    System.out.println(
                                            "[✗] Es ist so glitschig hier! Du fällst ins Wasser. \nDu versuchst noch herauszuklettern, aber rutschst ab. Der Schatz in Deinen Taschen ist so schwer und zieht dich nach unten.");
                                    warteKurz();
                                    System.out.println("\n" + "*".repeat(60));
                                    System.out.println("    GAME OVER - Du bist ertrunken!");
                                    System.out.println("*".repeat(60));
                                    warteKurz();
                                    raum = 0; // Reset auf Start
                                    raumVerlassen = true;
                                    break;
                                case 3:
                                    System.out.println("[✓] Du gehst vorsichtig eine Weile in diese Richtung.");
                                    System.out.println(
                                            "    Hinter einer Biegung entdeckst du einen umgestürzten Pfeiler,");
                                    warteKurz();
                                    System.out.println("    der Dich sicher ans andere Ufer bringt.");
                                    raum = 4;
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                default:
                                    System.out.println("[!] Ungültige Eingabe. Wähle 1, 2 oder 3.");
                            }
                            break;

                        case 4:
                            // Drache
                            switch (entscheidung) {
                                case 1:
                                    System.out
                                            .println(
                                                    "[✗] Du versuchst, schnell am Drachen vorbeizurennen um den Drachen zu umgehen, aber er wacht auf!");
                                    warteKurz();
                                    System.out.println(
                                            " Seine augen fangen an zu glühen und er öffnet sein Maul und verschlingt Dich und den Schatz mit einem Bissen!");
                                    warteKurz();
                                    System.out.println("\n" + "*".repeat(60));
                                    System.out.println("    GAME OVER - Du wurdest verschlungen!");
                                    System.out.println("*".repeat(60));
                                    warteKurz();
                                    raum = 0; // Reset auf Start
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                case 2:
                                    System.out.println(
                                            "[✓] Leise schleichst du am Drachen vorbei und erreichst den Ausgang!");
                                    System.out.println("    Schnell machst Du dich mit Deiner Beute aus dem Staub");
                                    System.out.println("    in Richtung der nächsten Taverne!");
                                    raum = 5;
                                    raumVerlassen = true;
                                    warteKurz();
                                    break;
                                case 3:
                                    System.out.println("[✗] Ohje - Der Drache wacht auf! Schnell zurückziehen!");
                                    break;
                                default:
                                    System.out.println("[!] Ungültige Eingabe. Wähle 1, 2 oder 3.");
                            }
                            break;
                    }
                }
            }
            System.out.println("\n" + "=".repeat(60));
            System.out.println("    🎉 HERZLICHEN GLÜCKWUNSCH! 🎉");
            System.out
                    .println("    Du hast Raum 5 erreicht und den Drachen überlebt! Du hast das Abenteuer gemeistert!");
            System.out.println("=".repeat(60));
            System.out.println("\nWillst du das Abenteuer nochmal spielen? (j/n)");
            spielNochmal = scanner.next().toLowerCase().charAt(0);
        } while (spielNochmal == 'j');

        scanner.close();
        System.out.println("\nDanke fürs Spielen! Bis zum nächsten Abenteuer!");
        System.out.println("\n" + "=".repeat(60));
    }
}