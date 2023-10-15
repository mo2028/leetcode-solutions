class Solution {
    int n;// rows
    int m; // column
    public int numIslands(char[][] grid) {
        

        int numIslands = 0;
        n = grid.length;
        m = grid[0].length;

        for( int i = 0; i <n; i++){
            for(int j =0; j<m; j++){
                // if not visited and is a land
                if(grid[i][j] == '1'){
                    // pass the grid, position(i,j), and the visited 2d array
                    dfs(grid, i, j);
                    numIslands++;
                }

            }
        }

        return numIslands;

    }

    // implement dfs

    private void dfs(char grid[][], int i, int j){
        if(i<0 || j < 0 || i >= n || j >= m || grid[i][j] != '1'){
            return;
        }
        grid[i][j] = '0';
        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);


    }



}