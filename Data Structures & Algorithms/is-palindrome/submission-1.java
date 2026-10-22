class Solution {
    public boolean isPalindrome(String s) {
        String clean = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");

        int start = 0; 
        int end = clean.length() - 1;
        System.out.println(clean);
        while (start < end) {
            if (clean.charAt(start++) != clean.charAt(end--)) return false;
        }

        return true;
    }
}
