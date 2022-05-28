import { HTTP } from "../api/HTTP"

async function getStoreSales(cnpj) {
    return HTTP.get(`store_sales/${cnpj}`)
        .then(res => {
            debugger;
        })
}

export {
    getStoreSales
}