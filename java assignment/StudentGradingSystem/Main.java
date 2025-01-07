package StudentGradingSystem;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) {

        int numberOfStudent = Integer.parseInt(System.console().readLine("enter number of Students in your class>>>> "));        
        int numberOfSubject = Integer.parseInt(System.console().readLine("enter number of Subjects>>>> "));

        GradingSystem_ system = new GradingSystem_(numberOfStudent, numberOfSubject);
        // System.out.println(Arrays.toString(system.student));
        // System.out.println(Arrays.toString(system.subjects));

        double[][] scores = system.collectSores();
        System.out.println(Arrays.deepToString(scores));

        double[] studentAverages = system.getStudentAverages(scores);
        System.out.println(Arrays.toString(studentAverages));

        int[] studentPositions = system.getStudentPositions(studentAverages);
        System.out.println(Arrays.toString(studentPositions));

        system.subjectSummary(scores);
        double[] totalScore = system.getStudentTotalScore(scores);

        system.sampleOutput(studentPositions, totalScore, studentAverages, scores);




    }

}
