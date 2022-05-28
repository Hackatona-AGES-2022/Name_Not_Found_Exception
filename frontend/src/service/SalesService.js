import { HTTP } from "../api/HTTP"

async function getStoreSales(cnpj) {
    return HTTP.get(`store_sales/${cnpj}`)
        .then(res => {
            const sales = res.data.map(item => ({
                currentAmount: item.Sale.current_amount,
                targetAmount: item.Sale.target_amount,
                defaultPrice: item.Sale.default_price,
                targetPrice: item.Sale.target_price,
                title: item.Sale.title
            }))
            return sales;
        })
}

export {
    getStoreSales
}