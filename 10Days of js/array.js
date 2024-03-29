function getSecondLargest(nums) {
    // Complete the function
     const sorted_array          = nums.sort((a,b) => a - b );
    const unique_sorted_array   = [...new Set(sorted_array)];
    return unique_sorted_array[unique_sorted_array.length - 2];
}