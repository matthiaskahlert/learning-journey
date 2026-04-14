# Du bist ein Softwareentwickler in einer Firma, die sich auf die Entwicklung von Web-Anwendungen spezialisiert hat. Dein aktuelles Projekt ist die Entwicklung einer Anwendung für ein Fitnessstudio. Die Anwendung soll verschiedene Arten von Mitgliedern (Standard, Premium, VIP) und die verschiedenen Dienstleistungen, die sie nutzen können, verwalten. 

# a) Erstelle eine Klasse Mitglied mit den Instanzvariablen name, mitgliedschafts_typ und genutzte_dienstleistungen. 

# b) Implementiere eine Methode dienstleistung_hinzufügen, die eine Dienstleistung zur Liste der genutzten Dienstleistungen hinzufügt.

# c) Erstelle drei Unterklassen StandardMitglied, PremiumMitglied und VIPMitglied, die von der Klasse Mitglied erben. Jede dieser Klassen sollte eine Methode preis_berechnen haben, die den Preis basierend auf den genutzten Dienstleistungen und dem Mitgliedschaftstyp berechnet. 

# d) Implementiere eine Methode rechnung_erstellen, die eine Rechnung für das Mitglied erstellt, indem sie die Methode preis_berechnen aufruft und den berechneten Preis zusammen mit dem Namen des Mitglieds und dem Mitgliedschaftstyp ausgibt.

# a) Basisklasse Mitglied
class Mitglied
  attr_reader :name, :mitgliedschafts_typ, :genutzte_dienstleistungen

  def initialize(name)
    @name = name
    @genutzte_dienstleistungen = []
    @mitgliedschafts_typ = self.class.to_s
  end

  # b) Dienstleistung hinzufügen
  def dienstleistung_hinzufuegen(dienst)
    @genutzte_dienstleistungen << dienst
  end

  # d) Rechnung erstellen
  def rechnung_erstellen
    preis = preis_berechnen
    puts "Rechnung für #{@name} (#{@mitgliedschafts_typ}): #{preis} €"
  end
end

# c) Unterklassen mit spezifischer Preisberechnung
class StandardMitglied < Mitglied
  def preis_berechnen
    # Standard: 10 € Grundgebühr + 5 € pro Dienstleistung
    10 + 5 * @genutzte_dienstleistungen.size
  end
end

class PremiumMitglied < Mitglied
  def preis_berechnen
    # Premium: 20 € Grundgebühr + 2 € pro Dienstleistung
    20 + 2 * @genutzte_dienstleistungen.size
  end
end

class VIPMitglied < Mitglied
  def preis_berechnen
    # VIP: 50 € Grundgebühr, alle Dienstleistungen inklusive
    50
  end
end

# Beispielnutzung
mitglied1 = StandardMitglied.new('Anna')
mitglied1.dienstleistung_hinzufuegen('Sauna')
mitglied1.dienstleistung_hinzufuegen('Kurs')
mitglied1.rechnung_erstellen

mitglied2 = PremiumMitglied.new('Ben')
mitglied2.dienstleistung_hinzufuegen('Sauna')
mitglied2.rechnung_erstellen

mitglied3 = VIPMitglied.new('Clara')
mitglied3.dienstleistung_hinzufuegen('Personal Training')
mitglied3.dienstleistung_hinzufuegen('Massage')
mitglied3.rechnung_erstellen
