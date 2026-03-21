/* 
Aufgabe: OOP, Arrays, Listen

Entwickle eine Java-Klasse namens Tierheim, die eine Liste von Tieren verwaltet. Jedes Tier wird durch eine eigene Klasse Tier repräsentiert, die mindestens die Eigenschaften name (String), art (String) und alter (int) besitzt. Implementiere in der Klasse Tierheim folgende Funktionalitäten:

a) Eine Methode hinzufuegen, die ein Tier-Objekt zur Liste hinzufügt.

b) Eine Methode entfernen, die ein Tier anhand seines Namens aus der Liste entfernt. Die Methode soll true zurückgeben, wenn das Tier gefunden und entfernt wurde, ansonsten false.

c) Eine Methode alterAktualisieren, die das Alter eines Tiers anhand des Namens aktualisiert. Die Methode soll true zurückgeben, wenn das Tier gefunden und das Alter aktualisiert wurde, ansonsten false.

d) Eine Methode alleTiereAnzeigen, die alle Tiere in der Liste auf der Konsole ausgibt.

e) Eine Methode sucheNachArt, die alle Tiere einer bestimmten Art zurückgibt.

Verwende für die Liste der Tiere ein ArrayList-Objekt. Teste deine Klasse Tierheim in der main-Methode, indem du einige Tiere hinzufügst, das Alter eines Tiers aktualisierst, ein Tier entfernst und die Liste der Tiere ausgibst.
*/

import java.util.ArrayList;
import java.util.List;

class Tier {
    String name;
    String art;
    int alter;
    public Tier(String name, String art, int alter) {
        this.name = name;
        this.art = art;
        this.alter = alter;
    }
    @Override
    public String toString() {
        return name + ", " + art + ", " + alter + " Jahre alt";
    }
}
public class Tierheim {
    private List<Tier> tiere = new ArrayList<>();
    public void hinzufuegen(Tier tier) {
        tiere.add(tier);
    }
    public boolean entfernen(String name) {
        return tiere.removeIf(tier -> tier.name.equals(name));
    }
    public boolean alterAktualisieren(String name, int neuesAlter) {
        for (Tier tier : tiere) {
            if (tier.name.equals(name)) {
                tier.alter = neuesAlter;
                return true;
            }
        }
        return false;
    }
    public void alleTiereAnzeigen() {
        for (Tier tier : tiere) {
            System.out.println(tier);
        }
    }
    public List<Tier> sucheNachArt(String art) {
        List<Tier> gefundeneTiere = new ArrayList<>();
        for (Tier tier : tiere) {
            if (tier.art.equals(art)) {
                gefundeneTiere.add(tier);
            }
        }
        return gefundeneTiere;
    }
    public static void main(String[] args) {
        Tierheim tierheim = new Tierheim();
        tierheim.hinzufuegen(new Tier("Bello", "Hund", 3));
        tierheim.hinzufuegen(new Tier("Miau", "Katze", 2));
        tierheim.hinzufuegen(new Tier("Hoppel", "Kaninchen", 1));
        tierheim.alterAktualisieren("Miau", 3);
        tierheim.entfernen("Hoppel");
        tierheim.alleTiereAnzeigen();
        List<Tier> hunde = tierheim.sucheNachArt("Hund");
        System.out.println("Gefundene Hunde: " + hunde);
    }
}