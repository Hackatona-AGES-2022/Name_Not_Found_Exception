<template>
  <div class="px-8 mt-4" fill-height>
    <v-row class="small mt-4">
      <span class="view__title">{{ pageTitle }}</span>
    </v-row>

    <v-row class="small mt-6">
      <Input
        label="Pesquisar promoções..."
        prepend-inner-icon="mdi-magnify"
        variant="round"
        elevation="3"
      />
    </v-row>

    <v-row class="justify-space-between mt-12">
      <v-col class="small" cols="6" v-for="sale in sales" :key="sale.id">
        <SaleCard :sale="sale" @click="onSaleClick(sale)" />
      </v-col>
    </v-row>

    <div class="bottom d-flex justify-center">
      <Button
        v-if="isStore"
        @click="$router.push('/store/sales/create/')"
        title="Cadastrar Promoção"
        extended
        rounded
        class="create-button"
      />
    </div>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
import { getStoreSales, getAllSales } from "../service/SalesService";
import SaleCard from "../components/SaleCard.vue";
import Button from "../components/Button.vue";
import { getUserType, loadUser } from "../service/UserService";
import UserType from "../service/UserType";

export default {
  name: "Home",
  components: { Input, SaleCard, Button },
  data: () => ({
    sales: [],
  }),
  async mounted() {
    const user = loadUser();
    this.$root.showToolbar(user.name);
    this.sales = await this.getList();
    console.log(this.sales);
  },
  methods: {
    async getList() {
      if (this.isStore) {
        const cnpj = loadUser().cnpj;
        return getStoreSales(cnpj);
      }
      return getAllSales();
    },
    onSaleClick(sale) {
      const userType = getUserType();
      this.$router.push(`/${userType}/sales/${sale.id}`);
    },
  },
  computed: {
    pageTitle() {
      return this.isStore ? "Promoções Ativas" : "Promoções";
    },
    isStore() {
      const type = getUserType();
      return type === UserType.store;
    },
  },
};
</script>

<style scoped>
.create-button {
  position: fixed;
  bottom: 22px;
}
</style>
