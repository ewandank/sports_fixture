export const toBase58Num = (n: bigint): string => {
  // No ambigous l and I or 0 and O.
  const ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
  let r = "";
  do {
    r = ALPHABET[Number(n % 58n)] + r;
    n /= 58n;
  } while (n > 0n);

  return r;
};