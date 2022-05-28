<template>
  <div class="card__container">
    <v-form id="storeCredentials" class="justify-space-between align-center">
      <Input
        label="Digite seu nome completo"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        class="mt-15"
        elevation="3"
        v-model="user.name"
      />
      <Input
        label="Digite seu email"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
        class="mt-15"
        v-model="user.email"
      />
      <Input
        label="Crie uma senha"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
        class="mt-15"
        type="password"
        v-model="user.password"
      />
      <Input
        label="url da imagem"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        class="mt-15"
        elevation="3"
        v-model="user.photo_link"
      />
    </v-form>
    <div
      type="submit"
      class="card__submitbutton d-flex justify-center align-center mt-15"
      form="storeCredentials"
      value="Submit"
      v-ripple
      @click="clickHandler"
    >
      Submit
    </div>
  </div>
</template>

<script>
import { HTTP } from "../api/HTTP";
import Input from "./Input.vue";
export default {
  props: ["title"],
  mounted() {
    console.log(this.title);
  },
  components: { Input },
  data: () => ({
    user: {
      name: "",
      email: "",
      password: "",
      photo_link: "",
    },
  }),
  methods: {
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