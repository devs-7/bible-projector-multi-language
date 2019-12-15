package helper;

import java.text.Normalizer;

public class StringHelper {
    public static String normalizar(String str) {
        return Normalizer.normalize(str, Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
    }
}
