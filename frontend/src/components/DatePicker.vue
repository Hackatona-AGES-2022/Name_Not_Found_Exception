<template>
  <v-menu
    ref="menu"
    v-model="menu"
    :close-on-content-click="false"
    :return-value.sync="date"
    transition="scale-transition"
    offset-y
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <Input
        v-model="date"
        label="Data de Expiração"
        prepend-icon="mdi-calendar"
        readonly
        v-bind="attrs"
        v-on="on"
        variant="round"
        elevation="3"
        @input="$emit('change', date)"
      />
    </template>
    <v-date-picker
      v-model="date"
      no-title
      scrollable
      v-bind="$attrs"
      v-on="$listeners"
    >
      <v-spacer></v-spacer>
      <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
      <v-btn text color="primary" @click="$refs.menu.save(date)"> OK </v-btn>
    </v-date-picker>
  </v-menu>
</template>

<script>
import Input from "./Input.vue";

export default {
  components: { Input },
  data: () => ({
    menu: false,
    date: null,
  }),
};
</script>

<style lang="scss">
.v-text-field {
  border-radius: 10px;
}

.round {
  border-radius: 16px;
  ::v-deep fieldset {
    border: none;
  }
}
</style>
