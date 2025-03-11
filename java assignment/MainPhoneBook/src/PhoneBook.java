
import java.util.ArrayList;

public class PhoneBook{

    ArrayList<Contact> contacts = new ArrayList<>();

    private void  addContact(){
        String firstName = System.console().readLine("Enter first name: ");
        String lastName = System.console().readLine("Enter last name: ");

        String phoneNumber = System.console().readLine("enter phone number");
        while (checkPhoneNumber(phoneNumber)){
            phoneNumber = System.console().readLine("enter phone number");
        }
        Contact newContact = new Contact(firstName, lastName, phoneNumber);
        contacts.add(newContact);
    }

    private Contact getAllContact(){
        for(Contact contact: contacts){
            return contact;
        }
        return null;
    }

    private Contact getContactByFirstNAme(String firstName){
        for(Contact contact:contacts){
            if(contact.getfirstName().equals(firstName)){
                return contact;
            }
        }
        return null;
    }

    private Contact getContactByPhoneNumber(String phoneNUmber){
        for(Contact contact:contacts){
            if(contact.getPhoneNumber().equals(phoneNUmber)){
                return contact;
            }
        }
        return null;
    }

    private Contact getContactByLastName(String lastName){
        for(Contact contact:contacts){
            if(contact.getLastName().equals(lastName)){
                return contact;
            }
        }
        return null;
    }

    private Contact searchContact(String input){
        for (Contact contact: contacts){
            if(input.equalsIgnoreCase(contact.getfirstName()) || input.equalsIgnoreCase(contact.getLastName()) || input.equals(contact.getPhoneNumber())){
                return contact;
            }
        }
        return null;
    }

    private void editContact(String input){
        for (Contact contact: contacts){
            if(input.equalsIgnoreCase(contact.getfirstName()) || input.equalsIgnoreCase(contact.getLastName()) || input.equals(contact.getPhoneNumber())){
                System.out.println("Edit contact");
                System.out.println(contact);
                System.out.print("""
                press 1. to edit first name
                press 2. to edit last name
                press 3. to edit phone number
                >>>>>>> """);
                String entry = System.console().readLine();
                switch(entry){
                    case "1" -> { 
                        String firstName = System.console().readLine("enter new first name>>> ");
                        contact.setFirstName(firstName);
                    }

                    case "2" -> {
                        String lastName = System.console().readLine("enter new last name>>> ");
                        contact.setLastName(lastName);
                    }

                    case "3" ->{
                        String phoneNumber= System.console().readLine("enter new phone number>>> ");
                        if (checkPhoneNumber(phoneNumber));
                            contact.setFirstName(phoneNumber);
                    }
                    default -> {
                        System.out.println("nothing to do");
                    }
                }

            }
        }

    }

    public void phoneBookInterface(){
        while(true){
        System.out.println("""
            1. create contact
            2. edit contact
            3. search contact(dynamic search)
            >>>>>""");

            String input = System.console().readLine();

            switch(input){
                case "1" -> {
                    String response;
                    do { 
                        addContact();
                        response = System.console().readLine("do you want to add more contacts y/n? : ");
                    } while (response.equalsIgnoreCase("y") || response.equalsIgnoreCase("yes"));
                }

                case "2" -> {
                    String entry = System.console().readLine("enter the contact you want to edit");
                    editContact(entry);
                }

                case "3" -> {
                    String entry = System.console().readLine("enter the contact detail");
                    System.out.println(searchContact(entry));
                }

                default ->{
                    System.out.println(getAllContact());
                }

            }
        }
    }

    private boolean checkPhoneNumber(String phoneNumber){
        int intPhoneNumber;
        try {
            if (phoneNumber.contains("+234")){
                intPhoneNumber = Integer.parseInt(phoneNumber.substring(3));
                return true;
            }
            intPhoneNumber = Integer.parseInt(phoneNumber);
            return true;
            
        } catch (NumberFormatException e) {
            return false;
        }
    }
}