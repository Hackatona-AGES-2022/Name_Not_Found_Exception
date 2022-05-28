<template>
  <div class="px-8 mt-4">
    <v-row class="small mt-4">
      <span class="view__title">Cadastrar Promoção</span>
    </v-row>

    <v-row class="mt-8">
      <Input
        label="Título"
        placeholder="Arroz 1KG"
        variant="round"
        elevation="3"
        v-model="sale.title"
      />
    </v-row>

    <v-row class="mt-8">
      <TextArea
        label="Descrição"
        variant="round"
        elevation="3"
        v-model="sale.description"
      />
    </v-row>

    <v-row class="mt-8">
      <Input
        label="Quantidade do Lote"
        placeholder="300"
        variant="round"
        elevation="3"
        type="number"
        v-model="sale.targetAmount"
        hint="Quantos itens terão na sua promoção."
      />
    </v-row>

    <v-row class="mt-8">
      <DatePicker v-model="sale.expirationDate" />
    </v-row>

    <v-row class="mt-8">
      <v-col class="pa-0 mr-4">
        <Input
          label="Preço Padrão"
          placeholder="R$ 1,75"
          variant="round"
          elevation="3"
          type="number"
          v-model="sale.defaultPrice"
          hint="O preço fora da promoção."
        />
      </v-col>
      <v-col class="pa-0">
        <Input
          label="Preço Desconto"
          placeholder="R$ 3,50"
          variant="round"
          elevation="3"
          type="number"
          v-model="sale.targetPrice"
          hint="O preço caso a promoção for completada."
        />
      </v-col>
    </v-row>

    <v-row class="justify-center mt-8">
      <Button title="Cadastrar" @click="onCreateButtonClick" extended rounded />
    </v-row>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
import TextArea from "../components/TextArea.vue";
import DatePicker from "../components/DatePicker.vue";
import Button from "../components/Button.vue";
import axios from "axios";

export default {
  components: { Input, TextArea, DatePicker, Button },
  data: () => ({
    sale: {},
  }),
  mounted() {
    this.$root.showToolbar("Mercado Pão de Açúcar");
  },
  methods: {
    onCreateButtonClick() {
      const saleDTO = {
        cnpj: "9696969696",
        title: this.sale.title,
        description: this.sale.description,
        target_amount: Number(this.sale.targetAmount),
        expiration_date: this.sale.expirationDate,
        target_price: Number(this.sale.targetPrice),
        default_price: Number(this.sale.defaultPrice),
        photo_link: "",
      };

      axios
        .post("/sale", saleDTO)
        .then(() => {
          //   this.$root.showSnackbar()
          console.log("funcionou!!!");
        })
        .catch(() => {
          console.log(":/");
        });
    },
  },
};
</script>

<style></style>
