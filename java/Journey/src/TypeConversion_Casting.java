public class TypeConversion_Casting {

    public static void main(String[] args) {
        // byte b = 127;// the rage of byte is -128 to 127
        int a = 257;
        byte k = (byte) a;
        System.out.println(k);
        float f = 5.6f;
        int t = (int) f;
        System.out.println(t);

        //this is promotion
        byte x=10,y=30;
        int result=x*y;
        System.out.println(result);
    }

}
