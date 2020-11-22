function getMaxLessThanK(n, k) {
    let max = 0;

    for (let i = 1; i < n; i++) {

        for (let j = i + 1; j <= n; j++) {

            let bitwiseAnd = i & j;

            if (bitwiseAnd < k && max < bitwiseAnd) {
                max = bitwiseAnd;
            }
        }
    }

    return max;
}
