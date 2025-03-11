package models;

public class Student extends User {
    private String studentClass;
    private int age;
    public Student(int id, Student userClass, String firstName, String lastName, String email, String student_class, int age, String password) {
        super(id, userClass.getClass(), firstName, lastName, email, password);
        this.studentClass = student_class;
        this.age = age;
    }



}
