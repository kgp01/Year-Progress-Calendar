/* Year Progress calculator */


// Change the year
// Generate output
// Copy and use it as input for python file
// Resolve date time issue in python file before importing
// Viola, enjoy life. 

#include <bits/stdc++.h>
using namespace std;


int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string month_name[12] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
string month_number[12] = {"01", "02", "03", "04", "05", "06", "07", "08", "09", "10" , "11", "12"}; 
int start_percent = 0;
int end_percent = 101;
int current_year = 2025;


vector<string> date_list;
vector<string> time_list;
vector<string> progress_list;


void progress_calc(int progress){
    double total_days = 0;
    for(int i = 0; i < 12; i++){
        total_days = total_days + months[i];
    }
    double value = total_days*progress/100;
    printf("value %f\n", value);
    int days = floor(value);
    int month_counter = 0;
    double exact_time = value - days;
    int hours = floor(exact_time*24);
    double mins = (exact_time*24 - hours)*60;
    cout << value << " " << days << " " << exact_time << " " << hours << " " << mins << endl;
    for(int i = 0; i < 12; i++){
        if(days > months[i]){
            days = days - months[i];
            month_counter++;
        }
        else{
            if(hours > 12){
                
                cout << hours - 12 << " pm " << mins << " mins " << days + 1  << " " << month_name[i] << endl;
                date_list.push_back('"' + to_string(days+1) + "-" +  month_number[i] + '-' + to_string(current_year) + '"');
                int int_mins = static_cast<int> (mins);
                
                time_list.push_back('"' + to_string(hours) + ":" + to_string(int_mins) + '"');
                progress_list.push_back('"' + to_string(progress) + "% year gone" + '"');
                
            }

            else if(hours == 12){
                cout << hours << " pm " << mins << " mins " << days + 1  << " " << month_name[i] << endl;
                date_list.push_back('"' + to_string(days+1) + "-" +  month_number[i] + '-' + to_string(current_year) + '"');
                int int_mins = static_cast<int> (mins);
                
                time_list.push_back('"' + to_string(hours) + ":" + to_string(int_mins) + '"');
                progress_list.push_back('"' + to_string(progress) + "% year gone" + '"');
            }


            else{
                cout << hours << " am " << mins << " mins " << days + 1  << " " << month_name[i] << endl;
                date_list.push_back('"' + to_string(days+1) + "-" +  month_number[i] + '-' + to_string(current_year) + '"');
                int int_mins = static_cast<int> (mins);
                
                time_list.push_back('"' + to_string(hours) + ":" + to_string(int_mins) + '"');
                progress_list.push_back('"' + to_string(progress) + "% year gone" + '"');
                
            }
            cout << endl;
            break;
        }
    }
}


int main(){
    int progress;

    for(int i = start_percent; i < end_percent; i++){
        cout << "Percentage " << i << endl;
        progress_calc(i);
    }

    for(int i = 0; i < end_percent - start_percent; i++){
        cout << date_list[i] << ",";
    }
    cout << endl; 

    for(int i = 0; i < end_percent - start_percent; i++){
        cout << time_list[i] << ",";
    }
    cout << endl;

    for(int i = 0; i < end_percent - start_percent; i++){
        cout << progress_list[i] << ",";
    }
    cout << endl;
    return 0; 
}

// g++ -o year_progress year_progress.cpp 
// year_progress