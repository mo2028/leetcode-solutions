class Solution {
    private int rows;
    private int cols;
    private int maxArea = 0; // Use the class field for maxArea

    public int maxAreaOfIsland(int[][] grid) {
        rows = grid.length;
        cols = grid[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, dfs(grid, i, j)); // Use maxArea directly
                }
            }
        }

        return maxArea;
    }

    public int dfs(int grid[][], int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] != 1) {
            return 0;
        }

        grid[row][col] = 0;

        int area = 1; // Initialize area to 1
        area += dfs(grid, row - 1, col);
        area += dfs(grid, row + 1, col);
        area += dfs(grid, row, col - 1);
        area += dfs(grid, row, col + 1);

        return area;
    }
}
