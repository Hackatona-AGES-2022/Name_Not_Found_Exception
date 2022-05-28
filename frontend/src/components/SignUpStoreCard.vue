<template>
  <div class="card__container">
    <v-form id="storeCredentials" class="justify-space-between align-center">
      <Input
        label="Digite o nome da empresa"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        class="mt-10"
        elevation="3"
        v-model="store.name"
      />
      <Input
        label="Digite o CNPJ da empresa"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
        class="mt-10"
        v-model="store.cnpj"
      />
      <Input
        label="Digite o email comercial"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
        class="mt-10"
        v-model="store.email"
      />
      <Input
        label="Digite o endereço da empresa"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        class="mt-10"
        elevation="3"
        v-model="store.address"
      />
      <Input
        label="Crie uma senha"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        elevation="3"
        class="mt-10"
        type="password"
        v-model="store.password"
      />
      <Input
        label="url da imagem"
        prepend-inner-icon="mdi-magnify"
        append-icon="mdi-filter-variant "
        variant="round"
        class="mt-10"
        elevation="3"
        v-model="store.photo_link"
      />
    </v-form>
    <div
      type="submit"
      class="card__submitbutton d-flex justify-center align-center mt-10"
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
  data: () => ({
    store: {
      name: "",
      cnpj: "",
      email: "",
      address: "",
      password: "",
      photo_link: "",
      description: "",
    },
  }),
  components: { Input },
  methods: {
    clickHandler() {
      HTTP.post("/store", this.store)
        .then(() => {
          this.$router.push("/sign-in?user_type=store");
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