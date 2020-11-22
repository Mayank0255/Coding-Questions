function modifyArray(nums) {
    return nums.map(i => (i & 1) ? i * 3 : i * 2);
}
