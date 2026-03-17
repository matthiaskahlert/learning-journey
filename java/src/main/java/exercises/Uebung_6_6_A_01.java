/* 
Entwickle ein Programm in Java, das eine Hierarchie von Klassen abbildet, welche die Konzepte der Vererbung und des Typecastings demonstriert. 

a) Definiere eine Basisklasse Person mit den Attributen vorname, nachname und einer Methode ganzerName(), die den vollständigen Namen der Person zurückgibt.

b) Erstelle eine abgeleitete Klasse Student, die von Person erbt und zusätzliche Attribute wie matrikelnummer und studienfach besitzt. 
Implementiere einen Konstruktor, der die Attribute initialisiert und den Konstruktor der Basisklasse aufruft. 

c) Erstelle eine weitere abgeleitete Klasse Dozent, die ebenfalls von Person erbt und zusätzliche Attribute wie fachbereich und bueroNummer enthält. 
Implementiere auch hier einen Konstruktor, der die Attribute initialisiert und den Konstruktor der Basisklasse aufruft.

d) Implementiere in beiden abgeleiteten Klassen eine Methode beschreibePerson(), 
die eine Beschreibung der Person inklusive der spezifischen Attribute für Studenten bzw. Dozenten zurückgibt.

e) Erstelle in deinem Hauptprogramm (main-Methode) Instanzen von Student und Dozent. Demonstriere das Typecasting, 
indem du eine Person-Referenz erstellst, die auf ein Student-Objekt zeigt, und rufe beschreibePerson() auf. 
Führe dann ein explizites Typecasting durch, um auf spezifische Methoden oder Attribute der Student-Klasse zuzugreifen. 
*/

public class Uebung_6_6_A_01 {
    class Person {
        String vorname;
        String nachname;

        public Person(String vorname, String nachname) {
            this.vorname = vorname;
            this.nachname = nachname;
        }

        public String ganzerName() {
            return vorname + " " + nachname;
        }
    }

    class Student extends Person {
        String matrikelnummer;
        String studienfach;

        public Student(String vorname, String nachname, String matrikelnummer, String studienfach) {
            super(vorname, nachname);
            this.matrikelnummer = matrikelnummer;
            this.studienfach = studienfach;
        }

        public String beschreibePerson() {
            return "Student: " + ganzerName() + ", Matrikelnummer: " + matrikelnummer + ", Studienfach: " + studienfach;
        }
    }

    class Dozent extends Person {
        String fachbereich;
        String bueroNummer;

        public Dozent(String vorname, String nachname, String fachbereich, String bueroNummer) {
            super(vorname, nachname);
            this.fachbereich = fachbereich;
            this.bueroNummer = bueroNummer;
        }

        public String beschreibePerson() {
            return "Dozent: " + ganzerName() + ", Fachbereich: " + fachbereich + ", Büro: " + bueroNummer;
        }
    }

    // e) Hauptprogramm
    public static void main(String[] args) {
        Uebung_6_6_A_01 uebung = new Uebung_6_6_A_01();

        Student student = uebung.new Student("Max", "Mustermann", "123456", "Informatik");
        Dozent dozent = uebung.new Dozent("Dr.", "Schmidt", "Informatik", "Büro 101");

        // Typecasting: Person-Referenz auf ein Student-Objekt
        Person person = student;
        System.out.println(person.ganzerName()); // Aufruf der Methode der Basisklasse
        System.out.println(dozent.beschreibePerson());

        // Explizites Typecasting, um auf spezifische Methoden der Student-Klasse
        // zuzugreifen
        if (person instanceof Student) {
            Student spezifischerStudent = (Student) person;
            System.out.println(spezifischerStudent.beschreibePerson());
        }
    }

}
