// Schreiben Sie eine Funktion swap , die als Parameter ein String- Array und zwei Indizes übergeben bekommt 
// und die Position der beiden Elemente an den übergebenen Stellen vertauscht.



public class swap {
    public static void swap(String[] array, int index1, int index2) {
        if (index1 >= 0 && index1 < array.length && index2 >= 0 && index2 < array.length) {
            String temp = array[index1];
            array[index1] = array[index2];
            array[index2] = temp;
        } else {
            System.out.println("Ungültige Indizes.");
        }
    }

    public static void main(String[] args) {
        String[] myArray = {"A", "B", "C", "D"};
        System.out.println("Vor dem Swap: ");
        for (String element : myArray) {
            System.out.print(element + " ");
        }
        System.out.println();

        swap(myArray, 1, 3);

        System.out.println("Nach dem Swap: ");
        for (String element : myArray) {
            System.out.print(element + " ");
        }
    }
}
