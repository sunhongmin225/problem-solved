/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
	let sortedArray = [];
	totalLength = nums1.length + nums2.length;
	medianIndex = Math.floor(totalLength / 2);

	while (nums1.length && nums2.length) {
		if (nums1[0] < nums2[0]) {
			sortedArray.push(nums1.shift());
		} else {
			sortedArray.push(nums2.shift());
		}
	}
	let resultArray = [...sortedArray, ...nums1, ...nums2];

	if (totalLength % 2 === 1) {
		return resultArray[medianIndex]
	} else {
		return (resultArray[medianIndex] + resultArray[medianIndex - 1]) / 2
	}
};