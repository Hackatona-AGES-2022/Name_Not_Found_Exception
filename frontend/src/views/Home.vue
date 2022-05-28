<template>
  <div class="px-8 mt-4 view__container">
    <v-row class="small mt-4">
      <span class="view__title">Promoções Ativas</span>
    </v-row>

    <v-row class="small mt-6">
      <Input
        label="Pesquisar promoções..."
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
      />
    </v-row>

    <v-row class="justify-space-between mt-12">
      <v-col cols="6" v-for="sale in sales" :key="sale.id">
        <SaleCard :sale="sale" />
      </v-col>
    </v-row>

    <div class="bottom d-flex justify-center">
      <Button title="Cadastrar Promoção" extended rounded />
    </div>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
import { getStoreSales } from "../service/SalesService";
import SaleCard from "../components/SaleCard.vue";
import Button from "../components/Button.vue";

export default {
  name: "Home",
  components: { Input, SaleCard, Button },
  data: () => ({
    sales: [{}],
  }),
  async mounted() {
    this.$root.showToolbar("Mercado Pão de Açúcar");
    this.sales = await getStoreSales("9696969696");
  },
};
</script>

<style scoped>
.small {
  max-height: 36px;
}
</style>
