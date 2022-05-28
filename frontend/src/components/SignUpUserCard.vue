<template>
  <div class="card__container px-6 mt-12">
    <v-form id="storeCredentials" class="justify-space-between align-center">
      <v-row>
        <Input
          label="Nome Completo"
          placeholder="João da Silva"
          variant="round"
          elevation="3"
          v-model="user.name"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="E-mail"
          placeholder="funciona@por.favor"
          variant="round"
          elevation="3"
          v-model="user.email"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="Senha"
          variant="round"
          elevation="3"
          :type="inputType"
          v-model="user.password"
          :append-icon="inputType === 'password' ? 'mdi-eye-off' : 'mdi-eye'"
          ref="pass"
          @click:append="onPassClick"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="url da imagem"
          variant="round"
          elevation="3"
          v-model="user.photo_link"
        />
      </v-row>
    </v-form>
    <v-row class="mt-8 justify-center">
      <Button
        @click="clickHandler"
        rounded
        extended
        title="Cadastrar"
        style="width: 200px"
      />
    </v-row>
  </div>
</template>

<script>
import { HTTP } from "../api/HTTP";
import Input from "./Input.vue";
import Button from "./Button.vue";

export default {
  props: ["title"],
  mounted() {
    console.log(this.title);
  },
  components: { Input, Button },
  data: () => ({
    user: {
      name: "",
      email: "",
      password: "",
      photo_link: "",
    },
    inputType: "password",
  }),
  methods: {
    onPassClick() {
      this.inputType = this.inputType === "password" ? "type" : "password";
    },
    clickHandler() {
      HTTP.post("/user", this.user)
        .then(() => {
          this.$router.push("/sign-in?user_type=user");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.card {
  &__submitbutton {
    width: 100%;
    max-width: flex;
    height: 50px;
    background-color: #4df95e;
    border-radius: 16px;
    margin: 5px;
  }
}
</style>
