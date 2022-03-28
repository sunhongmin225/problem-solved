/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
	let result = [];
	let count = n * 2;

	const backtrack = (S="", left=0, right=0) => {
		if (S.length === count) {
			result.push(S)
			return
		}
		if (left < n) {
			S += "(";
			backtrack(S, left+1, right);
			S = S.slice(0,-1);
		}
		if (right < left) {
			S += ")";
			backtrack(S, left, right+1);
			S = S.slice(0,-1);
		}
	}
	backtrack();
	return result
};

console.log(generateParenthesis(3));
