import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.LinkedList;
import java.util.function.Function;
import java.util.stream.Collectors;

class Opstrings1 {
    
    public static String rot(String strng) {
        List<String> list = Arrays.asList(strng.split("\n"));
        Collections.reverse(list);
        return list.stream().map(s -> new StringBuilder(s).reverse().toString()).collect(Collectors.joining("\n"));
    }
    public static String selfieAndRot(String strng) {
        List<String> list = Arrays.asList(strng.split("\n"));
        Collections.reverse(list);
        String rot = "...." + list.stream().map(s -> new StringBuilder(s).reverse().toString()).collect(Collectors.joining("\n...."));
        String selfie = strng.replaceAll("\n", "....\n") + "....\n";
        return selfie + rot;
    }
    
    public static String oper(Function<String, String> operator, String s) {
        return operator.apply(s);
    }
}