<template>
  <div>
    <div class="view__title mt-8">Cadastro de Usuário</div>
    <SignUpUserCard />
  </div>
</template>

<script>
import SignUpUserCard from "../components/SignUpUserCard.vue";

export default {
  name: "SignUpUser",
  components: { SignUpUserCard },
};
</script>

<style>
.view__title {
  font-size: 1.9rem;
  text-align: center;
}
</style>
