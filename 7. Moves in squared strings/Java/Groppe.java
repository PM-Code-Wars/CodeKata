import java.util.function.*;
import java.util.ArrayList;

class Opstrings {
    
    public static String vertMirror (String strng) {

        // parse out the individual strings
        String lines[] = strng.split("\\n");
        
        // reverse each one
        ArrayList<String> vertLines = new ArrayList<String>();
        for (String s : lines)
        {
           vertLines.add(new StringBuilder(s).reverse().toString());
        }
        
        // put them back together
        StringBuilder builder = new StringBuilder();
        builder.append(vertLines.get(0));
        for (int i = 1; i < vertLines.size(); ++i)
        {
            builder.append("\n");
            builder.append(vertLines.get(i));
        }

        return builder.toString();
    }

    public static String horMirror (String strng) {

        // parse out the individual strings
        String lines[] = strng.split("\\n");
        
        // put them together backwards
        StringBuilder builder = new StringBuilder();
        builder.append(lines[lines.length - 1]);
        for (int i = lines.length - 2; i >= 0; --i)
        {
            builder.append("\n");
            builder.append(lines[i]);
        }

        return builder.toString();
    }
    
    public static String oper(Function<String, String> func, String s) {
        return func.apply(s);
    }
}