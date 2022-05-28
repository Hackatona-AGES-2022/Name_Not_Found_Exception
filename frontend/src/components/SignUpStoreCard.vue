<template>
  <div class="card__container px-6">
    <v-form id="storeCredentials" class="justify-space-between align-center">
      <v-row class="mt-8">
        <Input
          label="Nome da Empresa"
          placeholder="Atacadão do Cássio"
          variant="round"
          elevation="3"
          v-model="store.name"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="CNPJ"
          variant="round"
          elevation="3"
          v-model="store.cnpj"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="Endereço"
          variant="round"
          elevation="3"
          v-model="store.address"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="E-mail comercial"
          variant="round"
          elevation="3"
          v-model="store.email"
        />
      </v-row>
      <v-row class="mt-8">
        <Input
          label="Senha"
          variant="round"
          elevation="3"
          type="password"
          v-model="store.password"
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
  components: { Input, Button },
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
