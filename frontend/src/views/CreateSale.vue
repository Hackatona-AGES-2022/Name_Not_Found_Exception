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
      />
    </v-row>

    <v-row class="mt-8">
      <TextArea label="Descrição" variant="round" elevation="3" />
    </v-row>

    <v-row class="mt-8">
      <Input
        label="Quantidade do Lote"
        placeholder="300"
        variant="round"
        elevation="3"
        type="number"
      />
    </v-row>

    <v-row class="mt-8">
      <DatePicker />
    </v-row>

    <v-row class="mt-8">
      <v-col class="pa-0 mr-4">
        <Input
          label="Preço Padrão"
          placeholder="R$ 1,75"
          variant="round"
          elevation="3"
          type="number"
        />
      </v-col>
      <v-col class="pa-0">
        <Input
          label="Preço Desconto"
          placeholder="R$ 3,50"
          variant="round"
          elevation="3"
          type="number"
        />
      </v-col>
    </v-row>

    <v-row class="mt-8">
      <Input label="Palavras-chave" variant="round" elevation="3" />
    </v-row>
  </div>
</template>

<script>
import Input from "../components/Input.vue";
import TextArea from "../components/TextArea.vue";
import DatePicker from "../components/DatePicker.vue";

export default {
  components: { Input, TextArea, DatePicker },
  mounted() {
    this.$root.showToolbar("Mercado Pão de Açúcar");
  },
};
</script>

<style></style>
