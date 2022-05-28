<template>
  <div class="card__container" v-ripple @click="$emit('click')">
    <div class="card__content d-flex justify-center align-center">
      <div class="image d-flex justify-left align-center">
        <img v-if="isStore" src="../assets/quero_vender.svg" alt="arroz" />
        <img v-else src="../assets/quero_comprar.svg" alt="arroz" />
      </div>
      <span class="d-flex justify-left align-left card-title">{{ title }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title", "isStore"],
  mounted() {
    console.log(this.title, this.isStore);
  },
};
</script>

<style lang="scss" scoped>
.card {
  &__container {
    width: 100%;
    max-width: flex;
    height: 160px;
    background-image: linear-gradient(90deg, #76e426, #4da80a);
    border-radius: 16px;
    margin: 5px;
    padding: 10px;
  }

  &__content {
    height: 100%;
    display: flex;
    .image {
      height: 50%;
      align-self: center;
    }

    .waves {
      border-radius: 16px;
      height: 50%;
      background-image: url(../assets/waves.svg);
      bottom: 0;
      padding: 22px 4px 0 4px;
      color: greenyellow;
      background-position: -120px;

      .sale {
        &__title {
          font-weight: 600;
        }

        &__quantity {
          display: flex;
          &--low {
            font-size: 1.4rem;
            font-weight: 600;
          }
        }
      }
    }
  }
}
.card-title {
  font-family: "Poppins";
  font-size: 35px;
  font-weight: 700;
  text-align: center;
  color: #fff;
}
</style>
