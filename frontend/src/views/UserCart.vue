<template>
  <div class="px-8 mt-4" fill-height>
    <v-row class="small mt-4">
      <span class="view__title">Meu Carrinho</span>
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
        <SaleCard :sale="sale" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
import { getUserSales } from "../service/SalesService";
import SaleCard from "../components/SaleCard.vue";
import { getUserType, loadUser } from "../service/UserService";
import UserType from "../service/UserType";

export default {
  name: "Home",
  components: { Input, SaleCard },
  data: () => ({
    sales: [],
  }),
  async mounted() {
    const user = loadUser();
    this.$root.showToolbar(user.name);
    this.sales = await getUserSales();
  },
  computed: {
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
