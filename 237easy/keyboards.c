#include <stdio.h>
#include <string.h>

#define MAX_STR_LEN 45

struct keyboard
{
    char keys[MAX_STR_LEN];
    int num_keys;
    char best_match[MAX_STR_LEN];
    int best_match_set;
    int longest_match;
};

int main(int argc, char* argv[])
{
    FILE* input = fopen(argv[1], "r");
    
    // load keyboards into an array
    int num_keyboards;
    fscanf(input, "%d\n", &num_keyboards);
    struct keyboard keyboards[num_keyboards];
    for (int i = 0; i < num_keyboards; i++)
    {
        fgets(keyboards[i].keys, MAX_STR_LEN, input);
        keyboards[i].num_keys = strlen(keyboards[i].keys) - 1;
        keyboards[i].longest_match = 0;
        keyboards[i].best_match_set = 0;
    }
    fclose(input);

    // scan dictionary
    FILE* word_list = fopen("/usr/share/dict/words", "r");
    char word[MAX_STR_LEN];
    while (fgets(word, MAX_STR_LEN, word_list))
    {
        // check each keyboard to see if it can type the current word
        for (int i = 0; i < num_keyboards; i++)
        {            
            int can_type = 1;
            int word_length = strlen(word) - 1;
            for (int j = 0; j < word_length; j++)
            {               
                char* s = strchr(keyboards[i].keys, word[j]);
                if (s == NULL) can_type = 0;
            }
            if (can_type)
            {
                // if word is longer than our longest match so far,
                // make it the new best match
                if (word_length > keyboards[i].longest_match)
                {
                    strcpy(keyboards[i].best_match, word);
                    keyboards[i].longest_match = word_length;
                }
                // if word is equal in length to longest match so far,
                // append it to the best match
                else if (word_length == keyboards[i].longest_match)
                {
                    keyboards[i].best_match[strlen(keyboards[i].best_match) - 1] = ',';
                    strcat(keyboards[i].best_match, " ");                    
                    strcat(keyboards[i].best_match, word);                    
                }
            }
        }
    }
    fclose(word_list);
    
    // print out the results for each keyboard
    for (int i = 0; i < num_keyboards; i++)
    {
        keyboards[i].keys[strlen(keyboards[i].keys) - 1] = '\0';
        printf("%s: %s", keyboards[i].keys, keyboards[i].best_match);
    }

    return 0;
}