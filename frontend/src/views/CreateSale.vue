<template>
  <div class="px-8 mt-4 view__container">
    <v-row class="small mt-4">
      <span class="view__title">Cadastrar Promoção</span>
    </v-row>

    <v-row>
      <Input label="Título" placeholder="Arroz 1KG" />
    </v-row>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$root.showToolbar("Mercado Pão de Açúcar");
  },
};
</script>

<style></style>
