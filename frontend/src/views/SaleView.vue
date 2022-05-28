<template>
  <v-container>
    <div class="view__title mt-12">{{ sale.title }}</div>

    <v-row class="amount justify-center mt-6">
      <div class="amount__current">{{ sale.current_amount }}</div>
      <div class="amount__target">{{ targetAmount }}</div>
    </v-row>

    <v-row class="mx-4 mt-12 justify-center">
      <div style="font-weight: bold; font-size: 22px; color: #515151">
        A oferta termina em
      </div>
      <div style="font-size: 20px">{{ expirationDate }}</div>
    </v-row>

    <v-row class="justify-center mt-12">
      <Button title="Reservar Compra" extended rounded />
    </v-row>
  </v-container>
</template>

<script>
import { getSale } from "../service/SalesService";
import { loadUser } from "../service/UserService";
import Button from "../components/Button.vue";
import { HTTP } from "../api/HTTP";

export default {
  data: () => ({
    sale: {},
  }),
  components: { Button },
  async mounted() {
    this.$root.showToolbar(loadUser().name);
    const id = this.$route.params.id;
    this.sale = await getSale(id);
  },
  computed: {
    targetAmount() {
      return `/${this.sale.target_amount} unidades`;
    },
    expirationDate() {
      return new Date(this.sale.expiration_date).toLocaleString();
    },
  },
  methods: {
    onButtonClick() {
      HTTP.post(`/user_sale`, {});
    },
  },
};
</script>

<style lang="scss">
.view__title {
  font-size: 1.9rem;
  text-align: center;
}

.amount {
  font-size: 24px;
  color: #515151;

  &__current {
    font-weight: bold;
  }
}
</style>
