public class Raster {
    public static void main(String[] args) {
        for (int y = 0; y < 5; y += 1) {
            for (int x = 0; x < 5; x += 1) {
                System.out.println("(" + x + "," + y + ")");
            }
        }

    }
}

/*
 * es sei ein Raster, das aus 5 x 5 Feldern besteht, also insgesamt 25
 * Feldern. Die Position eines Feldes kann durch eine x- und eine y-Koordinate
 * in der Form (x,y) beschrieben werden. Wir wollen nun ein Programm schreiben,
 * das alle möglichen Koordinaten der Reihe nach ausgibt, beginnend mit
 * (0,0), (1,0)
 * und so weiter bis
 * (4,4)
 */
