<template>
  <v-container class="px-8">
    <v-row class="mt-12 justify-center">
      <img src="../assets/conjunkt.svg" />
    </v-row>
    <v-row class="mt-14">
      <Input label="E-mail" variant="round" elevation="3" v-model="email" />
    </v-row>
    <v-row class="mt-10">
      <Input
        label="Senha"
        type="password"
        variant="round"
        elevation="3"
        v-model="password"
      />
    </v-row>
    <div class="mt-12">
      <v-row class="mt-14 justify-center">
        <Button
          class="login-button"
          title="Entrar"
          extended
          rounded
          @click="loginButtonClick"
        />
      </v-row>
      <v-row class="justify-center mt-8">
        <span
          >Ainda não possui login?
          <span class="link" @click="onSignupClick">Cadastre-se!</span></span
        >
      </v-row>
    </div>
  </v-container>
</template>

<script>
import Input from "../components/Input.vue";
import Button from "../components/Button.vue";
import { HTTP } from "../api/HTTP";
import { saveUser } from "../service/UserService";

export default {
  data: () => ({
    email: "",
    password: "",
  }),
  mounted() {
    this.$root.hideToolbar();
  },
  components: {
    Input,
    Button,
  },
  methods: {
    loginButtonClick() {
      const userType =
        this.$route.query.user_type === "user" ? "user" : "store";
      HTTP.post(`${userType}/authorization`, {
        email: this.email,
        password: this.password,
      })
        .then((data) => {
          saveUser(data.data);
          this.$router.push(`/${userType}/home`);
        })
        .catch(() => {
          this.$root.showSnackbar("E-mail ou senha incorretos.");
        });
    },
    onSignupClick() {
      const userType = this.$route.query.user_type;
      const path = userType ? `/sign-up?user_type=${userType}` : "/sign-up";
      this.$router.push(path);
    },
  },
};
</script>

<style>
.login-button {
  width: 200px;
}
.link {
  text-decoration: underline;
}
</style>
