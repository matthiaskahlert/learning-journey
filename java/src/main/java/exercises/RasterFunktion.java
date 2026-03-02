public class RasterFunktion {
    public static void koordinatenAusgeben(int n) {
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                System.out.println("(" + String.valueOf(x) + "," + String.valueOf(y) + ")");
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("Raster 1");
        koordinatenAusgeben(5);

        System.out.println("Raster 2");
        koordinatenAusgeben(10);
    }
}
