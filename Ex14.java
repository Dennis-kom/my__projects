package HW14;

/**
 * Student: Dennis Komarov
 * ID: 311725154
 *
 * **/
public class Ex14 {
    /**
     *QUESTION 1:
     * Signature: public static int size
     * Parameters: boolean[][],integer,integer
     * Recursive method when given matrix and two integers represents x,y coordinates, the method checks if given x,y are part of a spot, if they ara ,the method counts the amount of sells participates in the spot
     * otherwise it returns 0
     *
     * **/
    public static int size (boolean[][] mat, int x, int y){

        // case of null or coordinates out of array bounds
        if(mat == null || !isInBound(mat,x,y)) return 0;
        return size(mat,x,y,mat);
    }

    /**
     * signature public static int size overrides -  public static int size (boolean[][] mat, int x, int y)
     * Parameters: boolean[][], integer, integer, boolean[][]
     *
     *
     * **/
    public static int size(boolean[][] mat, int x, int y, boolean[][]sign){
        // initializing temporary variable
        boolean current = false;

        // remember current sign value
        if(isInBound(mat,x,y)) current = sign[x][y];

        // stop term
        if(!isInBound(mat,x,y) || !mat[x][y] ) return 0;

        // seek all possible directions , counting current location only if it unsigned
        if(isInBound(mat,x,y) && mat[x][y])
            sign[x][y] = false;
            return ((current)?1:0) + size(mat,x+1,y,sign) +
                    size(mat,x-1,y,sign) +
                    size(mat,x,y+1,sign) +
                    size(mat,x,y-1,sign) +
                    size(mat,x+1,y+1,sign) +
                    size(mat,x-1,y-1,sign) +
                    size(mat,x+1,y-1,sign) +
                    size(mat,x-1,y+1,sign);

    }

    /**
     * Utility function that gets as parameter the matrix and two integers represents the x,y coordinates and returns if those x,y coordinates
     * either in bounds of the matrix or not
     * **/
    public static boolean isInBound(boolean[][]mat,int x, int y){
        return (x < mat.length && x>=0 && y < mat.length && y >= 0);
    }
}
