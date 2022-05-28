<template>
  <div class="card__container" v-ripple>
    <div class="card__content">
      <div class="image">
        <img src="../assets/arroz.svg" alt="arroz" />
      </div>
      <div class="waves">
        <div class="sale__title">Sal refinado 1KG</div>
        <div class="sale_quantity">
          <span class="sale_quantity--low">147</span>
          <span class="sale_quantity--high">/200 un.</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["sale"],
  mounted() {
    console.log(this.sale);
  },
};
</script>

<style lang="scss" scoped>
.card {
  &__container {
    width: 100%;
    max-width: 165px;
    height: 200px;
    background-color: #ececec;
    border-radius: 16px;
  }

  &__content {
    height: 100%;
    display: flex;
    flex-direction: column;

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
      color: white;
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
          &--high {
          }
        }
      }
    }
  }
}
</style>
