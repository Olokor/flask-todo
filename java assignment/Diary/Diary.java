public class Diary{
    private String title;
    private String date;
    private String entry;
    private String passKey;

    public Diary(String title, String date, String entry, String passKey){
        this.title = title;
        this.date = date;
        this.entry = entry;
    }

    @Override
    public String  toString(){
        return String.format("%s %n%s %n%s", this.title, this.date, this.entry);
    }

    public String getPassKey(){
        return this.passKey;
    }

    public String getDate(){
        return this.date;
    }

    public String getTitle(){
        return this.title;
    }

    public String getEntry(){
        return this.entry;
    }

    public void setTitle(String title){
        this.title = title;
    }

    public void addEntry(String entry){
        this.entry += entry;
    }

    public void setEntry(String entry){
        this.entry = entry;
    }
    
}