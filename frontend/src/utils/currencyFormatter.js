export function toCurrency(value) {
    if (!value) return '';
    return `R$ ${Number(value).toFixed(2)}`
}