/* 

Problem from LeetCode - https://leetcode.com/problems/word-search/description/

Another - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

@author - Brendon Murthum
@version - January 2018

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. The same 
letter cell may not be used more than once.

TODO - 
1. Run analysis of runtime of "lettersAvailable" on 3x3 and large.
2. Setup test cases.
3. Clean up code whitespace and format to GVSU Style-Guide.
4. Run it on LeetCode.

Example:

  Given a board symbolically represented as the following...
 
  board = [['A','B','C','E'],
           ['S','F','C','S'],
           ['A','D','E','E']]
        
  word = "ABCCED", returns TRUE.
  word = "SEE", returns TRUE.
  word = "ABCB", returns FALSE.

My Performance Test Cases:

  Case 1: 3 x 3 board. Showing simple functionality.
  
    board = [['A','B','C'],
             ['D','E','F'],
             ['G','H','I']]
    word = "ABC", returns TRUE.
    word = "EHI", returns TRUE.
    word = "AEI", returns FALSE. No diagonals.
    word = "ABD", returns FALSE. "B" and "D" not connected.
    word = "ABA", returns FALSE. No repeated characters.
    word = "ZAB", returns FALSE. No "Z" in the board.
    word = "GHH", returns FALSE. No second "H" in the board.

  Case 2: 7 x 7 board. Showing complex solutions, edge cases.

  Case 3: 20 x 20 board. Showing variety of speeds to solution.

  Case 4: 30 x 30 board. Showing variety of speeds to solution.

  Case 5: 5 x 20 board. Showing odd-shaped boards.

*/

#include <string>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

/* This class is in format of LeetCode's assigned problem. */
class Solution {
public:
    /** Searches for a word within a matrix of letters. */
    bool exist(vector<vector<char> > &board, string &word) {
        
        /* First letter of the given word. */
        char firstLetter = word[0];
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();
        
        /** 
         Board of booleans for searching. Everything is initially false, then
         upon entering a position, it is marked true, so to not revisit.
        */
        vector<vector<bool> > boolBoard(boardRows, vector<bool>(boardColumns)); 
        for (int i=0; i < boardRows; i++) {
            for (int j=0; j < boardColumns; j++) {
                boolBoard[i][j] = false;
            }
        }
        
        // Debugging
        cout << "First Letter: " << firstLetter << "\n";
        
        /** 
         Iterate through the board for first-letters, to initiate a recursive
         search that will look for the entire word as a snake. 
        */
        for (int i = 0; i < boardRows; i++) {
            for (int j = 0; j < boardColumns; j++) {
                /* On finding a firstletter, initiate the search. */
                if (board[i][j] == firstLetter) {
                    /* Remove the first letter from the possible for search. */
                    boolBoard[i][j] = true;
                    if (recursiveSearch(board,boolBoard,word.substr(1),i,j)) {
                        return true;
                    }
                    /* Add that first letter back for next search. */
                    boolBoard[i][j] = false;
                }
            }
        }
        return false;
        
    }
    
    bool recursiveSearch( vector<vector<char> > &board, 
                          vector<vector<bool> > previouslySearched, 
                          string smallerWord, 
                          int currentRow, 
                          int currentColumn) {
        
        cout << "  Recursive Search... \n";
        
        cout << "    smallerWord: " << smallerWord << "\n";
        cout << "    currentRow: " << currentRow << "\n";
        cout << "    currentColumn: " << currentColumn << "\n";
        
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();
        
        /* Coordinates of the potential positions to search next. */
        int upRow = currentRow - 1;
        int upCol = currentColumn;
        int downRow = currentRow + 1;
        int downCol = currentColumn;
        int rightRow = currentRow;
        int rightCol = currentColumn + 1;
        int leftRow = currentRow;
        int leftCol = currentColumn - 1;;
        
        /* Initiate new recursive searches */
        
        /* Check the upper box from current position. */
        if (upRow >= 0 
                  && previouslySearched[upRow][upCol] == false 
                  && board[upRow][upCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                previouslySearched[currentRow][currentColumn] = true;
                cout << "    searching UP... \n";
                if (recursiveSearch(board, previouslySearched, smallerWord.substr(1), upRow, upCol)) {
                    return true;
                }
            }
        }
        /* Check the below box. */
        if (downRow < boardRows
            && previouslySearched[downRow][downCol] == false 
            && board[downRow][downCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                cout << "    searching DOWN... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, smallerWord.substr(1), downRow, downCol)) {
                    return true;
                }
            }
        }
        /* Check the right box. */
        if (rightCol < boardColumns
            && previouslySearched[rightRow][rightCol] == false 
            && board[rightRow][rightCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                cout << "    searching RIGHT... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, smallerWord.substr(1), rightRow, rightCol)) {
                    return true;
                }
            }
        }
        /* Check the left box. */
        if (leftCol >= 0
            && previouslySearched[leftRow][leftCol] == false 
            && board[leftRow][leftCol] == smallerWord[0]) {
            /* Found the last letter! */
            if (smallerWord.size() == 1) {
                return true;
            } 
            else {
                cout << "    searching RIGHT... \n";
                previouslySearched[currentRow][currentColumn] = true;
                if (recursiveSearch(board, previouslySearched, smallerWord.substr(1), leftRow, leftCol)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    /** Sees if the letters in the "word" match a count in the board. */
    bool lettersAvailable(vector<vector<char> >& board, string &word) {
    
        /* This code limits CPU processes in the cases of invalid searches. */
        
        /** Number of columns in board. */
        int boardRows = board.size();
        /** Number of rows in board. */
        int boardColumns = board[0].size();
        /** The length of the given word. */
        int wordLength = word.size();
        /** Each letter of the word, in a char array. */
        char wordLetters[wordLength + 1];
        /** Each letter position has a boolean. */
        bool boolLetters[wordLength + 1];
        
        /* Initialize each of these arrays. */
        for (int i = 0; i < wordLength; i++) {
            wordLetters[i] = word[i];
            boolLetters[i] = false;
        }
        
        /* Makes sure every letter is seen at least for the amount necessary. */
        for (int i = 0; i < boardRows; i++) {
            for (int j = 0; j < boardColumns; j++) {
                for (int k = 0; k < wordLength; k++) {
                    /* If match, mark the letter as counted. */
                    if ( (board[i][j] == wordLetters[k]) 
                         && (boolLetters[k] == false) ) {
                        boolLetters[k] = true;
                        break;
                    }
                }
            }
        }
        
        /* Return false if a single letter is missing. */
        for (int i = 0; i < wordLength; i++) {
            if (boolLetters[i] == false) {
                return false;
            }
        }
        return true;
    }
};

/** Displays the board to the terminal. */
void displayBoard(vector<vector<char> > &board) {
    
    /** Number of columns in board. */
    int boardRows = board.size();
    /** Number of rows in board. */
    int boardColumns = board[0].size();
    
    /* Iterate through the two-dimensional vector. */
    cout << "\n";
    cout << " Board: \n";
    for (int i=0; i < boardRows; i++) {
        cout << " [";
        for (int j=0; j < boardColumns; j++) {
            if (j == boardColumns - 1) {
                cout << board[i][j] << "]\n";
            } else {
                cout << board[i][j] << ", ";   
            }
        }
    }
}


int main(int argc, char** argv) {

    /* Initial text given to the terminal. */
    cout << "\n" << "Initializing the board word-finder.." << "\n";
    cout << "\n";
    cout << "This program will run each test a multitude of times, each \n" <<
            "within the period of a second. This is to find the runtime \n"<<
            "in an order of milliseconds. \n";
    cout << "\n";

    /** Initialize an object for testing. This uses leetcode's format. */
    Solution solutionObject;
    /** Columns in a board. */
    int cols;
    /** Rows in a board. */
    int rows;
    /** Iterator for adding characters. */
    int x;
    /* Timer of a case-test. */
    clock_t t;
    /* Time converted to milliseconds. */
    float timeInMilliseconds;
    /* Counted iterations of the line to be tested. */
    int iterationsOfLines;
    /* Output of exist() function to display. */
    bool output;

    /** Case-1 Board Vector. */
    /*
      ['A','B','C']
      ['D','E','F']
      ['G','H','I']
    */
    cols = 3;
    rows = 3;
    vector<vector<char> > board1(rows, vector<char>(cols)); 
    char addingCharacters[10] = "ABCBEFCHI";
    x = 0;
    for (int i=0; i < rows; i++) {
        for (int j=0; j < rows; j++) {
            board1[i][j] = addingCharacters[x];
            x++;
        }
    }

    /** Case-1 Test Word A. */
    string board1_testWordA = "ABC";
    /** Case-1 Test Word B. */
    string board1_testWordB = "ABD";
    /** Case-1 Test Word C. */
    string board1_testWordC = "ABA";
    
    /* Running Case-1 */
    cout << "Showing Case #1: ";
    /* Display the board on terminal. */
    displayBoard(board1);
    cout << "\n";
    /* Display the searched-for word. */
    cout << "Given Word: \"" << board1_testWordA << "\"\n";
    cout << "Letters Available: ";
    if (solutionObject.lettersAvailable(board1, board1_testWordA))
        cout << "True!\n";
    else
        cout << "False.\n";
        
    // t = clock();
    // iterationsOfLines = 0;
    // while (clock() - t < CLOCKS_PER_SEC) {
        output = solutionObject.exist(board1, board1_testWordA);
    //    iterationsOfLines++;
    // }
    // t = clock() - t;
    // timeInMilliseconds = (float)(round((((float)1 / (float)iterationsOfLines) * 1000) * 1000)) / (float)1000;
    // cout << "Iterations: " << iterationsOfLines << "\n";
    if (output == true) {
        cout << "Result: \"" << board1_testWordA << "\" was found! \n";
    } else {
        cout << "Result: \"" << board1_testWordA << "\" was not found \n";
    }
    
    // cout << "Runtime: " << timeInMilliseconds << "ms" << "\n";
    cout << "\n";
    
    return 0;
}

