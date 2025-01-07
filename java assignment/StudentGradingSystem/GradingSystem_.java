package StudentGradingSystem;

import java.util.Arrays;
import java.util.Scanner;

public class GradingSystem_ {

    private int numberOfStudent;
    private int numberOfSubject;
    public  String[] student = new String[numberOfStudent];
    public  String[] subjects = new String[numberOfSubject];


    Scanner input = new Scanner(System.in);

    public GradingSystem_(int numberOfStudent, int numberOfSubject){
        this.numberOfStudent = numberOfStudent;
        this.numberOfSubject = numberOfSubject;
        this.student = generateStudentIds(numberOfStudent);
        this.subjects = generateSubject(numberOfSubject);
        
    }

    private String[] generateStudentIds(int numberOfStudents) {
        String[] students = new String[numberOfStudents];
        for (int i = 0; i < numberOfStudents; i++) {
            // students.add(String.format("Student_%d", i));
            students[i] = String.format("Student_%d", i+1);
        }
        return students;
    }

    private String[] generateSubject(int numberOfSubject){
        String[] subjects = new String[numberOfSubject];
        for (int i = 0; i < numberOfSubject; i++) {
            // students.add(String.format("Student_%d", i));
            subjects[i] = String.format("Sub_%d", i+1);
        }
        return subjects;
    }

    private Boolean checkGrade(String[] grades){
        try {
            for(int i=0; i<grades.length; i++){
                if(Double.parseDouble(grades[i]) > 100 ||  Double.parseDouble(grades[i]) < 0){
                return true;
            } 
        }
        }catch (NumberFormatException e) {
            return true;
        }
        return false;
    }

    private static void successMsg(){
        System.out.println(">".repeat(35) +"\n Saved Successfully.....");
    }

    public double[][] collectSores(){
        double[][] scores = new double[this.numberOfStudent][this.numberOfSubject];
        for(int i=0; i<this.numberOfStudent; i++){
            System.out.println(String.format("\nEnter grades for %s for the following subjects %s", student[i], Arrays.toString(this.subjects) ));
            System.out.print("Enter grades separated with comma>>> ");

            String[] grades;
            while (true) { 
                grades = input.nextLine().split(",");
                if (checkGrade(grades)){
                    System.out.println("please enter correct grade (0-100)");
                }
                else{
                    break;
                }
            }
            for (int j=0; j<grades.length; j++){
                scores[i][j] = Double.parseDouble(grades[j]);
                
            } 
            successMsg(); 
            
        }
        return  scores;
    }


    public double[] getStudentAverages(double[][] scores){
        double[] average = new double[this.numberOfStudent];
        double sum = 0;
        for(int i=0; i<scores.length; i++){
            for (double j:scores[i]){
                sum +=j;
            }
            average[i] = (sum/this.numberOfSubject);
            sum = 0;
        }
        return average;

        
    }

    public double[] getStudentTotalScore(double[][] scores){
        double[] studentTotalScores = new double[this.numberOfStudent];
        double sum = 0;
        for(int i=0; i<scores.length; i++){
            for (double j:scores[i]){
                sum +=j;
            }
            studentTotalScores[i] = sum;
            sum = 0;
        }
        return studentTotalScores;
    }

    public int[] getStudentPositions(double[] studentAverages){
        int[] studentPositions = new int[this.numberOfStudent];
        for(int i=0; i<this.numberOfStudent; i++){
            int position = 1;

            for(int j=0; j<this.numberOfStudent; j++){
                if (studentAverages[j] > studentAverages[i]){
                    position++;
                }
            }
                
            studentPositions[i] = position;

        }
        return studentPositions;
    }


    public void subjectSummary(double[][] scores){
        double highestScore = 0;
        double lowesScore = 100;
        double numberOfPasses = 0;
        double numberOffailures = 0;
        String highestStudent = "";
        String lowesStudent = "";
        double totalScore = 0; 
        double averageScore = 0;
        int j=0;

        for (double[] score:scores){
            for(int i=0; i<score.length; i++){
                if (score[i] > highestScore){
                    highestScore = score[i];
                    highestStudent = this.student[i];
                    if(highestScore < 39){
                        numberOffailures++;
                    }else{
                        numberOfPasses++;
                    }
                }
                if(score[i] < lowesScore) {
                    lowesScore = score[i];
                    lowesStudent = this.student[i];
                    if(lowesScore < 39){
                        numberOffailures++;
                    }else{
                        numberOfPasses++;
                    }                
                }
                totalScore += score[i];
            }
            if(j < this.numberOfSubject){
                System.out.println("for "+this.subjects[j]);
            }
            
        
            averageScore = totalScore/this.numberOfSubject;
            System.out.printf("""
                    %s
                    Highest scoring student is: %s scoring %f 
                    %s 
                    lowest scoring student is: %s scoring %f
                    %s 
                    Total score is: %f
                    Average score is: %f
                    Number of passes: %d
                    number of failures: %d
                """, "=".repeat(25), highestStudent, highestScore, "=".repeat(25), 
                lowesStudent, lowesScore, "=".repeat(25), totalScore, 
                averageScore, (int)numberOfPasses/this.numberOfStudent, (int)numberOffailures/this.numberOfSubject);
                j++;
                totalScore = 0;


        }


    
    }

    public void sampleOutput(int[] position, double[] totalScore, double[]averageScore, double[][] scores){
        System.out.print("=".repeat(70) +"\nstudent\t");

        for(String subject:this.subjects){
            System.out.print(String.format("\t %s ", subject));
        }
        System.out.print("\t     TOT      AVG      POS  \n");
        System.out.println("=".repeat(70));

        for(int i=0; i<scores.length; i++){
            System.out.print(this.student[i]+"\t");
            for(int j=0; j<this.subjects.length; j++){
                System.out.print(String.format("%.2f    ", scores[i][j]));
            }
            System.out.print(String.format("%.2f    %.2f      %d   \n", totalScore[i], averageScore[i], position[i]));

        }
        System.out.println("=".repeat(70)+ "\n");
        System.out.println("=".repeat(70));

    }

}