#include <stdio.h>
#include <string.h>

int main()
{
    char v3;      // dl
    int i;        // [rsp+18h] [rbp-68h]
    int j;        // [rsp+18h] [rbp-68h]
    int v6;       // [rsp+1Ch] [rbp-64h]
    int v7;       // [rsp+1Ch] [rbp-64h]
    int v8;       // [rsp+20h] [rbp-60h]
    char v9[32];  // [rsp+30h] [rbp-50h] BYREF
    char v10[24]; // [rsp+50h] [rbp-30h] BYREF

    char a1[6] = "yeyy";

    v6 = 0;
    v8 = 0;
    strcpy(v10, "f~}jwe|PlQ|ilo|dD");
    // if (strlen(a2) != 17)
    //     return 0LL;

    char a2[17] = "Good_job_continue";

    for (i = 0; i < strlen(a1); ++i)
        v6 += a1[i];
    // v6 = 464

    v7 = v6 / 30;
    // v7 = 15

    while (v8 != 17)
    {
        if ((v8 & 1) != 0)
            v3 = a2[v8] - 4;
        else
            v3 = a2[v8] + 4;
        // printf("%c\n", v3);
        v9[v8] = v3;
        v9[v8++] ^= v7;
    }
    puts("Dd|oli|QlP|ewj}~f");
    puts(v9);
    printf("%s\n", a2);

    // for (j = strlen(v9) - 1; j >= 0; --j)
    // {
    //     if (v9[strlen(v9) - j - 1] != v10[j])
    // printf("%d: %c - %c\n", j, v9[strlen(v9) - j - 1], v10[j]);
    // }
    return 1LL;
}