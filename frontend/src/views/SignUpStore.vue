<template>
  <div>
    <div class="view__title mt-8">Cadastro de Loja</div>
    <SignUpStoreCard />
  </div>
</template>

<script>
import SignUpStoreCard from "../components/SignUpStoreCard.vue";

export default {
  name: "SignUpStore",
  components: { SignUpStoreCard },
};
</script>

<style>
.view__title {
  font-size: 1.9rem;
  text-align: center;
}
</style>
