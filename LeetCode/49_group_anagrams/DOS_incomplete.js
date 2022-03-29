/* brute force
1. loop through all strings
2. pop string from array and push to new array
3. for remaining elements run isAnagram()
    3-1. if isAnagram() true => pop from array and push to new array
    3-2. if isAnagram() false => continue
*/
function groupAnagrams(strs) {
    const result = new Set;
    const counts = [];
    const set = new Set();
    strs.forEach(str => {counts.push(countChar(str))})
    for (let i=0; i<counts.length; i++) {
        set.add(strs[i]);
        for (let k=i+1; k<counts.length; k++) {
            if (equalObject(counts[i], counts[k])) {
                set.add(strs[k]);
            }
        }
        result.add(set)
        set.clear();
    }
    return result
}

function equalObject(obj1, obj2) {
    if (Object.keys(obj1).length === Object.keys(obj2).length &&
        Object.keys(obj1).every(function (key) { return obj1[key] === obj2[key]; })) {
        return true;
    }
    return false;
}

function countChar(str) {
    const tot = {};
    str.split("").forEach(function (c) { return tot[c] ? tot[c]++ : tot[c] = 1; });
    return tot;
}

console.log(countChar("asdfasasasfd"));
console.log(countChar("sadfasasasfd"));
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
