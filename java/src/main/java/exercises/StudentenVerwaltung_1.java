import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Student_1 {
    private String name;
    private double notendurchschnitt;

    public Student_1(String name, double notendurchschnitt) {
        this.name = name;
        this.notendurchschnitt = notendurchschnitt;
    }

    public String getName() {
        return name;
    }

    public double getNotendurchschnitt() {
        return notendurchschnitt;
    }
}

public class StudentenVerwaltung_1 {
    private List<Student_1> studentenListe;

    public StudentenVerwaltung_1() {
        studentenListe = new ArrayList<>();
    }

    public void addStudent(String name, double notendurchschnitt) {
        studentenListe.add(new Student_1(name, notendurchschnitt));
    }

    public boolean removeStudent(String name) {
        return studentenListe.removeIf(student -> student.getName().equals(name));
    }

    public Student_1 getBestStudent() {
        return studentenListe.stream()
                .max(Comparator.comparingDouble(Student_1::getNotendurchschnitt))
                .orElse(null);
    }

    public void printAllStudents() {
        studentenListe
                .forEach(student -> System.out.println(student.getName() + ": " + student.getNotendurchschnitt()));
    }

    public static void main(String[] args) {
        StudentenVerwaltung_1 verwaltung = new StudentenVerwaltung_1();

        // Testfälle
        verwaltung.addStudent("Max Mustermann", 2.5);
        verwaltung.addStudent("Erika Musterfrau", 1.7);
        verwaltung.addStudent("Klaus Kleber", 3.0);

        System.out.println("Alle Studenten:");
        verwaltung.printAllStudents();

        System.out.println("\nBester Student:");
        Student_1 besterStudent = verwaltung.getBestStudent();
        if (besterStudent != null) {
            System.out.println("Bester Student: " + besterStudent.getName() + " mit einem Durchschnitt von "
                    + besterStudent.getNotendurchschnitt());
        }

        System.out.println("\nEntferne Student 'Klaus Kleber':");
        boolean entfernt = verwaltung.removeStudent("Klaus Kleber");
        System.out.println("Erfolgreich entfernt: " + entfernt);

        System.out.println("\nAlle Studenten nach Entfernung:");
        verwaltung.printAllStudents();
    }
}
