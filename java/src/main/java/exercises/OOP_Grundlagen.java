public class OOP_Grundlagen {
    // static bedeutet: jedes objekt hat die gleiche klasse, es gibt nur eine klasse, die von allen objekten geteilt wird
	static class Flasche {
		int inhalt;
		int maxInhalt;
		boolean geoeffnet;

		Flasche(int maxInhalt) {
			this.inhalt = 0;
			this.maxInhalt = maxInhalt;
			this.geoeffnet = false;
		}

		void oeffnen() {
			geoeffnet = true;
			System.out.println("Flasche geöffnet");
		}

		void schliessen() {
			geoeffnet = false;
			System.out.println("Flasche geschlossen");
		}

		void fuellen(int menge) {
			if (!geoeffnet) {
				System.out.println("Fehler: Flasche ist geschlossen!");
				return;
			}

			if (inhalt + menge > maxInhalt) {
				System.out.println("Fehler: Zu viel! Maximal " + maxInhalt + "ml möglich.");
			} else {
				inhalt += menge;
				System.out.println("Gefüllt: " + menge + "ml. Aktueller Inhalt: " + inhalt + "ml");
			}
		}

		void leeren() {
			if (!geoeffnet) {
				System.out.println("Fehler: Flasche ist geschlossen!");
				return;
			}

			inhalt = 0;
			System.out.println("Flasche geleert");
		}
	}

    // main ist static, da es zu programmstart noch kein objekt gibt, 
    // es ist die erste funktion, die aufgerufen wird, um das programm zu starten
    public static void main(String[] args) {
		System.out.println("=== Objektorientierte Programmierung Demo ===\n");

		Flasche meineFlasche = new Flasche(500);
		System.out.println("Flasche erstellt: max. " + meineFlasche.maxInhalt + "ml\n");

		meineFlasche.oeffnen();
		meineFlasche.fuellen(200);
		meineFlasche.fuellen(150);
		meineFlasche.fuellen(200);
		meineFlasche.schliessen();
		meineFlasche.leeren();

		System.out.println("\n=== Zweites Objekt ===\n");

		Flasche andereFlasche = new Flasche(1000);
		andereFlasche.oeffnen();
		andereFlasche.fuellen(750);

		System.out.println("\nMeine Flasche: " + meineFlasche.inhalt + "ml");
		System.out.println("Andere Flasche: " + andereFlasche.inhalt + "ml");
	}
}
