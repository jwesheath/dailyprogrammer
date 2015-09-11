public class ca {
    public static void main(String[] args) {
        
        int[] currentState = {0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,
                       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,0,0,0, 0};
        
        int steps = Integer.parseInt(args[0]);

        for (int step = 0; step < steps; step++) {
            printArray(currentState);
            currentState = getNextState(currentState);
        }
    }

    public static void printArray(int[] array) {
        for (int i = 1; i < array.length - 1; i++) {
            if (array[i] == 1) {
                System.out.print("X");
            } else {
                System.out.print(" ");
            }
        }
        System.out.print("\n");
    }

    public static int[] getNextState(int[] currentState) {
        int[] nextState = new int[currentState.length];
        for (int i = 1; i < currentState.length - 1; i++) {
            if (currentState[i + 1] == currentState[i - 1]) {
                nextState[i] = 0;
            } else {
                nextState[i] = 1;
            }
        }
        return nextState;      
    }
}
