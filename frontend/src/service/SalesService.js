import { HTTP } from "../api/HTTP"

async function getStoreSales(cnpj) {
    return HTTP.post('store_sales', { cnpj })
}

export {
    getStoreSales
}