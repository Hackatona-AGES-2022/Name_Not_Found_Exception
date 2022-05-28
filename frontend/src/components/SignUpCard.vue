<template>
  <div class="card__container" v-ripple @click='$emit(click)'>
    <div class="card__content d-flex justify-center align-center">
        <div class="image d-flex justify-left align-center">
            <img src="../assets/arroz.svg" alt="arroz" />
        </div>
        <span class="d-flex justify-left align-left">{{title}}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title"],
  mounted() {
    console.log(this.title);
  },
};
</script>

<style lang="scss" scoped>
.card {
  &__container {
    width: 100%;
    max-width: flex;
    height: 200px;
    background-color: #4df95e;
    border-radius: 16px;
    margin: 5px;
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
</style>
