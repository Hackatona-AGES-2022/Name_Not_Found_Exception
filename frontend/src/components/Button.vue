<template>
  <v-btn v-bind="$attrs" v-on="$listeners" class="py-6">{{ title }}</v-btn>
</template>

<script>
export default {
  inheritAttrs: false,
  props: ["title"],
};
</script>

<style lang="scss" scoped>
.v-btn {
  text-transform: none;
  color: #fff !important;
  font-size: 19px;
  font-weight: 500;
  box-sizing: border-box;
  transition: 300ms;
  letter-spacing: 0.02cm;
  background-image: linear-gradient(90deg, #85db46, #375c1d);
}
</style>
