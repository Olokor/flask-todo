package models;

public class Course {
    private int id;
    private String courseTitle;
    private String courseDescription;
    private Lecturer courseLecturer;

    public Course(String courseTitle, String courseDescription, Lecturer courseLecturer) {
        this.courseTitle = courseTitle;
        this.courseDescription = courseDescription;
        this.courseLecturer = courseLecturer;
    }
}
