const toBase58Num = n => {
    let r = "", a = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
    do { r = a[n % 58] + r; n = Math.floor(n / 58); } while (n > 0);
    return r;
};