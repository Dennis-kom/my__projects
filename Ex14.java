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
     * Remarks: any changes in the matrix are prohibited
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
    private static boolean isInBound(boolean[][]mat,int x, int y){
        return (x < mat.length && x>=0 && y < mat.length && y >= 0);
    }

    /**
     * QUESTION 2
     * Signature:
     *
     * **/
    public static boolean isPermutation(int [] a, int [] b){
        if(a==null || b==null || a.length !=b.length) return false;
        return isPermutation(a,b,0,0,a);


    }
    /**
     *
     *
     * **/
    public static boolean isPermutation(int [] a, int [] b,int i,int j,int[]res){

        // stop term 1
        if(!(inBound(a,i) && inBound(a,j)) && !allCellsZero(res,0)) return false;

        // seeking index got the bound of the array
        if(j>=a.length) return isPermutation(a,b,i+1,0,res);

        // stop term 2
        if(i>=a.length && allCellsZero(res,0)) return true;

        // similar value caught
        if (inBound(a,i) && inBound(a,j) && a[i] == b[j]) {
            res[i]=res[i]-b[j];
            return isPermutation(a,b,i,j+1,res);
        }

        // different values
        return isPermutation(a,b,i,j+1,res);
    }

    private static boolean allCellsZero (int[]a,int i){
        if(i>=a.length) return true;
        if(a[i]!=0) return false;
        return allCellsZero(a,i+1);

    }
    private static boolean inBound(int[]a,int i){
        return (i>=0 && i<a.length);
    }

}
