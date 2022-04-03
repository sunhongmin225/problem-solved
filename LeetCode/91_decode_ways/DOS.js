var numDecodings = function(s) {
    // cell i stores number of decodes from s[0] to s[i-1] where i >= 1
    let dp = Array(s.length+1).fill(0);
    dp[0] = 1;
    dp[1] = s[0]=="0" ? 0 : 1;
    
    for (let i=2; i<dp.length; i++) {
        if (s[i-1] != "0") { dp[i] = dp[i-1] };
        let twoDigits = Number(s.slice(i-2,i));
        if (twoDigits >= 10 && twoDigits <= 26) { dp[i] += dp[i-2] }
    }
    return dp.slice(-1)
};
