import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Student {
    String name;
    double notendurchschnitt;

    public Student(String name, double notendurchschnitt) {
        this.name = name;
        this.notendurchschnitt = notendurchschnitt;
    }
}

public class StudentenVerwaltung {
    private List<Student> studentenListe;

    public StudentenVerwaltung() {
        studentenListe = new ArrayList<>();
    }

    public void addStudent(String name, double notendurchschnitt) {
        studentenListe.add(new Student(name, notendurchschnitt));
    }

    public boolean removeStudent(String name) {
        return studentenListe.removeIf(student -> student.name.equals(name));
    }

    public Student getBestStudent() {
        return studentenListe.stream()
                .max(Comparator.comparingDouble(student -> student.notendurchschnitt))
                .orElse(null);
    }

    public void printAllStudents() {
        studentenListe.forEach(student -> System.out
                .println("Name: " + student.name + ", Notendurchschnitt: " + student.notendurchschnitt));
    }

    public static void main(String[] args) {
        StudentenVerwaltung verwaltung = new StudentenVerwaltung();

        // Testfälle
        verwaltung.addStudent("Max Mustermann", 1.5);
        verwaltung.addStudent("Erika Musterfrau", 1.3);
        verwaltung.addStudent("Hans Müller", 2.0);

        System.out.println("Alle Studenten:");
        verwaltung.printAllStudents();

        System.out.println("\nBester Student:");
        Student besterStudent = verwaltung.getBestStudent();
        if (besterStudent != null) {
            System.out
                    .println("Name: " + besterStudent.name + ", Notendurchschnitt: " + besterStudent.notendurchschnitt);
        }

        System.out.println("\nEntferne Student 'Hans Müller':");
        boolean entfernt = verwaltung.removeStudent("Hans Müller");
        System.out.println("Erfolgreich entfernt: " + entfernt);

        System.out.println("\nAlle Studenten nach Entfernung:");
        verwaltung.printAllStudents();
    }
}
