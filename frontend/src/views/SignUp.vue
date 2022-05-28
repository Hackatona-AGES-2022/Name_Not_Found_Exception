<template>
  <v-container class="px-8 mt-4">
    <v-row>
      <span class="view__title">O que você deseja fazer no aplicativo?</span>
    </v-row>
    <v-row class="mt-6">
      <SignUpCard title="Quero Comprar" isStore="false"/>
    </v-row>
    <v-row class="justify-space-between">
    <SignUpCard title="Quero Vender" isStore/>
    </v-row>
  </v-container>
</template>

<script>
import SignUpCard from '../components/SignUpCard.vue';

export default {
  name: "SignUp",
  components: {SignUpCard}
};
</script>
