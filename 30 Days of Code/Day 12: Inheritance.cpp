#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
using namespace std;


class Person{
    protected:
        string firstName;
        string lastName;
        int id;
    public:
        Person(string firstName, string lastName, int identification){
            this->firstName = firstName;
            this->lastName = lastName;
            this->id = identification;
        }
        void printPerson(){
            cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n"; 
        }
    
};

class Student :  public Person{
    private:
        vector<int> testScores;  
    public:
        /*    
        *   Class Constructor
        *   
        *   Parameters:
        *   firstName - A string denoting the Person's first name.
        *   lastName - A string denoting the Person's last name.
        *   id - An integer denoting the Person's ID number.
        *   scores - An array of integers denoting the Person's test scores.
        */
        // Write your constructor here
        Student(string firstName, string lastName, int identification, vector<int> scores): Person(firstName, lastName, identification) {
            this->testScores = scores;
        }
        /*    
        *   Function Name: calculate
        *   Return: A character denoting the grade.
        */
        // Write your function here
        char calculate() {
            int sum = std::accumulate(testScores.begin(), testScores.end(), 0);
            double a = (double)sum / testScores.size();

            char grade = 'T';

            if (a <= 100 && a >= 90)
                grade = 'O';
            else if (a < 90 && a >= 80)
                grade = 'E';
            else if (a < 80 && a >= 70)
                grade = 'A';
            else if (a < 70 && a >= 55)
                grade = 'P';
            else if (a < 55 && a >= 40)
                grade = 'D';

            return grade;
        }
};

int main() {
    string firstName;
      string lastName;
    int id;
      int numScores;
    cin >> firstName >> lastName >> id >> numScores;
      vector<int> scores;
      for(int i = 0; i < numScores; i++){
          int tmpScore;
          cin >> tmpScore;
        scores.push_back(tmpScore);
    }
    Student* s = new Student(firstName, lastName, id, scores);
    s->printPerson();
    cout << "Grade: " << s->calculate() << "\n";
    return 0;
}