class Company {
    private String name;
    private ArrayList<Departament> departamentList;

    public Company(String name) {
        this name = name;
        this departamentList = new ArrayList<>();
    }

    public void addDepartament(Departament) {
        for(Departament : departament){
            this.departamentList.add(departament);
        }
    }
    public void deleteDepartament(Departament) {
        this.departamentList.remove(departament);
    }
    public void printInfo() {
        System.out.printf("Компания \"%s\"\n\nОтделы компании:\n", this name);
        for (Departament : this.departamentList) {
            System.out.printf("- %s\n", departament.getName());
        }
    }
}
class Departament {
    private String name;
    private ArrayList<Employee> employeesList;

    public Departament(String name) {
        this name = name;
        this employeesList = new ArrayList<>();
    }

    public void addEmployees(Employee) {
        for(Employee : Employees){
            this.employeesList.add(Employee);
        }
    }
    public void deleteDepartament(Employee) {
        this.employeesList.remove(Employee);
    }
    public void printInfo() {
        System.out.printf("\n%s.\nВ отделе сотрудников: %d, Общая ЗП: %d\nСписок сотрудников отдела:\n", this name, this.employeesList.size(), this.getTotalSalary());
        for (Employee : this.employeesList) {
            System.out.printf("- %s\n", employee.getName());
        }
    }
    public String getname() {
        returnt this.name;
    }
    public int getTotalSalary() {
        int totalSalary = 0;
        for (Employee : this.employeesList) {
            totalSalary += employee.getSalary();
        }
        return totalSalary;
    }
    class Employee {
        private String name;
        private int age;
        private int salary;

        public Employee (String name, int age, int salary) {
            this name = name;
            this age = age;
            this.salary = salary;
        }
        public void printInfo() {
            System.out.printf("Имя сотрудника: %s\nВозраст сотрудника: %d\nЗарплата сотрудника: %d\n", this name, this.age, this.salary);
            for (Departament : this.departamentList) {
                System.out.printf("- %s\n", departament.getName());
            }
        }
    }
}
