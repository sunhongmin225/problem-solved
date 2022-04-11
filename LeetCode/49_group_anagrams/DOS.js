function groupAnagrams(strs) {
    const countMap = {};
    strs.forEach(str => {
        const countStr = JSON.stringify(countChar(str));
        countMap[countStr] ? countMap[countStr].push(str) : countMap[countStr] = [str];
        }
    );
    return Object.values(countMap);
}

function countChar(str) {
    const tot = {};
    str.split("").forEach(c => { tot[c] ? tot[c]++ : tot[c] = 1; });
    return sortObj(tot);
}

function sortObj(obj) {
    const newObj = {};
    Object.keys(obj).sort().forEach(key => newObj[key] = obj[key])
    return newObj;
}
