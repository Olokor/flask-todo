package StudentGradingSystem;

import java.util.ArrayList;
import java.util.Scanner;

public class GradingSystem {
    private Scanner scanner = new Scanner(System.in);
    private ArrayList<String> students;
    private ArrayList<String> subjects;
    public int numberOfSubjects;

    public GradingSystem(int numberOfStudents) {
        this.students = generateStudentIds(numberOfStudents);
        this.subjects = getSubjects(); // Initialize subjects in constructor
        this.numberOfSubjects = this.subjects.size();
    }

    public ArrayList<String> getStudents() {
        return this.students;
    }

    private ArrayList<String> getSubjects() {
        ArrayList<String> listOfSubjects = new ArrayList<>();
        
        System.out.print("Enter subject(s) separated with comma>>> ");
        String line = scanner.nextLine();
        String[] values = line.split(",");
        for (String subject : values) {
            listOfSubjects.add(subject.trim()); // Add trim() to handle spaces
        }
        
        return listOfSubjects;
    }

    private ArrayList<String> generateStudentIds(int numberOfStudents) {
        ArrayList<String> students = new ArrayList<>();
        for (int i = 1; i <= numberOfStudents; i++) {
            students.add(String.format("Student_%d", i));
        }
        return students;
    }

    private double[] checkScores(String[] values) {
        double[] doubleScores = new double[this.numberOfSubjects];
        try {
            for (int i = 0; i < values.length; i++) { // Changed <= to 
                double score = Double.parseDouble(values[i].trim());
                doubleScores[i] = Math.min(score, 100.0); // Simplified score capping
            }
        } catch (NumberFormatException e) {
            System.out.println("Error: Please enter valid numbers");
        }
        return doubleScores;
    }

    public ArrayList<ArrayList<Double>> gradeStudents() {
        ArrayList<ArrayList<Double>> allGrades = new ArrayList<>();
        
        System.out.println("Available subjects: " + subjects);
        
        for (String student : this.students) {
            System.out.println(String.format("\nEnter grades for %s", student));
            System.out.print("Enter grades separated with comma>>> ");
            
            String line = scanner.nextLine();
            String[] values = line.split(",");
            
            if (values.length != numberOfSubjects) {
                System.out.println("Error: Number of grades must match number of subjects");
                continue;
            }
            
            double[] scores = checkScores(values);
            ArrayList<Double> studentGrades = new ArrayList<>();
            for (double score : scores) {
                studentGrades.add(score);
            }
            allGrades.add(studentGrades);
        }
        
        return allGrades;
    }

    public void displayGrades() {
        ArrayList<ArrayList<Double>> grades = gradeStudents();
        
        // Print header with subjects
        System.out.println("\nGrade Report:");
        System.out.print("Student ID\t");
        for (String subject : subjects) {
            System.out.print(subject + "\t");
        }
        System.out.println();

        // Print grades for each student
        for (int i = 0; i < students.size(); i++) {
            System.out.print(students.get(i) + "\t");
            for (Double grade : grades.get(i)) {
                System.out.print(grade + "\t");
            }
            System.out.println();
        }
        
        scanner.close(); // Close scanner after all input is done
    }
}