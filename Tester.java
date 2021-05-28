package HW14;

public class Tester {

    public static void main(String[]args){
         boolean[][]mat1 = new boolean[5][5];
        int[]a={1,2,3,4};
        int[]b={2,1,4,3};
         for(int i=0;i<5;i++){
             for(int j=0;j<5;j++){
                 if((i==0 && (j==1 || j==4)) || (i==1 && (j==0 || j==3 || j==4)) || (i==2 && (j==2 || j==3)) || (i==3 && j==0) || (i==4 && (j==0 || j==1 || j==2))){ mat1[i][j] = true;}
                 else{mat1[i][j] = false;}
             }
         }
        System.out.println(Ex14.size(mat1,0,0));
        System.out.println(Ex14.isPermutation(a,b));



    }
}
