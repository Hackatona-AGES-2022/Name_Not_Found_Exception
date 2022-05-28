<template>
  <v-container class="px-8 mt-4">
    <v-row>
      <span class="view__title">Promoções Ativas</span>
    </v-row>
    <v-row class="mt-6">
      <Input
        label="Pesquisar promoções..."
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
      />
    </v-row>
    <v-row class="justify-space-between mt-8">
      <v-col cols="6" v-for="sale in sales" :key="sale.id">
        <SaleCard :sale="sale" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Input from "../components/Input.vue";
import { getStoreSales } from "../service/SalesService";
import SaleCard from "../components/SaleCard.vue";

export default {
  name: "Home",
  components: { Input, SaleCard },
  data: () => ({
    sales: [{}],
  }),
  async mounted() {
    this.sales = await getStoreSales("9696969696");
  },
};
</script>
