#include <stdio.h>
#include <conio.h>
#define N 9
#define UNASSIGNED 0

int is_exist_row(int grid[N][N], int row, int num){
    int col;
	for (col = 0; col < 9; col++) {
		if (grid[row][col] == num) {
			return 1;
		}
	}
	return 0;
}

int is_exist_col(int grid[N][N], int col, int num) {
	int row;
    for (row = 0; row < 9; row++) {
		if (grid[row][col] == num) {
			return 1;
		}
	}
	return 0;
}

int is_exist_box(int grid[N][N], int startRow, int startCol, int num) {
	int row,col;
    for (row = 0; row < 3; row++) {
		for (col = 0; col < 3; col++) {
			if (grid[row + startRow][col + startCol] == num) {
				return 1;
			} 
		}
	}
	return 0;
}

int is_safe_num(int grid[N][N], int row, int col, int num) {
	return !is_exist_row(grid, row, num) 
			&& !is_exist_col(grid, col, num) 
			&& !is_exist_box(grid, row - (row % 3), col - (col %3), num);
}

int find_unassigned(int grid[N][N], int *row, int *col) {
	for (*row = 0; *row < N; (*row)++) {
		for (*col = 0; *col < N; (*col)++) {
			if (grid[*row][*col] == 0) {
				return 1;
			}
		}
	}
	return 0;
}

int solve(int grid[N][N]) {
	
	int row = 0;
	int col = 0;
	
	if (!find_unassigned(grid, &row, &col)){
		return 1;
	}
	int num;
	for (num = 1; num <= N; num++ ) {
		
		if (is_safe_num(grid, row, col, num)) {
			grid[row][col] = num;
			
			if (solve(grid)) {
				return 1;
			}
			
			grid[row][col] = UNASSIGNED;
		}
	}
	
	return 0;
}

void print_grid(int grid[N][N]) {
    int row,col;
	for (row = 0; row < N; row++) {
		for (col = 0; col < N; col++) {
			printf("%2d", grid[row][col]);
		}
		printf("\n");
	}
}

int main() {
	
	printf("MARK BLANK BOXES AS '0' (ZERO)\n");
	int grid[N][N] = {};
	int i,j;
	printf("ENTER GRID VALUES\n");
	for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            printf("ENTER VALUE AT [%d][%d]: ",i,j);
            scanf("%d",&grid[i][j]);
        }
    }
    printf("\n***QUESTION***\n");
    print_grid(grid);
	
	if (solve(grid)) {
		printf("\n***SOLUTION***\n");
        print_grid(grid);
	} 
    else {
		printf("No Solution");
	}
	getch();
	return 0;
}
