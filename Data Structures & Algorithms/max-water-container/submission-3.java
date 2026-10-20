class Solution {
    public int maxArea(int[] heights) {

        int maxVolume = 0;

        int start = 0;
        int end = heights.length - 1;

        while(start < end) {

            int height1 = heights[start];
            int height2 = heights[end];

            int width = end - start;
            int height = height1 < height2 ? height1 : height2;

            int volume = width * height;

            if (volume > maxVolume) maxVolume = volume;

            if (heights[start] == height){
                start++;
            }else{
                end--;
            }
        }

        return maxVolume;
    }
}