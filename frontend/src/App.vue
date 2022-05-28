<template>
  <v-app>
    <v-app-bar class="toolbar" app color="primary" dark>
      <v-btn icon>
        <v-icon>mdi-menu</v-icon>
      </v-btn>

      <v-app-bar-title v-if="$root.isToolbarVisible">{{
        $root.toolbarTitle
      }}</v-app-bar-title>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Montserrat+Alternates:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Poppins:ital,wght@0,200;0,300;0,400;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap");
.v-application {
  font-family: "Poppins", sans-serif !important;
}

.view {
  &__container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: calc(100% - 56px);
  }

  &__title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #515151bf;
  }
}

.toolbar {
  background-image: linear-gradient(90deg, #85db46, #66a836);
}
</style>
