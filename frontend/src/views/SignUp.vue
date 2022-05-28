<template>
  <v-container class="px-8 mt-4">
    <v-row>
      <span class="view__title">O que você deseja fazer no aplicativo?</span>
    </v-row>
    <v-row class="mt-8">
      <SignUpCard
        title="Quero Comprar"
        isStore="false"
        @click="goToUserSignUp"
      />
    </v-row>
    <v-row class="mt-8 justify-space-between">
      <SignUpCard title="Quero Vender" isStore @click="goToStoreSignUp" />
    </v-row>
  </v-container>
</template>

<script>
import SignUpCard from "../components/SignUpCard.vue";
export default {
  name: "SignUp",
  components: { SignUpCard },
  methods: {
    goToUserSignUp() {
      this.$router.push("/sign-up-user");
    },
    goToStoreSignUp() {
      this.$router.push("/sign-up-store");
    },
  },
};
</script>
