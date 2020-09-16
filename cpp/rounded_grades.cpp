/*
https://www.hackerrank.com/challenges/grading/problem
HackerLand University has the following grading policy:
Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:
If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
*/

/*

I like this one, because I was able to do it without six(?) different if-else statements.
I'm a big fan of mod.

*/

vector<int> gradingStudents(vector<int> grades) {
    vector<int> ret(grades.size());
    int mod;
    for (int i; i < grades.size(); i++) {
        if (grades[i] < 38) {
            ret[i] = grades[i];
            continue;
        }
        mod = grades[i] % 5;
        if (mod > 2) {
            ret[i] = grades[i]+(5-mod);
        } else {
            ret[i] = grades[i];
        }
    }
    return ret;
}