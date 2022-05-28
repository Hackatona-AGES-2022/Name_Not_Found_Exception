<template>
  <v-textarea
    v-bind="$attrs"
    v-on="$listeners"
    :class="[variantClass, elevation]"
    outlined
    hide-details
  />
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    variant: String,
  },
  computed: {
    variantClass() {
      return this.variant || "";
    },
    elevation() {
      return `elevation-${this.$attrs.elevation || 0}`;
    },
  },
};
</script>

<style lang="scss" scoped>
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
